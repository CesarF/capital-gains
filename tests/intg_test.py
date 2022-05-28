import json, subprocess
from typing import List
from unittest import TestCase


class IntegrationTest(TestCase):

    def setUp(self):
        output = subprocess.run(['pwd'], capture_output = True, text = True)
        self._path = output.stdout.replace('\n','')

    def execute_command(self, filename:str) -> List[str]:
        cmd = 'python3 %s/main.py < %s/tests/txt/%s' % (self._path, self._path, filename)
        # Since last element is empty, we return a list without it
        return subprocess.run(cmd, capture_output = True, text = True, shell = True).stdout.split('\n')[:-1]
    
    def str_to_json(self, str_line:str):
        return json.loads(str_line)

    def test_case_1(self):
        result = self.execute_command('test1.txt')
        expected_result = [{'tax': 0.00},{'tax': 0.00},{'tax': 0.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_2(self):
        result = self.execute_command('test2.txt')
        expected_result = [{'tax': 0.00},{'tax': 10000.00},{'tax': 0.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_3(self):
        result = self.execute_command('test3.txt')
        expected_result = [{'tax': 0.00},{'tax': 0.00},{'tax': 1000.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_4(self):
        result = self.execute_command('test4.txt')
        expected_result = [{'tax': 0.00},{'tax': 0.00},{'tax': 0.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_5(self):
        result = self.execute_command('test5.txt')
        expected_result = [{'tax': 0.00},{'tax': 0.00},{'tax': 0.00},{'tax': 10000.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_6(self):
        result = self.execute_command('test6.txt')
        expected_result = [{'tax': 0.00},{'tax': 0.00},{'tax': 0.00},{'tax': 0.00},{'tax': 3000.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_7(self):
        result = self.execute_command('test7.txt')
        expected_result = [{'tax':0.00}, {'tax':0.00}, {'tax':0.00}, {'tax':0.00}, {'tax':3000.00}, {'tax':0.00}, {'tax':0.00}, {'tax':3700.00}, {'tax':0.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_8(self):
        result = self.execute_command('test8.txt')
        expected_result = [{'tax':0.00},{'tax':80000.00},{'tax':0.00},{'tax':60000.00}]
        self.assertEqual(expected_result, self.str_to_json(result[0]))

    def test_case_1_and_2(self):
        result = self.execute_command('test1+2.txt')
        expected_result = [[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}], [{"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}]]
        for index, item in enumerate(result):
            self.assertEqual(expected_result[index], self.str_to_json(item))