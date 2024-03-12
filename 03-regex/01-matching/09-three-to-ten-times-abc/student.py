# Write your code here
import re


def ten_times_abc(string):
    return re.fullmatch('(abc){3,10}', string)