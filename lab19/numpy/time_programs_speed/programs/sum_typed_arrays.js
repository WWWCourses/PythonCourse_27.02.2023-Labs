const SIZE = 90000000;
const arr = new Int32Array(SIZE);
let sum = 0;

// Initialize array
for (let i = 0; i < SIZE; i++) {
  arr[i] = i;
}

// Calculate sum
for (let i = 0; i < SIZE; i++) {
  sum += arr[i];
}

console.log(sum);
