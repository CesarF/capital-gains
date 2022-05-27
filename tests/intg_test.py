import subprocess
from unittest import TestCase


class IntegrationTest(TestCase):

    def test_cases(self):
        output = subprocess.run(['pwd'], capture_output=True, text=True)
        path = str(output.stdout).replace('\n','')
        result = subprocess.run(['python3', path + '/main.py'], args= '< '+ path + '/tests/txt/all.txt', capture_output=True, text=True)
        print(result)
