# Selenium Python Automation Framework

## Project Overview
This project is a Selenium Python Automation Framework designed for end-to-end UI automation
using Python. It follows the Page Object Model (POM) design pattern and supports both
BDD (Behave) and PyTest for test execution.

## Tech Stack
- Python 3
- Selenium WebDriver
- PyTest
- Behave (BDD)
- Page Object Model (POM)
- Jenkins (CI/CD)

## Framework Highlights
- End-to-end UI automation using Selenium with Python
- BDD implementation using Behave feature files
- PyTest-based execution with reusable fixtures
- Page Object Model for better maintainability
- CI/CD support using Jenkins

## Project Structure
features/       → BDD feature files  
pages/          → Page Object classes  
tests/          → Test execution files  
utils/          → Reusable utilities  
requirements.txt → Project dependencies  

## How to Run Tests

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run PyTest tests
pytest

### 3. Run BDD tests
behave

## CI/CD
This framework is CI/CD ready and can be integrated with Jenkins for automated test execution.


## Author
Sangeethavani Subramanian  
QA Automation Engineer
