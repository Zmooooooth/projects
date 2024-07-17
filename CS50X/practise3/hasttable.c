#include <ctype.h>

unsigned int hash(const char *word)
{
    return tuupper(word[0]) - 'A';
}
