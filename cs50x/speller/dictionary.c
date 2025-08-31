#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Use prime number bigger than word count to avoid colisions
const unsigned int N = 187751;

// Hash table
node *table[N]; // may need to use malloc

// word count
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // While there is still text in the file to read, compare to the dictionary
    for (node *tmp = table[hash(word)]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number using polynomial rolling hash
unsigned int hash(const char *word)
{
    unsigned long hash_number = 541; // prime number
    int hash = 0;

    for (int i = 0; i <= strlen(word); i++)
    {
        hash = (hash_number * hash + toupper(word[i])) % N;
    }
    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open file.\n");
        unload();
        return false;
    }

    // create temp string for word
    char *word = malloc(LENGTH + 1);

    if (word == NULL)
    {
        printf("Could not allocate memory for string.\n");
        unload();
        free(word);
        return false;
    }

    // read words from dictionary and write to hash table
    while (fscanf(source, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Cound not allocate memory for node\n");
            unload();
            free(word);
            return false;
        }
        int location = hash(word);   // run hash to find the bucket in table
        strcpy(n->word, word);       // write word to temp node
        if (table[location] == NULL) // check if node is first
        {
            n->next = NULL;
        }
        else // if not the first, write node to the head
        {
            n->next = table[location]; // reference first node
        }
        table[location] = n; // write node to table
        word_count++;        // count new word
    }
    fclose(source);
    free(word);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i <= N - 1; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next; // Make a temporary node and move to the next cell
            free(table[i]);             // Free the original cell
            table[i] = tmp;             // Reset table to the temp node
        }
    }
    return true;
}
