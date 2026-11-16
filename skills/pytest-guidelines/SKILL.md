---
name: pytest-guidelines
description: Write reliable, maintainable Python tests with pytest. Use when writing new tests, reviewing test code, refactoring test suites, or setting up test infrastructure for data engineering projects. Covers fixtures, parametrize, mocking, assertions, markers, configuration, and data pipeline testing patterns. Apply FIRST principles (Fast, Independent, Repeatable, Simple, Self-Testing).
metadata:
  author: Artefact
  version: "2.0"
  source: kode/src/content/docs/code/howto_guides/testing.mdx, kode/src/content/docs/code/howto_guides/code_review.mdx
  complexity: intermediate
---

# Pytest Guidelines

Use pytest as the default Python testing framework.

Apply FIRST principles in every test:

- Fast: keep tests quick enough for local and CI loops.
- Independent: avoid shared mutable state and order dependence.
- Repeatable: avoid non-deterministic inputs without control.
- Simple: test one behavior at a time with minimal setup.
- Self-Testing: keep execution automated with clear pass/fail outcomes.

## Test Type Decision Tree

1. Single function/class with no external systems?
   - Write a unit test.
2. Multiple components (service + repository + adapter)?
   - Write an integration test.
3. Full user or pipeline workflow from input to output?
   - Write an end-to-end test.
4. Data applications:
   - Unit: one transform.
   - Integration: sequence of transforms.
   - End-to-end: full pipeline run.

Default strategy: prioritize unit tests, add targeted integration tests, keep end-to-end tests for critical paths.

## Rules Quick Reference

| Category                        | Impact | Rule Headings                                            |
| ------------------------------- | ------ | -------------------------------------------------------- |
| Test Structure and Organization | HIGH   | 1. Standard Directory Layout; 2. Naming Conventions      |
| Fixtures                        | HIGH   | 3. Fixtures Over Setup/Teardown; 4. Factory Fixtures     |
| Parametrize                     | MEDIUM | 5. Parametrize to Eliminate Duplication                  |
| Mocking and Patching            | HIGH   | 6. monkeypatch for Overrides; 7. Mock at the Right Level |
| Assertions and Error Testing    | MEDIUM | 8. `pytest.raises(..., match=...)`; 9. `pytest.approx`   |
| Markers and Configuration       | MEDIUM | 10. Markers and Centralized pytest Configuration         |
| Data Engineering Patterns       | HIGH   | 11. DataFrame Fixtures; 12. In-Memory SQL Tests          |

## Rules

Examples focus on pytest patterns. Project-specific imports (for example application modules) are omitted for brevity unless relevant to the pattern.

### 1. Use Standard Directory Layout

Mirror source structure in `tests/` and keep shared fixtures in `conftest.py`.
**Incorrect:**

```text
project/
  app.py
  helpers.py
  test_misc.py
```

**Correct:**

```text
project/
  src/
    services/pricing.py
    pipelines/normalize.py
  tests/
    services/test_pricing.py
    pipelines/test_normalize.py
    conftest.py
```

Why:

- Makes behavior-focused tests easier to discover and review.
- Keeps shared setup reusable and consistent.


### 2. Follow Naming Conventions

Use `test_*.py` file names and `test_*` functions. Use `Test*` classes only for grouping.
**Incorrect:**

```python
# tests/pricing_checks.py

def pricing_case_one():
    assert calculate_total(100, 0.2) == 120
```

**Correct:**

```python
# tests/test_pricing.py

def test_calculate_total_applies_tax():
    assert calculate_total(100, 0.2) == 120

class TestDiscounts:
    def test_calculate_total_applies_discount_before_tax(self):
        assert calculate_total(100, 0.2, discount=0.1) == 108
```

Why:

- Ensures predictable pytest collection and readable CI output.

Validation command:

```bash
pytest --collect-only -q
```

### 3. Use Fixtures Over Setup/Teardown

Use `@pytest.fixture` with `yield` cleanup instead of unittest lifecycle methods.
**Incorrect:**

```python
import unittest

class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepo("sqlite:///:memory:")
    def tearDown(self):
        self.repo.close()
    def test_get_user(self):
        assert self.repo.get_user(1)["id"] == 1
```

**Correct:**

```python
import pytest

@pytest.fixture
def repo():
    instance = UserRepo("sqlite:///:memory:")
    yield instance
    instance.close()


def test_get_user(repo):
    assert repo.get_user(1)["id"] == 1
```

Why:

- Makes dependencies explicit and reduces hidden side effects.
- Allows intentional fixture scoping.


### 4. Use Factory Fixtures for Variants

Return callables from fixtures when tests need many object variants.
Use a factory fixture when the test object is a composite type (dict, dataclass, model) with multiple fields. Reserve bare parametrize for scalar or tuple inputs.
**Incorrect:**

```python
import pytest

@pytest.fixture
def bronze_customer():
    return {"tier": "bronze", "spend": 100}

@pytest.fixture
def silver_customer():
    return {"tier": "silver", "spend": 500}
```

**Correct:**

```python
import pytest

@pytest.fixture
def customer_factory():
    def build(*, tier="bronze", spend=0):
        return {"tier": tier, "spend": spend}
    return build


def test_gold_discount(customer_factory):
    customer = customer_factory(tier="gold", spend=2500)
    assert compute_discount(customer) == 0.2
```

Why:

- Avoids fixture explosion and keeps test setup maintainable.


### 5. Use Parametrize to Eliminate Duplication

Use `@pytest.mark.parametrize` for input-output variants. Add `ids` when auto-generated names are opaque (dicts, complex objects); skip ids for simple scalars where pytest's default output is clear.
**Incorrect:**

```python
def test_parse_yes():
    assert parse_flag("yes") is True

def test_parse_no():
    assert parse_flag("no") is False

def test_parse_invalid():
    assert parse_flag("maybe") is None
```

**Correct:**

```python
import pytest

@pytest.mark.parametrize(
    "raw, expected",
    [("yes", True), ("no", False), ("maybe", None)],
)
def test_parse_flag(raw, expected):
    assert parse_flag(raw) is expected

# Use indirect=True when params should be built by a fixture.
```

Why:

- Increases coverage without duplicating test logic.
- Improves failure readability when ids are needed.


### 6. Use monkeypatch for Simple Overrides

Use `monkeypatch` for environment and attribute overrides.
**Incorrect:**

```python
from unittest.mock import patch

def test_reads_region():
    with patch("os.environ", {"REGION": "eu-west-1"}):
        assert get_region() == "eu-west-1"
```

**Correct:**

```python
def test_reads_region(monkeypatch):
    monkeypatch.setenv("REGION", "eu-west-1")
    assert get_region() == "eu-west-1"


def test_uses_stubbed_endpoint(monkeypatch):
    monkeypatch.setattr(client_config, "API_URL", "http://stub")
    assert make_request_path("/health") == "http://stub/health"
```

Why:

- Integrates with pytest lifecycle and auto-restores state.


### 7. Mock at the Right Level

Patch where the object is imported and used.
CRITICAL: When the module under test imports from any non-standard-library module (external service or project package), you MUST mock those imports with `@patch("module_name.symbol")` before calling the function under test — where `module_name` is the exact filename of the module under test (without `.py`), not an import alias. Never call functions with external dependencies without mocking first.
**Incorrect:**

```python
from unittest.mock import patch

# service.py: from notifications import send_email
@patch("notifications.send_email")
def test_register_user_sends_welcome(mock_send):
    register_user("a@company.com")
    mock_send.assert_called_once()
```

**Correct:**

```python
from unittest.mock import patch

@patch("service.send_email")
def test_register_user_sends_welcome(mock_send):
    register_user("a@company.com")
    mock_send.assert_called_once_with("a@company.com", template="welcome")
```

Why:

- Prevents ineffective mocks and false confidence.


### 8. Use pytest.raises with match

Assert both exception type and message pattern.
**Incorrect:**

```python
import pytest

def test_negative_amount_rejected():
    with pytest.raises(ValueError):
        validate_amount(-1)
```

**Correct:**

```python
import pytest

def test_negative_amount_rejected():
    with pytest.raises(ValueError, match="amount must be >= 0"):
        validate_amount(-1)
```

Why:

- Verifies the intended failure path, not just any exception of the same type.


### 9. Use pytest.approx for Floats

CRITICAL: ALWAYS use `pytest.approx` when asserting any float value — including results from arithmetic, numeric transforms, aggregations, pandas/numpy operations, and `.tolist()` calls on float columns. Never compare floats with `==` directly.
**Incorrect:**

```python
def test_conversion_rate():
    assert compute_rate(10, 3) == 3.3333333333
```

**Correct:**

```python
import pytest

def test_conversion_rate():
    assert compute_rate(10, 3) == pytest.approx(3.3333333333, rel=1e-6)


def test_probability_is_normalized():
    probs = normalize([1, 2, 3])
    assert sum(probs) == pytest.approx(1.0, abs=1e-12)
```

Why:

- Avoids flaky failures caused by floating-point representation.


### 10. Use Markers and Centralize pytest Configuration

CRITICAL: If a function's docstring says it is "slow" or describes contacting an external service (email, scheduler, queue, database, API), ALWAYS add `@pytest.mark.slow` and `@pytest.mark.integration` to every test for that function. Use markers for selective execution and define marker policy in `pyproject.toml`.
**Incorrect:**

```python
# Unmarked long-running test in default suite

def test_full_pipeline_backfill():
    run_backfill(days=365)
```

**Correct:**

```python
import pytest

@pytest.mark.slow
@pytest.mark.integration
def test_full_pipeline_backfill():
    run_backfill(days=365)
```

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
markers = [
  "slow: long-running tests",
  "integration: cross-component behavior",
  "e2e: end-to-end workflow tests",
]
```

Why:

- Keeps local runs fast and CI intent explicit.
- Catches marker typos with `--strict-markers`.


### 11. Use DataFrame Fixtures for Pipeline Tests

Create minimal DataFrames inline to test transformations in isolation.
**Incorrect:**

```python
# Hidden dependency on external test files

def test_normalize_orders():
    df = pandas.read_csv("/tmp/orders_sample.csv")
    result = normalize_orders(df)
    assert len(result) == 3
```

**Correct:**

```python
import pandas as pd
import pytest

@pytest.fixture
def raw_orders_df():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "country": ["FR", "fr", "US"],
            "amount": [10.0, 15.0, 20.0],
        }
    )


def test_normalize_orders_uppercases_country(raw_orders_df):
    result = normalize_orders(raw_orders_df)
    assert result["country"].tolist() == ["FR", "FR", "US"]
```

Why:

- Keeps tests deterministic, readable, and easy to review.

Tip — after `dropna()`, `merge()`, or filtering, call `reset_index(drop=True)` before comparing and prefer `pd.testing.assert_frame_equal` for full checks.


### 12. Test SQL Transforms with In-Memory Databases

Use DuckDB or SQLite in memory for SQL transform tests.
**Incorrect:**

```python
# Depends on external warehouse state

def test_daily_sales_aggregation(real_warehouse_client):
    result = real_warehouse_client.query("SELECT * FROM marts.daily_sales")
    assert result.row_count == 42
```

**Correct:**

```python
import duckdb


def test_daily_sales_aggregation_sql():
    conn = duckdb.connect(":memory:")
    conn.execute("CREATE TABLE orders(order_date DATE, amount DOUBLE)")
    conn.execute(
        "INSERT INTO orders VALUES ('2025-01-01', 10.0), ('2025-01-01', 15.0), ('2025-01-02', 7.0)"
    )
    rows = conn.execute(
        """
        SELECT CAST(order_date AS VARCHAR) AS order_date, SUM(amount) AS total_amount
        FROM orders
        GROUP BY order_date
        ORDER BY order_date
        """
    ).fetchall()
    assert rows == [("2025-01-01", 25.0), ("2025-01-02", 7.0)]
```

Why:

- Removes external infra dependencies and keeps SQL tests fast.


## Common Pitfalls

| Anti-pattern                       | Why it is risky                                    | Better approach                              |
| ---------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| Testing implementation details     | Refactors break tests without behavior regressions | Assert externally visible outcomes           |
| Cross-test dependencies            | Creates order-sensitive flakes                     | Isolate state and use fixture scoping        |
| Broad assertions (`assert result`) | Can pass for wrong reasons                         | Assert exact values, shape, and invariants   |
| Missing edge cases                 | Failures appear in production only                 | Add null, empty, boundary, and invalid cases |
| Over-mocking domain logic          | Unrealistic tests hide regressions                 | Mock external boundaries only                |
| Slow tests in default run          | Developers skip running tests                      | Mark and split slow suites                   |

## When Stuck

| Problem                    | Quick check                       | Action                               |
| -------------------------- | --------------------------------- | ------------------------------------ |
| Test not discovered        | Run `pytest --collect-only -q`    | Rename files/functions to `test_*`   |
| Marker warning/error       | Check marker registration         | Register markers in `pyproject.toml` |
| Flaky date/random behavior | Look for non-deterministic inputs | Freeze time and seed randomness      |
| Mock does not apply        | Inspect patch target path         | Patch where symbol is used           |
| Suite too slow             | Run `pytest --durations=10`       | Mark and isolate slow tests          |
