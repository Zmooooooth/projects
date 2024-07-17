// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int loaded_words = 0;
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 675;
unsigned int hash_value = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    hash_value = hash(word);
    node *runner = table[hash_value];
    while (runner != NULL)
    {
        char hword[LENGTH + 1];
        char sword[LENGTH + 1];
        strcpy(hword, runner->word);
        strcpy(sword, word);
        int i = 0;
        while (hword[i] != '\0')
        {
            hword[i] = tolower(hword[i]);
            i++;
        }
        i = 0;
        while (sword[i] != '\0')
        {
            sword[i] = tolower(sword[i]);
            i++;
        }
        if (strcmp(hword, sword) == 0)
        {
            return true;
        }
        runner = runner->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int first = toupper(word[0]) - 'A';
    int second = toupper(word[1]) - 'A';
    unsigned int result = (first * 26) + second;
    if (result > N)
    {
        result = result % N;
    }
    return result;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *sourcefile = fopen(dictionary, "r");
    if (sourcefile == NULL)
    {
        return false;
    }
    char buffer[LENGTH + 1];
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    while (fscanf(sourcefile, "%s", buffer) != EOF)
    {
        node *item = malloc(sizeof(node));
        if (item == NULL)
        {
            return false;
        }
        strcpy(item->word, buffer);
        hash_value = hash(item->word);
        item->next = table[hash_value]; // Here is the segmentation fault
        table[hash_value] = item;
        loaded_words++;
    }
    fclose(sourcefile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return loaded_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *cursor;
    node *tmp;
    for (int i = 0; i < N; i++)
    {
        cursor = table[i];
        tmp = cursor;
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
