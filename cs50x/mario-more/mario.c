#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_towers(int height);

int main(void)
{
    int height = get_height();
    print_towers(height);
}

int get_height(void)
{
    int height;

    do
    {
        height = get_int("How high do you want to make Mario's obstacle? Valid input is [1-8]? ");
    }
    while (height < 1 || height > 8);

    return height;
}

void print_towers(int height)
{
    // total possible width of the pattern is 2 times the
    // height plus two empty spaces between the towers
    int max_width = (2 * height - 2);

    for (int row_width = 0; row_width < height; row_width++)
    {
        // startspace is calculated by the max width, minus the 2 center spaces
        // and 2 times the height.

        for (int startspace = ((max_width - (2 * row_width - 2)) / 2); startspace > 1; startspace--)
        {
            // printf("%i", startspace);
            printf(" "); // Print the empty spaces before the blocks
        }

        for (int count = 0; count <= row_width; count++)
        {
            printf("#"); // Print the first set of blocks (number is same as height)
        }

        printf("  "); //  Print the two empty spaces in the middle

        for (int count = 0; count <= row_width; count++)
        {
            printf("#"); // Print the last set of blocks (number is same as height)
        }

        printf("\n"); // Print a newline to start the next row
    }
}
