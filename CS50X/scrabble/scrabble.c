#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char clist[26] = {'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int pointlist[26] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    int n = 2;
    string userinputs[n];
    int userscore[2] = {0, 0};
    for (int i = 0; i < n; i++)
    {
        userinputs[i] = get_string("Player %i: ", i + 1);
        int length = strlen(userinputs[i]);
        for (int x = 0; x < length; x++)
        {
            userinputs[i][x] = tolower(userinputs[i][x]);
            for (int y = 0; y < 26; y++)
            {
                if (userinputs[i][x] == clist[y])
                {
                    userscore[i] += pointlist[y];
                }
            }
        }
    }
    if (userscore[0] > userscore[1])
    {
        printf("Player 1 wins!\n");
    }
    else if (userscore[0] < userscore[1])
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
