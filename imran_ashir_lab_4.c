#include <stdio.h>
#include <math.h>

int main() {
    // Declare variables
    double mass, height, time, velocity, kinetic_energy;

    // Prompt user for input
    printf("Enter the mass of the object in kilograms: ");
    scanf("%lf", &mass);

    printf("Enter the height of the drop in meters: ");
    scanf("%lf", &height);

    // Calculate time taken to reach the ground
    time = sqrt(2 * height / 9.8);

    // Calculate velocity at impact
    velocity = 9.8 * time;

    // Calculate kinetic energy at impact
    kinetic_energy = 0.5 * mass * velocity * velocity;

    // Display the results
    printf("\nThe time taken by an object weighing %.2f kg to reach the ground when dropped from a height of %.2f meters is %.2f seconds.\n", mass, height, time);
    printf("The velocity of the object when it hits the ground = %.2f m/s.\n", velocity);
    printf("The kinetic energy at the moment of impact with the ground is %.2f Joules.\n", kinetic_energy);

    return 0;
}
