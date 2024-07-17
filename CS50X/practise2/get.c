#include <stdio.h>
#include <stdlib.h>

int get_number(void);
int get_string(void);

int main(void)
{
    get_number();
    get_string();
}

int get_string(void)
{
    char *s = malloc(50 * 8);
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
    free(s);
    return 0;
}

int get_number(void)
{
    int number;
    printf("Int: ");
    scanf("%i", &number);
    printf("%i\n", number);
    return 0;
}
