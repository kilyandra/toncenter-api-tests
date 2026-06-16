# TON API Test Suite

[![Tests](https://github.com/kilyandra/toncenter-api-tests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/kilyandra/toncenter-api-tests/actions/workflows/tests.yml)

Automated test suite for the [TON Center API v2](https://toncenter.com/api/v2).  
Validates response structure, business logic, and error handling across API endpoints.

## Stack
- Python 3.13
- pytest
- httpx
- pydantic

## How to Run
```
pip install -r requirements.txt
pytest tests/
```

## Testing Approach
- **Integration tests** verify real API behavior and response contracts
- **Unit tests** cover scenarios that can't be reproduced via the live API (e.g. frozen accounts) using mocks

## Test Coverage
- `getAddressState` — active, uninitialized, invalid input, frozen (mocked)