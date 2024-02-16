#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

//index = 0.0588 * L - 0.296 * S - 15.8

int main(void)
{
    float L = 0.0;
    int W = 0.0;
    float S = 0.0;

    //prompt user for input
    string userInput = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text

    for(int i = 0, len = strlen(userInput); i < len; i++)
    {
        if(isalpha(userInput[i])){
            L++;
        }
        if(userInput[i] == ' '){
            W++;
        }
        if(userInput[i] == '.' || userInput[i] == '!' || userInput[i] == '?'){
            S++;
        }
    }
    W++;
    L = (L / W) * 100;
    S = (S / W) * 100;
    float grade = 0.0588 * L - 0.296 * S - 15.8;
    int finalGrade = round(grade);

    if(finalGrade <1){
        printf("Before Grade 1\n");
    }
    else if(finalGrade >= 16){
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", finalGrade);
    }
}