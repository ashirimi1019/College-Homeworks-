// Ashir Imran
// 3/6/2024
#include <stdio.h>

void bubble_sorting(int array[], int n, int *min, int *max) {
    int i, j, temp;
    
    // Bubble sort algorithm
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (array[j] > array[j+1]) {
                // Swap if elements are not in order
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    
    // Assign min and max values
    *min = array[0];
    *max = array[n-1];
}

int main() {
    int array[10];
    int i, min, max;
    
    // Prompt user to enter 10 integers
    printf("Please Enter 10 Integers:\n");
    for (i = 0; i < 10; i++) {
        printf("Enter Number %d: ", i+1);
        scanf("%d", &array[i]);
    }
    
    // Sort the array and find min and max
    bubble_sorting(array, 10, &min, &max);
    
    // Output the sorted list
    printf("\nSorted List:\n[");
    for (i = 0; i < 10; i++) {
        printf("%d", array[i]);
        if (i < 9) printf(", ");
    }
    printf("]\n");
    
    // Output min and max
    printf("Largest: %d\n", max);
    printf("Smallest: %d\n", min);
    
    return 0;
}

