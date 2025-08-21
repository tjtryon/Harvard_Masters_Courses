#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //init char_scores array
    int letter_score["Z"-"A"];

    //assign values to letter_score array
    letter_score[("A"-"A")] = 1;
    letter_score[("B"-"A")] = 3;
    letter_score["C"-"A"] = 3;
    letter_score["D"-"A"] = 2;
    letter_score["E"-"A"] = 1;
    letter_score["F"-"A"] = 4;
    letter_score["G"-"A"] = 2;
    letter_score["H"-"A"] = 4;
    letter_score["I"-"A"] = 1;
    letter_score["J"-"A"] = 8;
    letter_score["K"-"A"] = 5;
    letter_score["L"-"A"] = 1;
    letter_score["M"-"A"] = 3;
    letter_score["N"-"A"] = 1;
    letter_score["O"-"A"] = 1;
    letter_score["P"-"A"] = 3;
    letter_score["Q"-"A"] = 10;
    letter_score["R"-"A"] = 1;
    letter_score["S"-"A"] = 1;
    letter_score["T"-"A"] = 1;
    letter_score["U"-"A"] = 1;
    letter_score["V"-"A"] = 4;
    letter_score["W"-"A"] = 4;
    letter_score["X"-"A"] = 8;
    letter_score["Y"-"A"] = 4;
    letter_score["Z"-"A"] = 10;

    //prompt user for input for words

    printf("%i", letter_score[1]);


    //calculate scores

    //print results

}
