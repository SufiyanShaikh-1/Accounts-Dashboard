###
To run the test suite, simply type 'q2 test'
###

No project is truly complete without unit tests. With the Antilles SDK, we officially support
pytest (https://docs.pytest.org/en/latest/index.html)

There is absolutely nothing stopping you from using your own test framework, but assuming
you are ok using the default, we've generated a few tests for you. Any tests in this folder
will be automatically discovered based on the following rules.

1. Is the test in a class called Test*
2. Is the test in a function called test_

The tests we've generated are currently disabled. To enable them, remove the lines marked with
@pytest.mark.skip
