import argparse
import os

msg = 'This will be provide unittest broilerplate for development'

parser = argparse.ArgumentParser(description=msg)
parser.add_argument("-cu", "--CreateUnittest", help = "Create a solution with unit test")
args = parser.parse_args()

if args.CreateUnittest:
    print("Displaying Output as: % s" % args.CreateUnittest)
    print(os.getcwd())
    path = os.getcwd() + "\\" + args.CreateUnittest
    os.mkdir(path)
    content = [
        'import unittest\n',
        'from typing import List\n',
        'class Solution:\n',
        '\tdef MethodName():\n'
        '\t\t# TODO : write solution here\n',
        '\t\tpass\n',
        '\n\n',
        'class TestSolution(unittest.TestCase):\n',
        '\tdef setUp(self):\n',
        '\t\tself.solution = Solution()\n\n'
        '\tdef test_sampleTest(self):\n',
        '\t\t# Arrange\n',
        '\n',
        '\t\t# Act\n',
        '\n',
        '\t\t# Assert\n',
        '\t\tpass\n',
        '\n\n',
        'if __name__ == "__main__":\n',
        '\tunittest.main()'
    ]
    with open(path + "\\" + "Solution.py", 'a') as file:
       file.writelines(content)