import unittest

def main():

    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='tests', pattern='*test.py')
    testrunner = unittest.TextTestRunner(verbosity=2)
    testrunner.run(tests)

# Call the function to run all tests
main()