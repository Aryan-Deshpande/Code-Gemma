from test_functions import mimic_llm_feedback, mimic_llm_inference

step_size = 4

if __name__ == "__main__": 
    # this script mimics the user 'pressing' generate code
        # for now the steps are fixed, future implementation is based on 
    for i in range(step_size):
        generated_code = mimic_llm_inference(input())
        feedback_code = mimic_llm_feedback(input())


    # code is checked for errors
    

