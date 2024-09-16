This project contains automation tests for SauceDemo (Used this site for automation demo) using Python, Selenium, and pytest. It includes setup instructions, usage guidelines, and how to run the tests with parallel execution and Allure reporting.

## Project Structure

- `config/`
  - `config.py`: Configuration settings for the test automation.
- `drivers/`
  - `chromedriver`: Chrome WebDriver binary.
  - `geckodriver`: Gecko WebDriver binary for Firefox.
- `tests/`
  - `test_login.py`: Test cases for the login functionality.
  - `test_checkout.py`: Test cases for the checkout functionality.
  - `test_confest.py`: Test cases for various user flows.
- `reports/`
  - `allure_reports/`: Directory where Allure reports will be generated.
- `requirements.txt`: List of required Python packages.
- `pytest.ini`: Pytest configuration file.
- `README.md`: This file.

## Prerequisites

- Python 3.8 or higher
- pip
- WebDriver binaries (chromedriver and geckodriver)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository-name

