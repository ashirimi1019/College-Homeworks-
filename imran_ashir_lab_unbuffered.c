// unbuffered_io.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>

#define ITERATIONS 1000000
#define MESSAGE "Hello, World!\n"
#define FILENAME "output.txt"

int main() {
    int fd, i;
    time_t start, end;

    // Record start time
    start = time(NULL);

    // Open file
    fd = open(FILENAME, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Write to file ITERATIONS times
    for (i = 0; i < ITERATIONS; i++) {
        if (write(fd, MESSAGE, sizeof(MESSAGE) - 1) == -1) {
            perror("write");
            close(fd);
            exit(EXIT_FAILURE);
        }
        printf("%d: Called write(%d, %s, %ld) which returned that %ld bytes were written.\n",
               i, fd, MESSAGE, sizeof(MESSAGE) - 1, sizeof(MESSAGE) - 1);
    }

    // Close file
    close(fd);

    // Record end time
    end = time(NULL);

    // Output time elapsed
    printf("Unbuffered IO Time Elapsed: %ld seconds\n", end - start);

    return 0;
}

