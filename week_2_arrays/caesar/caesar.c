#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    bool only_digits(string s);
    char rotate(char c, int key);

    if(argc == 2 && only_digits(argv[1]) == 0)
    {
    int key = atoi(argv[1]);
    printf("%d\n", key);
    string plaintext = get_string("plaintext: ");
    printf("\nCiphertext: ");
    for(int i = 0, l = strlen(plaintext); i < l; i++)
    {
        char secret = rotate(plaintext[i], key);
        printf("%c", secret);
    }
    printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool only_digits(string s)
{
    for(int i = 0, l = strlen(s); i < l; i++)
    {
        if(isdigit(s[i]) == false)
        {
            return 1;
        }
    }
    return 0;
}

char rotate(char c, int key)
{
    if(c > 64 && c < 91)
    {
        c = ((c - 65 + key) %26) + 65;
        return c;
    }
    else if(c > 96 && c < 123)
    {
        c = ((c - 97 + key) %26) + 97;
        return c;
    }
    else{
        return c;
    }
}

