import json
import re
import sys

parameter1 = sys.argv[1]
parameter2 = sys.argv[2]

#print(parameter1, " parameter 1")
#print("parameter 2 ", parameter2)
s = parameter2

####################################
####################################
####################################
##### here is the script to detect the error
spliting = parameter2.splitlines()
#print(spliting)
try:
  type_of_error = spliting[-1]
except IndexError:
  exit(0)


print("splitting ", type_of_error)

#print(parameter1)
####################################
####################################
####################################
"""# Extract all lines that start with "  File "
lines = re.findall(r"  File .*", s)

# Extract the first two lines
first_two_lines = lines[:2]

# Join the lines into a single string
first_string = "\n".join(first_two_lines)

# Extract the last line that starts with "    "
last_line = re.search(r"^    .*", s, re.MULTILINE)
if last_line:
    second_string = last_line.group(0)
else:
    second_string = ""

print(first_string)"""

####################################
####################################
####################################
########### detects what object is causing the error
"""# Define regular expressions to extract function calls and lines of code
function_call_pattern = r'\b\w+\(.*?\)'
code_line_pattern = r'  File ".*?", line \d+, in .*?\n\s+(.*?)\n'

# Find function calls and lines of code in the traceback error
#function_call_matches = re.findall(function_call_pattern, s)
code_line_matches = re.findall(code_line_pattern, s)

# Output the extracted function calls and lines of code
print("Extracted function calls:")
for function_call in function_call_matches:
    print(function_call)

print("\nExtracted lines of code:")
for code_line in code_line_matches:
    print("\n",code_line)"""

obj = list()
for i in range(0,len(spliting)): #0 - 6
    if 'File' in spliting[i]:
       obj.append(spliting[i+1].strip())
#print(obj, " object ") 
    

####################################
####################################
####################################
file_name = "stack.json"

temp_dict = []

for i in range(0,len(spliting)):
  print(i,'\n')
  if 'File' in spliting[i]:
    a = spliting[i]
    b = spliting[i+1]
    temp_dict.append({a.strip(): b.strip()})



single_dict = temp_dict[-1]
key = next(iter(single_dict))
single_dict[key] = f'{single_dict[key]}, {type_of_error}'
#print(single_dict, ' single dict')
#print(temp_dict, ' temp dict ')


temp_object = {}
for i in reversed(range(0, len(temp_dict))):
  temp_object[(len(temp_dict)-1)-i] = temp_dict[i]
#print(temp_object)


json_string = json.dumps(temp_object, indent=2)
with open(f'./{file_name}', 'w') as f:
    f.write(json_string)
####################################
####################################
####################################