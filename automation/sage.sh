source ~/.bashrc

if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Please install it first."
    sudo apt-get update
    sudo apt-get install jq
fi

if ! command -v dos2unix &> /dev/null; then
    echo "dos2unix is not installed. Please install it first."
    sudo apt-get install dos2unix
fi

TRACK_FILE="track.py"
PYTHON_FILE="cv.py"
SPLITSCRIPT="split.py"

pyth="/mnt/c/Users/deshp/AppData/Local/Programs/Python/Python310/python.exe"

"$pyth" "$PYTHON_FILE" 2>&1 | tee output.log
ERROR_MESSAGES=$(awk '/Traceback|File/,/No errors found/' output.log)
errors=$(echo "$ERROR_MESSAGES" | grep -oP 'File ".+", line \d+.*')

"$pyth" "$SPLITSCRIPT" "$errors" "$ERROR_MESSAGES"

json_file="./stack.json"

# Count the number of keys in the JSON file
num_keys=$(jq 'keys | length' "$json_file")

function inference_function(){
    CURR_FILE="$1"
    CURR_FILE="${CURR_FILE//$'\r'/}"
    PATH_INPUT="$2"
    LOC_INPUT="$3"

    PROG=$(cat "$CURR_FILE")
    
    
    ${pyth} "t_actual_inference.py" "${PROG}" "${PATH_INPUT}" "${LOC_INPUT}" "$1" 2>&1 | tee output.log
    
    "$pyth" "$CURR_FILE" 2>&1 | tee output.log
    ERROR_MESSAGES=$(awk '/Traceback|File/,/No errors found/' output.log)

    if [ -z "$ERROR_MESSAGES" ]; then
        echo "No errors found."
        return 0
    else
        echo "ERROR_MESSAGES"
        return 1
        #source sage.sh
        #push ${ERROR_MESSAGES}
    fi

}

function check_run(){

    exit=1
    track=0

    if [ -z "$ERROR_MESSAGES" ]; then
        echo "in function No errors found."
    else
        echo "in function ERROR_MESSAGES"
    fi

    while [ $track -ne $num_keys ]; do
        echo "in while loop before track file exec"
        "$pyth" "$TRACK_FILE" "$track" 2>&1 | tee output.log
        echo "in while loop after track file exec"
        output=$(awk '' output.log)

        declare -a lines
        while IFS= read -r line; do
            lines+=("$line")
            done < output.log

        echo ${lines[0]}
        echo ${lines[1]}
        echo ${lines[2]}

        CURR_FILE=${lines[0]}
        PATH_INPUT=${lines[1]}
        LOC_INPUT=${lines[2]}

        echo "printing current file"
        echo "$CURR_FILE"

        echo "in while loop, before inference function call"
        inference_function "$CURR_FILE" "$PATH_INPUT" "$LOC_INPUT"
        exit_value=$?
        echo "in while loop, after inference function generated"

        echo "what the hell"
        echo "$exit_value"

        if [ ${exit_value} -eq 1 ]; then
            echo "in the while loop if statement"
            continue
        else
            track=$((track + 1))
        fi

    done
}

if [ -z "$ERROR_MESSAGES" ]; then
    echo "No errors found."
    exit 0
else
    echo "ERROR_MESSAGES"
    check_run
    exit 0
    #source sage.sh
    #push ${ERROR_MESSAGES}

fi



