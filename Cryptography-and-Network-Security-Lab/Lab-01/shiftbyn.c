#include <stdio.h>

int main() {
    char text[1000];
    int key, choice;

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter the key: ");
    scanf("%d", &key);

    printf("\n1. Encryption\n");
    printf("2. Decryption\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    key = key % 26;

    for (int i = 0; text[i] != '\0'; i++) {

        if (text[i] >= 'A' && text[i] <= 'Z') {
            if (choice == 1)
                text[i] = (text[i] - 'A' + key) % 26 + 'A';
            else if (choice == 2)
                text[i] = (text[i] - 'A' - key + 26) % 26 + 'A';
        }

        else if (text[i] >= 'a' && text[i] <= 'z') {
            if (choice == 1)
                text[i] = (text[i] - 'a' + key) % 26 + 'a';
            else if (choice == 2)
                text[i] = (text[i] - 'a' - key + 26) % 26 + 'a';
        }
    }

    if (choice == 1)
        printf("\nEncrypted text: %s", text);
    else if (choice == 2)
        printf("\nDecrypted text: %s", text);
    else
        printf("\nInvalid choice!");

    return 0;
}