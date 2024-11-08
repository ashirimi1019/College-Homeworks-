#include <stdio.h>
#include <string.h>

void reverseString(char *str);
void swap(char *left, char *right);

int main() {
    printf("Enter a string: ");
    
    char input[100]; 
    
    fgets(input, sizeof(input), stdin);
    
    input[strcspn(input, "\n")] = '\0';
    
    reverseString(input);
    
    printf("Reversed string: %s\n", input);
    
    return 0;
}

void reverseString(char *str) {
    int length = strlen(str);
    
    char *start = str;
    char *end = str + length - 1;
    
    while (start < end) {
        swap(start, end);
        start++;
        end--;
    }
}

void swap(char *left, char *right) {
    char temp = *left;
    *left = *right;
    *right = temp;
}
