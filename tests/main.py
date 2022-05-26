if __name__ == '__main__':
    from unittest import TestLoader, TextTestRunner


    loader = TestLoader()
    suite = loader.discover('./', pattern = '*_test.py')

    runner = TextTestRunner(verbosity = 2)
    runner.run(suite)