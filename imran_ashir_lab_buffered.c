// buffered_io.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ITERATIONS 1000000
#define MESSAGE "Hello, World!\n"
#define FILENAME "buffered.txt"

int main() {
    FILE *fp;
    int i;
    time_t start, end;

    // Record start time
    start = time(NULL);

    // Open file
    fp = fopen(FILENAME, "w");
    if (fp == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    // Write to file ITERATIONS times
    for (i = 0; i < ITERATIONS; i++) {
        if (fprintf(fp, "%s", MESSAGE) < 0) {
            perror("fprintf");
            fclose(fp);
            exit(EXIT_FAILURE);
        }
        printf("%d: %ld characters written to %s\n", i, sizeof(MESSAGE) - 1, FILENAME);
    }

    // Close file
    fclose(fp);

    // Record end time
    end = time(NULL);

    // Output time elapsed
    printf("Buffered IO Time Elapsed: %ld seconds\n", end - start);

    return 0;
}

