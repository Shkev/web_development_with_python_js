# Lecture 5: Testing and Continuous Integration and Delivery (CI/CD)

## Testing
* Using `assert` in Python
  * `assert CONDITION`
  * If condition is `True` nothing happens, otherwise an exception
* Add tests to various points in the program to ensure that it does what you want it to do
* Python code can be tested in the terminal (by importing functions/classes from the file being tested)
  * This method can also be used with other test files (ex: test0.py, test0.sh)
* Libraries that help with testing: unittest
* Unittest built into Django. Tests can be run in the tests.py file
* Selenium allows testing web browser functions (like javascript functionality)

## CI/CD
* **CI** - Frequently merging to main branch of project (ex: master) and automatically running tests
  * Prevents large, difficult to resolve merge conflicts
* **CD** - Shorter release cycles. Releasing changes every few days/weeks instead of waiting a long time before releasing a version

### GitHub Actions
* Automates some actions (ex: tests) when code is pushed to a repository
  * Written in YAML
  * Must be in root directory of repository
