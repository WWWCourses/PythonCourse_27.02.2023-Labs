commands=(
	"gcc -O3 sum_C_arrays.c -o sum_C_arrays && time ./sum_C_arrays"
	"time node sum_typed_arrays.js"
	"time python sum_numpy_arays.py"
	"time node sum_arrays.js"
	"time python sum_list.py"
)

for cmd in "${commands[@]}"; do
	echo "Running $cmd"
  	eval $cmd
	echo
done


