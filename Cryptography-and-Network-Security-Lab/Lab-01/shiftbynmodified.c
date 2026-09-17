#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 31

char dictionary[SIZE][20] = {
    "hello", "world", "this", "is", "a",
    "test", "the", "cat", "dog", "computer",
    "science", "engineering", "student", "good",
    "morning", "welcome", "secret","cab", "message",
    "cryptography", "cipher", "program", "code",
    "college", "india", "love", "you", "are",
    "very", "smart", "great"
};

int isMeaningful(char word[]) {
    for (int i = 0; i < SIZE; i++) {
        if (strcmp(word, dictionary[i]) == 0)
            return 1;
    }
    return 0;
}

void decrypt(char text[], char result[], int key) {
    for (int i = 0; text[i] != '\0'; i++) {

        if (text[i] >= 'A' && text[i] <= 'Z')
            result[i] = (text[i] - 'A' - key + 26) % 26 + 'A';

        else if (text[i] >= 'a' && text[i] <= 'z')
            result[i] = (text[i] - 'a' - key + 26) % 26 + 'a';

        else
            result[i] = text[i];
    }

    result[strlen(text)] = '\0';
}

int main() {
    char text[1000];
    char decrypted[1000];
    char temp[1000];

    printf("Enter encrypted text: ");
    fgets(text, sizeof(text), stdin);

    for (int key = 1; key <= 25; key++) {

        int count = 0;

        decrypt(text, decrypted, key);

        strcpy(temp, decrypted);

        char *word = strtok(temp, " ,.!?\n");

        while (word != NULL) {

            // Convert word to lowercase
            for (int i = 0; word[i] != '\0'; i++)
                word[i] = tolower(word[i]);

            if (isMeaningful(word))
                count++;

            word = strtok(NULL, " ,.!?\n");
        }

        printf("Key %d: %s", key, decrypted);

        if (count > 0) {
            printf("  --> Meaningful words found: %d", count);
            printf("  <-- POSSIBLE ANSWER");
        }

        printf("\n");
    }

    return 0;
}