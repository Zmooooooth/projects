#include <cs50.h>
#include <math.h>
#include <stdio.h>

int get_amount_of_letters(string sentences);
int get_amount_of_words(string sentences);
int get_amount_of_sentences(string sentences);
float calculate_L(int words, int letters);
float calculate_S(int words, int sentences);
int calculate_formula(float L, float S);

int main(void)
{
    string userinput = get_string("Text: ");

    int letters = get_amount_of_letters(userinput);
    int words = get_amount_of_words(userinput);
    int sentences = get_amount_of_sentences(userinput);
    float L = calculate_L(words, letters);
    float S = calculate_S(words, sentences);
    int grade = calculate_formula(L, S);

    // printf("Letters: %i\n",letters);
    // printf("Words: %i\n",words);
    // printf("Sentences: %i\n",sentences);
    // printf("L: %f\n",L);
    // printf("S: %f\n",S);
    // printf("Clean_Grade: %i\n",grade);

    if (grade <= 0)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int calculate_formula(float L, float S)
{
    float result = 0.0588 * L - 0.296 * S - 15.8;
    result = roundf(result);
    return (int) result;
}

float calculate_L(int words, int letters)
{
    float sum = (float) letters / (float) words;
    sum *= 100;
    return sum;
}

float calculate_S(int words, int sentences)
{
    float result = (float) sentences / (float) words;
    result *= 100;
    return result;
}

int get_amount_of_letters(string sentences)
{
    int letters = 0;
    int i = 0;
    while (sentences[i] != '\0')
    {
        if ((64 < (int) sentences[i] && (int) sentences[i] < 91) ||
            (96 < (int) sentences[i] && (int) sentences[i] < 123))
        {
            letters += 1;
        }
        i++;
    }
    return letters;
}

int get_amount_of_words(string sentences)
{
    int words = 1;
    int i = 0;
    while (sentences[i] != '\0')
    {
        if (((int) sentences[i] == 32))
        {
            words += 1;
        }
        i++;
    }
    return words;
}

int get_amount_of_sentences(string sentences)
{
    int sentence = 0;
    int i = 0;
    while (sentences[i] != '\0')
    {
        if (((int) sentences[i] == 33) || ((int) sentences[i] == 46) || ((int) sentences[i] == 63))
        {
            sentence += 1;
        }
        i++;
    }
    return sentence;
}
