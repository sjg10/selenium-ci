# selenium-ci

This project serves as a template to run a set of selenium tests in python in Github Actions CI against a chosen URL.

These tests can either be:
 - built with the [Selenium IDE](https://www.selenium.dev/selenium-ide/), exported as pytest, and modified as shown in `tests/test_welcome.py`
 - written directly

Just fork this repo, change the `url.txt` file as needed, add new tests, and you are away. 
