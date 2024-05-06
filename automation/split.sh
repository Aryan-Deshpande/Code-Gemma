#!/bin/bash

error_string="Traceback (most recent call last):
  File \"D:\\GitHub\\LLMCodeDebugger\\automation\\test_main.py\", line 1, in <module>
    from test_functions import print_random_tensors
  File \"D:\\GitHub\\LLMCodeDebugger\\automation\\test_functions.py\", line 6
    dimension1 =
                 ^
SyntaxError: invalid syntax"

main_file=$(echo "$traceback" | grep -oP '(?<=File ")[^"]+')
main_line=$(echo "$traceback" | grep -oP '(?<=line )[0-9]+')

func_file=$(echo "$traceback" | grep -oP '(?<=File ")[^"]+' | tail -n1)
func_line=$(echo "$traceback" | grep -oP '(?<=line )[0-9]+' | tail -n1)

# Print the extracted information
echo "Error occurred in:"
echo "Main file: $main_file, line $main_line"
echo "Function file: $func_file, line $func_line"