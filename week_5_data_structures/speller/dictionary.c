// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 5000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int l = strlen(word);
    char lowerWord[l + 1];
    strcpy(lowerWord, word);
    lowerWord[l] = '\0';
    for (int i = 0; i < l; i++)
    {
        lowerWord[i] = tolower(lowerWord[i]);
    }
    int index = hash(lowerWord);
    if (table[index] != NULL)
    {
        node *cursor = table[index];
        while (cursor != NULL)
        {
            if (strcasecmp(lowerWord, cursor->word) == 0)
            {
                return true;
            }
            cursor = cursor->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int index = 0;
    int factor = 1000;
    for (int i = 0, l = strlen(word); i < l; i++)
    {

        int num = (word[i] - 97);
        if (num < 0 || num > 25)
        {
            num = 1;
        }
        index += num * factor;
        factor /= 10;
        if (factor <= 1)
        {
            break;
        }
    }
    return index % N;
}

// Loads dictionary into memory, returning true if successful, else false
int wordCount = 0;

bool load(const char *dictionary)
{
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(source, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("insufficient memory\n");
            return false;
        }
        strcpy(new_node->word, word);
        for (int i = 0, l = strlen(word); i < l; i++)
        {
            new_node->word[i] = tolower(new_node->word[i]);
        }
        int index = hash(new_node->word);
        new_node->next = table[index];
        table[index] = new_node;
        wordCount++;
    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return wordCount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            node *tmp = table[i];
            node *cursor = table[i];
            while (cursor != NULL)
            {
                cursor = cursor->next;
                free(tmp);
                tmp = cursor;
            }
        }
    }
    return true;
}
