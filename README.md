Inside README.md:

# Insurance Risk Analytics

A machine learning and analytics project focused on insurance risk assessment, exploratory data analysis, hypothesis testing, and predictive modeling.

## Project Structure

- `data/` → datasets tracked using DVC
- `notebooks/` → Jupyter notebooks for analysis
- `src/` → reusable Python source code
- `tests/` → unit tests
- `reports/` → reports and findings

## Setup

```bash
conda activate D:\python-data\env
pip install -r requirements.txt
Running Tests
pytest
Linting
flake8 src tests

---

# 9. Create a Simple Test

Inside `tests/`

Create:

```bash
type nul > tests\test_basic.py

Inside test_basic.py:

def test_example():
    assert 1 + 1 == 2