// Ashir Imran
// 2/28/2024
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

double addition(double left, double right) {
    return left + right;
}

double subtraction(double left, double right) {
    return left - right;
}

double multiplication(double left, double right) {
    return left * right;
}

double division(double left, double right) {
    return left / right;
}

double power(double left, double right) {
    return pow(left, right);
}

int main() {
    char operator[3]; // Increase size to handle two-character operators
    double left, right, result;
    
    printf("Please enter an expression:\n");
    printf(":> ");
    if (scanf("%lf %s %lf", &left, operator, &right) != 3) {
        printf("Error: Invalid expression\n");
        return 1;
    }
    
    if (strcmp(operator, "+") == 0) {
        result = addition(left, right);
    } else if (strcmp(operator, "-") == 0) {
        result = subtraction(left, right);
    } else if (strcmp(operator, "*") == 0) {
        result = multiplication(left, right);
    } else if (strcmp(operator, "/") == 0) {
        result = division(left, right);
    } else if (strcmp(operator, "**") == 0) {
        result = power(left, right);
    } else {
        printf("Error: Invalid Operator (%s)\n", operator);
        return 1;
    }
    
    printf("%.2lf %s %.2lf = %.2lf\n", left, operator, right, result);
    
    return 0;
}
