# Write your code here
import re


def ten_times_abs(string):
    return re.fullmatch('(abc){10}', string)