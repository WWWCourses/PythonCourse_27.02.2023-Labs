#include <stdio.h>
#include <stdlib.h>

#define SIZE 90000000

int main() {
    long *arr = malloc(sizeof(long) * SIZE);
    long long sum = 0;

    // Initialize array
    for (int i = 0; i < SIZE; i++) {
        arr[i] = i;
    }

    // Calculate sum
    for (int i = 0; i < SIZE; i++) {
        sum += arr[i];
    }

    printf("%lld\n", sum);

    return 0;
}