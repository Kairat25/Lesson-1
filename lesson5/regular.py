import re

text = "Hello! my name is Jack."

"""
    re.search
"""
# result = re.search('l', text)
# print(text[result.start()])
"""
    re.findall
"""
# result = re.findall('l', text)
# print(result)
"""
    re.match
    Is Valid Phone Number?
"""

result = re.match('l', text)

print(result)