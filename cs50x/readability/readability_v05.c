#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string lit_text);

const int max_num_words = 100;

int main (void)
{
    int num_words = 0;
    int num_sentences = 0;
    int num_letters = 0;

    float readability_index = 0;

    // Get text string

    string literature_string = get_string("Text: ");

    // Get length of the string

    int strlen_text = strlen(literature_string);

    printf("strlen_text = %i\n", strlen_text);

    // get the number of letters in the string
    for (int i = 0, n = strlen_text; i < strlen_text; i++)
    {
        if (isalpha(literature_string[i]))
        {
            num_letters++;
        }
    }

    printf("num_letters = %i\n", num_letters);

    // Get the number of words in the string

    for (int i = 0; i <= strlen_text; i++)
    {
        if (literature_string[i] == ' ' || literature_string[i] == '\0')
        {
            num_words++;
        }
    }

    printf("num_words = %i\n", num_words);

    // Find the num_sentences in the string

    for (int i = 0; i < strlen_text; i++)
    {
        if (literature_string[i] == '.' || literature_string[i] == '!' ||
            literature_string[i] == '?' || literature_string[i] == ';')
        {
            num_sentences++;
        }
    }

    printf("num_sentences = %i\n", num_sentences);

    float L = round(max_num_words * (num_letters / num_words));
    float S = round(max_num_words * (num_sentences / num_words));

    // Find the average number of words in the sentences

    //float average_words_sentences = (float) num_words / (float) num_sentences;

    //    printf("average_words_sentences = %f\n", average_words_sentences);

    // float num_sentences_hundred_words = 100 / average_words_sentences;

    // printf("num_sentences_hundred_words = %f\n", num_sentences_hundred_words);

    // Find the average length of the words

    // float average_len_words = (float) num_letters / (float) num_words;

    // float letters_hundred_words  = average_len_words * 100;

    // printf("letters_hundred_words %3f\n", letters_hundred_words);

    // Calculate readability index

    readability_index = round(0.0588 * L - 0.296 * S - 15.8);

    // Print readability index

    if (readability_index < 1)
    {
        printf("Grade < 1\n");
    }
    else if (readability_index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) readability_index);
    }

    printf("Readability index = %f\n", readability_index);

    return 0;

}

