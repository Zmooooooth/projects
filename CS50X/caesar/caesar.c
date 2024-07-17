#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

bool check_valid(string input);
char rotate_chars(char inputchar, int number);
string plain_to_cypher(string inputstring, int number);

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Missing command-line argument\n");
        return 1;
    }
    if (argc > 2)
    {
        printf("Too many command-line arguments\n");
        return 1;
    }
    if (argv[1] < 0)
    {
        printf("Invalid Integer\n");
        return 1;
    }
    if (check_valid(argv[1]))
    {
        int number = atoi(argv[1]);
        string userinput = get_string("plaintext: ");
        string cypher = plain_to_cypher(userinput, number);
        printf("ciphertext: %s\n", cypher);
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

string plain_to_cypher(string inputstring, int number)
{
    int index = 0;
    while (inputstring[index] != '\0')
    {
        inputstring[index] = rotate_chars(inputstring[index], number);
        index++;
    }
    return inputstring;
}

bool check_valid(string input)
{
    int i = 0;
    while (input[i] != '\0')
    {
        if ((int) input[i] > 47 && (int) input[i] < 58)
        {
            i++;
        }
        else
        {
            return false;
        }
    }
    return true;
}

char rotate_chars(char inputchar, int number)
{
    int shift = number % 26;
    char lowerchars[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char upperchars[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    for (int x = 0; x < 26; x++)
    {
        if (inputchar == lowerchars[x])
        {
            shift = number % 26;
            if (shift + x >= 26)
            {
                shift = (shift + x) - 26;
                return lowerchars[shift];
            }
            else
            {
                shift = shift + x;
                return lowerchars[shift];
            }
        }
        if (inputchar == upperchars[x])
        {
            if (shift + x >= 26)
            {
                shift = (shift + x) - 26;
                return upperchars[shift];
            }
            else
            {
                shift = shift + x;
                return upperchars[shift];
            }
        }
    }
    return inputchar;
}
