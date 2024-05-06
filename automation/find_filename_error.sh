source ~/.bashrc

PYTHON_FILE="test_main.py"
SPLITSCRIPT="split.py"

pyth="/mnt/c/Users/deshp/AppData/Local/Programs/Python/Python310/python.exe"

#${pyth} ${PYTHON_FILE} 2>&1 | tee output.log

#ERROR_MESSAGES=$(awk '/Traceback|File/,/No errors found/' output.log)

#errors=$(echo "$ERROR_MESSAGES" | grep -oP 'File ".+", line \d+.*')

#if [ -z "$ERROR_MESSAGES" ]; then
#    echo "No errors found."
#else
#    echo "ERROR_MESSAGES"
    #source sage.sh
    #push ${ERROR_MESSAGES}

#fi

# Print the extracted information
#
#echo "Errors:"
#echo "$errors"
#echo "$ERROR_MESSAGES"
#echo "something"

#${pyth} ${SPLITSCRIPT} "$errors" "$ERROR_MESSAGES"

${pyth} ${PYTHON_FILE} 2>&1 | tee output.log
ERROR_MESSAGES=$(awk '/Traceback|File/,/No errors found/' output.log)
errors=$(echo "$ERROR_MESSAGES" | grep -oP 'File ".+", line \d+.*')

${pyth} ${SPLITSCRIPT} "$errors" "$ERROR_MESSAGES"

json_file="./stack.json"





#echo ${CURR_FILE} 
#echo ${PATH_INPUT} 
#echo ${LOC_INPUT}

function inference_function(){
    CURR_FILE="$1"
    PATH_INPUT="$2"
    LOC_INPUT="$3"

    cat "test_st.py" 2>&1 | tee output.log
    PROG= $(awk '' output.log)
    
    #echo "printing code"
    #echo "$PROG"

    echo "in ineference function"
    echo "$CURR_FILE"

    echo "$pyth"
    
    ${pyth} "t_actual_inference.py" ${PROG} ${PATH_INPUT} ${LOC_INPUT} ${CURR_FILE} 2>&1 | tee output.log
}

#inference_function "$CURR_FILE" "$PATH_INPUT" "$LOC_INPUT"
#exit_value=$?
#echo "$exit_value"

#if [ ${exit_value} -eq 1 ]; then
#    echo "err repeat"
#    continue
#else
#    track=$((track + 1))
#fi


#echo "$track"
