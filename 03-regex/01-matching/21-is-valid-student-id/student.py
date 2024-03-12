# Write your code here
import re
def is_valid_student(string):
    return re.fullmatch('r|R|s|S[0-9]{7}',string)