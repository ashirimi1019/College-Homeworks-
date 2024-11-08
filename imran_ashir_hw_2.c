#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRIES 8
#define DIGITS 3
#define RANGE 10

void generateSecretCode(int *secretCode) {
    srand(time(NULL));
    for (int i = 0; i < DIGITS; i++) {
        secretCode[i] = rand() % RANGE;
    }
}

void printFeedback(int correctDigits, int correctPosition, int correctWrongPosition) {
    printf("%d digits are correct and in the right place, %d digits are correct but not in the right place.\n", correctPosition, correctWrongPosition);
}

int main() {
    int secretCode[DIGITS];
    int guess[DIGITS];
    int tries = TRIES;
    int correctDigits, correctPosition, correctWrongPosition;

    generateSecretCode(secretCode);

    printf("%d tries remaining. What is the code? ", tries);
    while (tries > 0) {
        for (int i = 0; i < DIGITS; i++) {
            if (scanf("%1d", &guess[i]) != 1) {
                printf("Invalid input.\n");
                return 1;
            }
        }
        getchar(); // Consume newline character

        correctDigits = 0;
        correctPosition = 0;
        correctWrongPosition = 0;

        for (int i = 0; i < DIGITS; i++) {
            if (guess[i] == secretCode[i]) {
                correctPosition++;
            } else {
                for (int j = 0; j < DIGITS; j++) {
                    if (guess[i] == secretCode[j]) {
                        correctDigits++;
                        break;
                    }
                }
            }
        }

        correctWrongPosition = correctDigits - correctPosition;

        if (correctPosition == DIGITS) {
            printf("You opened the vault!\n");
            return 0;
        } else {
            printf("%d tries remaining. ", --tries);
            if (tries == 0) {
                printf("The vault shuts down permanently due to too many incorrect attempts. You failed to open the vault!\n");
                printf("The secret code was %d%d%d\n", secretCode[0], secretCode[1], secretCode[2]);
                return 0;
            }
            if (correctPosition == 0 && correctWrongPosition == 0) {
                printf("Too low, ");
            } else if (correctPosition == 0) {
                printf("Too low, ");
            } else if (correctPosition == DIGITS) {
                printf("You opened the vault!\n");
                return 0;
            } else {
                printf("Too low, ");
            }
            printFeedback(correctDigits, correctPosition, correctWrongPosition);
            printf("What is the code? ");
        }
    }

    return 0;
}

