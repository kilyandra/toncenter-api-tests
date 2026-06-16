# TON Center API Test Suite

[![Tests](https://github.com/kilyandra/toncenter-api-tests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/kilyandra/toncenter-api-tests/actions/workflows/tests.yml)

Automated test suite for the [TON Center API v2](https://toncenter.com/api/v2) built with pytest.  
Validates response structure, business logic, and error handling across API endpoints.

## Setup

Get a free API key from [@tonapibot](https://t.me/tonapibot) on Telegram and add it to a `.env` file:

    TON_API_KEY=your_api_key

Then install dependencies and run:

    pip install -r requirements.txt
    pytest tests/

## Testing Approach
- **Integration tests** verify real API behavior and response contracts
- **Unit tests** cover scenarios that can't be reproduced via the live API (e.g. frozen accounts) using mocks

## Test Coverage
- `getAddressState` — active, uninitialized, frozen (mocked), invalid input
- `detectAddress` — raw, bounceable, non-bounceable, testnet, invalid input