#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string, int);
int count_words(string, int);
int count_sentences(string, int);

int main(void)
{
    // Get the text string
    string text = get_string("Text: ");

    // What is the string length
    int text_length = strlen(text);

    // Get the number of alpha letters in the string
    int letter_count = count_letters(text, text_length);

    // Get the number of words in the string
    int word_count = count_words(text, text_length);

    // Get the number of sentences in the string
    int sentence_count = count_sentences(text, text_length);

    // Calc coleman-liau index
    int grade_index = round(5.88 * ((float) letter_count / (float) word_count) -
                            29.6 * ((float) sentence_count / (float) word_count) - 15.8);

    // Print the grade index
    if (grade_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_index);
    }
}

int count_letters(string text, int text_length)
{
    // Count letters
    int letters = 0;
    for (int i = 0; i <= text_length; i++)
    {
        // If the txt is between a-z (97 - 122) or A-Z (65 - 90), increase letter count.
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text, int text_length)
{
    // Count words
    int words = 1;
    for (int i = 0; i <= text_length; i++)
    {
        // If there is a space (ascii 32), then increase word count.
        if (isblank(text[i]))
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text, int text_length)
{
    int sentences = 0;
    for (int i = 0; i < text_length; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}
