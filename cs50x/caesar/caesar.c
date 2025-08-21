#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void convert_text(int cipher_code, string plain_text);

int main(int argc, string argv[])
{

    int cipher_code = 0;
    string plain_text = "";
    // string cipher_text = "";

    // Looks for a integer key on the command line
    // If an arguement exists, program continues, and
    // decodes the ceasar key
    if (argc == 2)
    {

        // Convert a ascii integer to decimal value
        if (isdigit(*argv[1]))
        {

            for (int i = 0; i < strlen(argv[1]); i++)
            {
                if (!isdigit(argv[1][i]))
                {
                    // Error for syntax if non-numeric arg
                    printf("Usage: ./caesar key\n");
                    return 1;
                }
            }

            cipher_code = atoi(argv[1]);
        }

        else if (isalpha(*argv[1]))
        {
            // Convert input of a letter integer to a real
            // integer

            cipher_code = toupper(*argv[1]) - 'A';
        }
        else
        {
            // Error for syntax if no argument is specified,
            // Return usage instructions and error code 1
            // Syntax if error
            printf("Usage: ./caesar key\n");
            return 1;
        }

        // Get plain_text from user
        plain_text = get_string("plaintext: ");

        // Calculate & print cipher_text
        convert_text(cipher_code, plain_text);
    }

    else
    {
        // Error for syntax if no argument is specified,
        printf("Usage: ./caesar key\n");
        return 1;
    }

    return 0;
}

void convert_text(int cipher_code, string plain_text)
{

    string cipher_text = "";

    printf("ciphertext: ");

    // printf("plain_text: %s\n", plain_text);
    // printf("cipher_code: %i\n", cipher_code);

    for (int i = 0; i < strlen(plain_text); i++)
    {
        // Coverts upper case letters to cypher_text
        if (isupper(plain_text[i]))
        {
            printf("%c", (char) (((plain_text[i] - 'A') + cipher_code) % 26) + 'A');
        }

        // Coverts lower case letters to cypher_text
        else if (islower(plain_text[i]))
        {
            printf("%c", (char) (((plain_text[i] - 'a') + cipher_code) % 26) + 'a');
        }

        // Leave anything other than alphaetic as plain text
        else
        {
            printf("%c", (char) plain_text[i]);
        }
    }

    printf("\n");
}
