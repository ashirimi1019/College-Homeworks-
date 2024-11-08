// NAME: Ashir Imran
// LAB: 7
#include <stdio.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

int main() {
    FILE *file;
    int frequencies[ALPHABET_SIZE] = {0}; // Array to store frequencies of each alphabet character
    char c;

    // Open the file
    file = fopen("sample.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Read characters from the file and update frequencies
    while ((c = fgetc(file)) != EOF) {
        if (isalpha(c)) {
            c = tolower(c); // Convert character to lowercase
            frequencies[c - 'a']++; // Increment frequency count for the character
        }
    }

    // Find the most frequent character
    int maxFrequency = 0;
    char mostFrequentChar;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (frequencies[i] > maxFrequency) {
            maxFrequency = frequencies[i];
            mostFrequentChar = 'a' + i;
        }
    }

    // Output the most frequent character and its frequency
    printf("Most frequent character: %c\n", mostFrequentChar);
    printf("Frequency: %d\n", maxFrequency);

    // Close the file
    fclose(file);

    return 0;
}
