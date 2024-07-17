#include <stdio.h>

int main(void)
{
    char *s = "Test!";
    int index = 0;
    while(s[index] != '\0')
    {
        printf("%c",s[index]);
        index++;
    }
    printf("\n");
}
