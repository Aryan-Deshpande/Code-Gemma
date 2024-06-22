# GemmaDev: 
![image](https://github.com/Aryan-Deshpande/GemmaDev/assets/72693780/a865d8f0-e436-4153-8bed-52a84c2e58b4)


## Overview
The primary goal of this research is to enhance the capabilities of large language models (LLMs) for specific programming tasks, such as code synthesis and self-debugging. This involves fine-tuning an advanced LLM to achieve high proficiency in generating and debugging code autonomously, incorporating agentic features that enable the model to perform tasks with minimal human intervention
<br>
[camera-ready conference paper link](https://drive.google.com/file/d/1Xdrp0SXQsaosv2EwarC26UG92DhgwuVu/view?usp=sharing)

# Agentic features
**`Autonomous Code Synthesis:`**
Enabled the model to autonomously generate code based on provided specifications, reducing the need for human-written boilerplate code.
Implemented feedback loops where the model could iteratively improve code quality based on test results and predefined criteria.

**`Self-Debugging Capabilities:`**

Designed the model to autonomously identify and fix bugs in the code it generates.
Integrated debugging protocols that allow the model to run diagnostic checks and apply corrections without human intervention.
<br>

![Self Debugging Life Cycle](https://github.com/Aryan-Deshpande/GemmaDev/assets/72693780/2516b6d6-2226-4c26-96f3-b1dba994cc47)

## Large Language Model Fine-Tuning techniques used

- **`Supervised Fine-tuning:`** 
Applied supervised fine-tuning (SFT) using the Hugging Face library.
Leveraged high-performance computing resources, specifically the NVIDIA A100 Tensor Core GPU with 40GB of VRAM, to maximize training efficiency.

- **`Parameter-Efficient Fine-tuning (LoRA/QLoRA):`** 
Employed Parameter Efficient Tuning (PEFT) to adapt the model to specific code-related tasks without extensive computational resources. Implemented quantization using Low-Rank Adaptation/QLow-Rank Adaptation weights. Loaded the model in a 4-bit (4b) version using normal float-4 (NF4) to reduce memory footprint while maintaining performance.

# **Project Setup:**
To use GemmaDev in your projects, follow these simple steps:

```sh
git clone https://github.com/Aryan-Deshpande/GemmaDev
```

```sh
cd automation
# GemmaDev works in a single folder context, make sure to copy these files into the specfic directory you need
sage.sh
t_actual_inference.py
track.py
```

```sh
# For now manually enter the python file to debug in sage.sh, eg:
PYTHON_FILE="x.py" 
# Depending on your os platform run the bash script sage.sh, for windows:
bash sage.sh
```

```
Your Code Should Now Fix Itself :)
```

## Frontend Setup
```sh
git clone https://github.com/Aryan-Deshpande/GemmaDev
```

```sh
npm i
```

```sh
cd vue/project-alpha
npm run dev
```

```
➜  Local:   http://localhost:5173/
```

## Authors

- [@Aryan-Deshpande](https://github.com/Aryan-Deshpande)
- [@Nitesh-Arya](https://github.com/Aryan-Deshpande)



## Acknowledgements
 - [Gemma](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Huggingface](https://github.com/matiassingers/awesome-readme)

