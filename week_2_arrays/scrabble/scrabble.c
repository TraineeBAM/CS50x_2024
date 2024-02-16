#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    int p1score = 0;
    int p2score = 0;

    for(int i = 0, l = strlen(player1); i < l; i++){
        player1[i] = toupper(player1[i]);
        if(player1[i] == 'A' || player1[i] == 'E' || player1[i] =='I' || player1[i] =='L' || player1[i] =='N' || player1[i] =='O' || player1[i] =='R' || player1[i] =='S' || player1[i] =='T' || player1[i] =='U'){
            p1score ++;
        }
        else if(player1[i] == 'D' || player1[i] =='G'){
            p1score += 2;
        }
        else if(player1[i] == 'B' || player1[i] == 'C' || player1[i] =='M' || player1[i] =='P'){
            p1score += 3;
        }
        else if(player1[i] == 'F' || player1[i] =='H' || player1[i] =='V' || player1[i] =='W' || player1[i] =='Y'){
            p1score += 4;
        }
        else if(player1[i] == 'K'){
            p1score += 5;
        }
        else if(player1[i] == 'J' || player1[i] =='X'){
            p1score += 8;
        }
        else if(player1[i] == 'Q' || player1[i] =='Z'){
            p1score += 10;
        }
    }
        for(int i = 0, l = strlen(player2); i < l; i++){
        player2[i] = toupper(player2[i]);
        if(player2[i] == 'A' || player2[i] == 'E' || player2[i] =='I' || player2[i] =='L' || player2[i] =='N' || player2[i] =='O' || player2[i] =='R' || player2[i] =='S' || player2[i] =='T' || player2[i] =='U'){
            p2score ++;
        }
        else if(player2[i] == 'D' || player2[i] =='G'){
            p2score += 2;
        }
        else if(player2[i] == 'B' || player2[i] == 'C' || player2[i] =='M' || player2[i] =='P'){
            p2score += 3;
        }
        else if(player2[i] == 'F' || player2[i] =='H' || player2[i] =='V' || player2[i] =='W' || player2[i] =='Y'){
            p2score += 4;
        }
        else if(player2[i] == 'K'){
            p2score += 5;
        }
        else if(player2[i] == 'J' || player2[i] =='X'){
            p2score += 8;
        }
        else if(player2[i] == 'Q' || player2[i] =='Z'){
            p2score += 10;
        }
    }
    if(p1score > p2score){
        printf("Player 1 wins!\n");
    }
    else if(p2score > p1score){
        printf("Player 2 wins!\n");
    }
    else printf("Tie!\n");
}


