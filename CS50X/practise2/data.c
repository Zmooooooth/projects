#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("data.csv","a");
    if (file == NULL)
    {
        return 1;
    }
    char *name = get_string("Name: ");
    char *year = get_string("Year of birth: ");

    fprintf(file, "%s,%s\n", name, year);
    fclose(file);
    return 0;
}
