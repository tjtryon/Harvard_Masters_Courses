#include <cs50.h>
#include <stdio.h>

string get_name(void);

int main(void)
{
    string name = get_name();

    printf("hello, %s\n", name);
}

string get_name(void)
{
    string name;

    // ask the user for their name
    do
    {
        name = get_string("What's your name? ");
    }
    while (name == NULL);

    return name;
}
