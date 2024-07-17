#include <cs50.h>
#include <stdio.h>

int get_valid_int(void);
void create_pyramid(int n);

int main(void)
{
    int height = get_valid_int();
    create_pyramid(height);
}

void create_pyramid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int x = n; x > i + 1; x--)
        {
            printf(" ");
        }
        for (int x = 1; x <= i + 1; x++)
        {
            printf("#");
        }
        printf("  ");
        for (int x = 1; x <= i + 1; x++)
        {
            printf("#");
        }
        printf("\n");
    }
}

int get_valid_int(void)
{
    while (true)
    {
        int valid_int = get_int("Height: ");
        if (valid_int > 0)
        {
            return valid_int;
        }
    }
}
