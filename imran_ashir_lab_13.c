// Ashir Imran
// 4/10/2024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 50

// Define the structure for a student
struct Student {
    char name[MAX_NAME_LENGTH];
    int rollNumber;
    int grades[5]; // Assuming 5 subjects
    float totalGrade;
    float averageGrade;
    struct Student* next; // Pointer to the next student in the linked list
};

void addStudent(struct Student** head) {
    struct Student* newStudent = (struct Student*)malloc(sizeof(struct Student));
    if (newStudent == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }

    printf("Enter student name: ");
    scanf("%s", newStudent->name);
    printf("Enter roll number: ");
    scanf("%d", &newStudent->rollNumber);
    printf("Enter grades for 5 subjects:\n");
    newStudent->totalGrade = 0;
    for (int i = 0; i < 5; ++i) {
        printf("Subject %d: ", i + 1);
        scanf("%d", &newStudent->grades[i]);
        newStudent->totalGrade += newStudent->grades[i];
    }
    newStudent->averageGrade = newStudent->totalGrade / 5;

    newStudent->next = *head;
    *head = newStudent;
}

void displayStudents(struct Student* head) {
    printf("-------------------------------------------------------------------------\n");
    printf("Name\t\tRoll Number\tSubject 1\tSubject 2\tSubject 3\tSubject 4\tSubject 5\tTotal\tAverage\n");
    printf("-------------------------------------------------------------------------\n");
    while (head != NULL) {
        printf("%s\t\t%d\t\t", head->name, head->rollNumber);
        for (int i = 0; i < 5; ++i) {
            printf("%d\t\t", head->grades[i]);
        }
        printf("%.2f\t%.2f\n", head->totalGrade, head->averageGrade);
        head = head->next;
    }
    printf("-------------------------------------------------------------------------\n");
}

// Function to calculate class average
float calculateClassAverage(struct Student* head) {
    float classTotal = 0;
    int count = 0;
    while (head != NULL) {
        classTotal += head->averageGrade;
        ++count;
        head = head->next;
    }
    return classTotal / count;
}

// Function to find student with highest and lowest average grades
void findHighestAndLowest(struct Student* head, char* highestName, float* highestGrade, char* lowestName, float* lowestGrade) {
    *highestGrade = 0;
    *lowestGrade = 100;
    while (head != NULL) {
        if (head->averageGrade > *highestGrade) {
            *highestGrade = head->averageGrade;
            strcpy(highestName, head->name);
        }
        if (head->averageGrade < *lowestGrade) {
            *lowestGrade = head->averageGrade;
            strcpy(lowestName, head->name);
        }
        head = head->next;
    }
}

int main() {
    struct Student* head = NULL;
    char choice;

    do {
        addStudent(&head);
        printf("Do you want to add another student? (y/n): ");
        scanf(" %c", &choice);
    } while (choice == 'y' || choice == 'Y');

    displayStudents(head);

    float classAverage = calculateClassAverage(head);
    printf("Class Average: %.2f\n", classAverage);

    char highestName[MAX_NAME_LENGTH], lowestName[MAX_NAME_LENGTH];
    float highestGrade, lowestGrade;
    findHighestAndLowest(head, highestName, &highestGrade, lowestName, &lowestGrade);
    printf("Student with highest average grade: %s (%.2f)\n", highestName, highestGrade);
    printf("Student with lowest average grade: %s (%.2f)\n", lowestName, lowestGrade);

    struct Student* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}