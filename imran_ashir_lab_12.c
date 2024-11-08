#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 50
#define MAX_SUBJECT_NAME 20
#define NUM_SUBJECTS 5

// Structure to store student data
struct Student {
    char name[50];
    int rollNo;
    float marks[NUM_SUBJECTS];
    float totalMarks;
    float averageMarks;
};

int main() {
    struct Student classRoster[MAX_STUDENTS];
    char subjectNames[NUM_SUBJECTS][MAX_SUBJECT_NAME];
    int numStudents, i, j;
    float classTotalMarks = 0;
    float classAverageMarks;
    int highestIndex = 0, lowestIndex = 0;

    // Prompt user to enter the total number of students
    printf("Enter the total number of students in the class (max 50): ");
    scanf("%d", &numStudents);

    // Validate the number of students
    if (numStudents < 1 || numStudents > MAX_STUDENTS) {
        printf("Invalid number of students. Please enter a number between 1 and 50.\n");
        return 1;
    }

    // Input subject names
    printf("\nEnter the names of %d subjects:\n", NUM_SUBJECTS);
    for (i = 0; i < NUM_SUBJECTS; i++) {
        printf("Subject %d: ", i + 1);
        scanf("%s", subjectNames[i]);
    }

    // Input student data
    for (i = 0; i < numStudents; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Name: ");
        scanf("%s", classRoster[i].name);
        printf("Roll number: ");
        scanf("%d", &classRoster[i].rollNo);

        printf("Enter grades for the subjects:\n");
        for (j = 0; j < NUM_SUBJECTS; j++) {
            printf("%s: ", subjectNames[j]);
            scanf("%f", &classRoster[i].marks[j]);
            // Validate grades
            if (classRoster[i].marks[j] < 0 || classRoster[i].marks[j] > 100) {
                printf("Invalid grade! Please enter a grade between 0 and 100.\n");
                j--; // Repeat for the same subject
            }
            else {
                classRoster[i].totalMarks += classRoster[i].marks[j];
            }
        }
        // Calculate average marks for the student
        classRoster[i].averageMarks = classRoster[i].totalMarks / NUM_SUBJECTS;
        classTotalMarks += classRoster[i].averageMarks;

        // Find the student with the highest average grade
        if (classRoster[i].averageMarks > classRoster[highestIndex].averageMarks)
            highestIndex = i;
        // Find the student with the lowest average grade
        if (classRoster[i].averageMarks < classRoster[lowestIndex].averageMarks)
            lowestIndex = i;
    }

    // Calculate class average
    classAverageMarks = classTotalMarks / numStudents;

    // Output and statistics
    printf("\nClass Roster and Statistics:\n");
    printf("--------------------------------------------------------------\n");
    printf("Name\t\tRoll No.\t");
    for (i = 0; i < NUM_SUBJECTS; i++) {
        printf("%s\t", subjectNames[i]);
    }
    printf("Total Marks\tAverage Marks\n");
    printf("--------------------------------------------------------------\n");
    for (i = 0; i < numStudents; i++) {
        printf("%-15s\t%-10d\t", classRoster[i].name, classRoster[i].rollNo);
        for (j = 0; j < NUM_SUBJECTS; j++) {
            printf("%.2f\t\t", classRoster[i].marks[j]);
        }
        printf("%.2f\t\t%.2f\n", classRoster[i].totalMarks, classRoster[i].averageMarks);
    }
    printf("--------------------------------------------------------------\n");
    printf("Class Average: %.2f\n", classAverageMarks);
    printf("Student with Highest Average: %s (Roll No. %d)\n", classRoster[highestIndex].name, classRoster[highestIndex].rollNo);
    printf("Student with Lowest Average: %s (Roll No. %d)\n", classRoster[lowestIndex].name, classRoster[lowestIndex].rollNo);

    return 0;
}
