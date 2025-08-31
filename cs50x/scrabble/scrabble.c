#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int char_points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                       1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);
void print_winner(int score1, int score2);

int main(void)
{
    // Get the player's words to compare
    string player1_word = get_string("Player 1: ");
    string player2_word = get_string("Player 2: ");

    // Score both words
    int player1_score = compute_score(player1_word);
    int player2_score = compute_score(player2_word);

    print_winner(player1_score, player2_score);
}

int compute_score(string word)
{

    int n = strlen(word);
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        // convert characters in word to capital
        word[i] = toupper(word[i]);

        // get the ascii index of the letter
        int letter_index = word[i] - 65;

        // if chars are letters, add the points
        if (word[i] >= 65 && word[i] <= 90)
        {

            int points = char_points[letter_index];
            sum += points;
        }
        else
        {
            // ignore non-char input
            sum += 0;
        }
    }
    return sum;
}

void print_winner(int player1_score, int player2_score)
{
    // print the winners
    if (player1_score > player2_score)
    {
        printf("Player 1 wins! \n");
    }
    else if (player1_score < player2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
