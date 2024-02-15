#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get change owed value
    int change;
    int answer = 0;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 1);

    // divide change owed by 25(quarter) | 10(dime) | 5(nickel) | 1(penny)
    int quarter = change / 25;
    answer += quarter;
    change -= quarter * 25;
    int dime = change / 10;
    answer += dime;
    change -= dime * 10;
    int nickel = change / 5;
    answer += nickel;
    change -= nickel * 5;
    int penny = change / 1;
    answer += penny;
    printf("%d\n", answer);
}