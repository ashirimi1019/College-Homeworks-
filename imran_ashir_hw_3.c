#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 50
#define MAX_DESCRIPTION_LENGTH 100

// Structure to represent product dimensions
struct Dimensions {
    int length;
    int width;
    int height;
};

// Union to represent either dimensions or description of a product
union ProductDetails {
    struct Dimensions dimensions;
    char description[MAX_DESCRIPTION_LENGTH];
};

// Structure to represent a product
struct Product {
    char name[MAX_NAME_LENGTH];
    int quantity;
    float price;
    union ProductDetails details;
    struct Product *next;
};

// Function prototypes
void addProduct(struct Product **inventory);
void displayProducts(struct Product *inventory);
void updateProductQuantity(struct Product *inventory);
void updateProductPrice(struct Product *inventory);
void deleteProduct(struct Product **inventory);
void freeInventory(struct Product *inventory);

int main() {
    struct Product *inventory = NULL;
    int choice;

    do {
        printf("\nInventory Management System\n");
        printf("1. Add Product\n");
        printf("2. Display Products\n");
        printf("3. Update Product Quantity\n");
        printf("4. Update Product Price\n");
        printf("5. Delete Product\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addProduct(&inventory);
                break;
            case 2:
                displayProducts(inventory);
                break;
            case 3:
                updateProductQuantity(inventory);
                break;
            case 4:
                updateProductPrice(inventory);
                break;
            case 5:
                deleteProduct(&inventory);
                break;
            case 6:
                freeInventory(inventory);
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 6);

    return 0;
}

void addProduct(struct Product **inventory) {
    struct Product *newProduct = (struct Product *)malloc(sizeof(struct Product));
    if (newProduct == NULL) {
        printf("Memory allocation failed. Product cannot be added.\n");
        return;
    }

    printf("Enter product name: ");
    scanf(" %[^\n]s", newProduct->name);
    printf("Enter quantity: ");
    scanf("%d", &newProduct->quantity);
    printf("Enter price: ");
    scanf("%f", &newProduct->price);

    printf("Does this product have dimensions (0 - No, 1 - Yes): ");
    int hasDimensions;
    scanf("%d", &hasDimensions);
    if (hasDimensions) {
        printf("Enter length, width, and height: ");
        scanf("%d %d %d", &newProduct->details.dimensions.length, &newProduct->details.dimensions.width, &newProduct->details.dimensions.height);
    } else {
        printf("Enter product description: ");
        scanf(" %[^\n]s", newProduct->details.description);
    }

    newProduct->next = *inventory;
    *inventory = newProduct;

    printf("Product added successfully!\n");
}

void displayProducts(struct Product *inventory) {
    printf("\nName\tQuantity\tPrice\tDetails\n");
    while (inventory != NULL) {
        printf("%s\t%d\t\t%.2f\t", inventory->name, inventory->quantity, inventory->price);
        if (strlen(inventory->details.description) > 0) {
            printf("%s\n", inventory->details.description);
        } else {
            printf("%dx%dx%d\n", inventory->details.dimensions.length, inventory->details.dimensions.width, inventory->details.dimensions.height);
        }
        inventory = inventory->next;
    }
}

void updateProductQuantity(struct Product *inventory) {
    char productName[MAX_NAME_LENGTH];
    printf("Enter product name to update quantity: ");
    scanf(" %[^\n]s", productName);

    while (inventory != NULL) {
        if (strcmp(inventory->name, productName) == 0) {
            printf("Enter new quantity: ");
            scanf("%d", &inventory->quantity);
            printf("Product quantity updated successfully!\n");
            return;
        }
        inventory = inventory->next;
    }

    printf("Product not found.\n");
}

void updateProductPrice(struct Product *inventory) {
    char productName[MAX_NAME_LENGTH];
    printf("Enter product name to update price: ");
    scanf(" %[^\n]s", productName);

    while (inventory != NULL) {
        if (strcmp(inventory->name, productName) == 0) {
            printf("Enter new price: ");
            scanf("%f", &inventory->price);
            printf("Product price updated successfully!\n");
            return;
        }
        inventory = inventory->next;
    }

    printf("Product not found.\n");
}

void deleteProduct(struct Product **inventory) {
    char productName[MAX_NAME_LENGTH];
    printf("Enter product name to delete: ");
    scanf(" %[^\n]s", productName);

    struct Product *current = *inventory;
    struct Product *prev = NULL;

    while (current != NULL) {
        if (strcmp(current->name, productName) == 0) {
            if (prev == NULL) {
                *inventory = current->next;
            } else {
                prev->next = current->next;
            }
            free(current);
            printf("Product deleted successfully!\n");
            return;
        }
        prev = current;
        current = current->next;
    }

    printf("Product not found.\n");
}

void freeInventory(struct Product *inventory) {
    struct Product *temp;
    while (inventory != NULL) {
        temp = inventory;
        inventory = inventory->next;
        free(temp);
    }
}
