import json
import sys

parameter1 = sys.argv[1]
val=None
file=None
loc=None

with open('./stack.json', 'r') as f:
    a = f.read()
    json_object = json.loads(a)
    
    val = json_object[parameter1]
    #print(val)

for key,value in val.items():
    file=key
    loc=value

# Given string
#print(file)

string = file
# Split the string based on double quotes
parts = string.split('"')
# Extract the content inside quotes
content_inside_quotes = parts[1]

last_backslash_index = string.rfind('\\')
# Use string slicing to extract the substring after the last backslash
file_name_with_extension = string[last_backslash_index + 1:]
# Find the index of the comma (,) after the file name
comma_index = file_name_with_extension.find('"')
# Use string slicing to extract the substring before the comma
file_name = file_name_with_extension[:comma_index]

print(file_name)
#print(content_inside_quotes)
print(key)
print(loc)
