import ollama
import math
import sys

print("in python inference function")

code = sys.argv[1]
fileloc = sys.argv[2]
errorloc = sys.argv[3]
file = sys.argv[4]
file = file.strip()

print(code)
print(fileloc)
print(errorloc)
print(file)

response = ollama.chat(model='llama3', messages = [
    {
        'role': 'user',
        'content': f"""can you fix my code for this program withought changing the logic, generate the new fixed code within ``` ```, do not add ``` python or Python ``` just plain code, code "{code}", error "{fileloc}, {errorloc}" """,

    }
], options={"num_ctx": 27000,})

a = response['message']['content']

b = a.split("```")

c = (len(b)-1)/2
c = math.ceil(c)

print(a)


with open(f'./{file}', 'w') as f:
    f.write(b[c])

print("response generated")