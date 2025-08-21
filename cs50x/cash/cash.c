#include <cs50.h>
#include <stdio.h>

int get_change_owed(void);
int calculate_num_coins(int cash_owed);

int main(void)
{
    int change_owed = get_change_owed();
    int num_coins = calculate_num_coins(change_owed);

    printf("%i\n", num_coins);
}

int get_change_owed(void)
{
    int change_owed;

    // ask the user for the amount of change owed
    // only accept a positive integer
    do
    {
        change_owed = get_int("Change owed: ");
    }
    while (change_owed < 0);

    return change_owed;
}

int calculate_num_coins(int cash_owed)
{

    // calculate the number of quarters in cash_owed
    int quarters = cash_owed / 25;
    // remove the quarters in cash_owed
    cash_owed -= (quarters * 25);

    // calculate the number of dimes left in cash_owed
    int dimes = cash_owed / 10;
    // remove the dimes in cash_owed
    cash_owed -= (dimes * 10);

    // calculate the number of nickles left in cash_owed
    int nickles = cash_owed / 5;
    // remove the nickles in cash_owed
    cash_owed -= (nickles * 5);

    // calculate the number of pennies left in cash_owed
    int pennies = cash_owed / 1;
    // remove the pennies in cash_owed
    cash_owed -= (pennies * 1);

    // add the coins
    int num_coins = quarters + dimes + nickles + pennies;

    return num_coins;
}
