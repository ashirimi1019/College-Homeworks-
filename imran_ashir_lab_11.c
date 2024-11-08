#include <stdio.h>

void bubbleSort(int *arr, int n) {
    int *ptr1, *ptr2;
    int temp;
    int i, j;
    
    for (i = 0; i < n - 1; i++) {
        ptr1 = arr;
        ptr2 = arr + 1;
        for (j = 0; j < n - i - 1; j++) {
            if (*ptr1 > *ptr2) {
                temp = *ptr1;
                *ptr1 = *ptr2;
                *ptr2 = temp;
            }
            ptr1++;
            ptr2++;
        }
    }
}

int main() {
    int arr[10];
    int i;

    printf("Please Enter 10 Numbers:\n");
    for (i = 0; i < 10; i++) {
        printf("Please Enter Number %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    bubbleSort(arr, 10);

    printf("Sorted Array: [");
    for (i = 0; i < 10; i++) {
        printf("%d", arr[i]);
        if (i != 9)
            printf(", ");
    }
    printf("]\n");

    printf("Largest: %d\n", arr[9]);
    printf("Smallest: %d\n", arr[0]);

    return 0;
}
