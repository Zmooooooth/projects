#include <cs50.h>
#include <stdio.h>

long get_user_input(void);
bool checksum(long userin);

int main(void)
{
    long userin = get_user_input();
    bool response = checksum(userin);
    if (response == true)
    {
        if ((userin >= 340000000000000 && userin < 350000000000000) ||
            (userin >= 370000000000000 && userin < 380000000000000))
        {
            printf("AMEX\n");
        }
        else if (userin >= 5100000000000000 && userin < 5600000000000000)
        {
            printf("MASTERCARD\n");
        }
        else if ((userin >= 4000000000000 && userin < 5000000000000) ||
                 (userin >= 4000000000000000 && userin < 5000000000000000))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

bool checksum(long userin)
{
    int result1 = 0;
    int result2 = 0;
    bool first = true;

    while (userin != 0)
    {
        if (first)
        {
            result1 = result1 + userin % 10;
            userin = userin / 10;
            first = false;
        }
        else
        {
            int doubled_number = (userin % 10) * 2;
            if (doubled_number > 9)
            {
                result2 = result2 + doubled_number % 10 + doubled_number / 10;
            }
            else
            {
                result2 = result2 + doubled_number;
            }
            userin = userin / 10;
            first = true;
        }
    }

    int all_result = result1 + result2;
    if (all_result % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

long get_user_input(void)
{
    while (true)
    {
        long valid_long = get_long("Number: ");
        if (valid_long > 0)
        {
            return valid_long;
        }
    }
}
