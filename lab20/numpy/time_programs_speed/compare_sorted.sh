run_command(){
	cmd=$1
	echo "Running $cmd"

	cmd_name=$(echo $cmd | grep -Po '\w+\.\w{1,3}')

	temp_file=$(mktemp)
	eval $cmd &>$temp_file

	result=$(cat "$temp_file")
	rm "$temp_file"

	output=$(echo "$result" | grep -oP 'real\t.*|user\t.*|sys\t.*' | tr '\n' '\t')
	results+=("$cmd_name"$'\t'"$output")
}

display_results(){
    # Display sorted results
    echo -e "\nDisplay sorted results"
    for line in "${sorted[@]}"; do
        # Split the line into fields based on tabs
        IFS=$'\t' read -r -a fields <<< "$line"

        # Extract the first field
        first_field="${fields[0]}"

        # Add padding to the first field
        padded_field="$(printf '%-30s' "$first_field")"

        # Replace the first field with the padded version
        formatted_line="${padded_field}${line#${line%%$'\t'*}}"

        # Print the formatted line
        echo "$formatted_line"
    done

}


results=()
programs_path="./programs"

cd "$programs_path"

for file_name in *.*; do
	echo "file_name: $file_name"

	if [[ "$file_name" == *.js ]]; then
		cmd="time node $file_name"
		run_command "$cmd"
	elif [[ "$file_name" == *.py ]]; then
		cmd="time python3 $file_name"
		run_command "$cmd"
	elif [[ "$file_name" == *.c ]]; then
		# gcc -O3 sum_C_arrays.c -o sum_C_arrays && time ./sum_C_arrays
		name=$(echo $file_name|sed 's/\.c//')
		cmd="gcc -O3 ${file_name} -o ${name} && time ./${name}"
		run_command "$cmd"
	else
		cmd=""
	fi
done


# Sort results by real time in ascending order
IFS=$'\n' sorted=($(sort -t $'\t' -k3.3n <<<"${results[*]}"))
unset IFS

display_results