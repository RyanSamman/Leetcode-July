#include <stdio.h>

#define MAX_INT 2000000;

unsigned int A(unsigned int n)
{
    return (n*(n + 1))/2;
}

int arrangeCoins(int n)
{
    unsigned int left = 0;
    unsigned int middle;
    unsigned int right = MAX_INT;

    unsigned int sol = 0;

    unsigned int prev1 = 0;
    unsigned int prev2 = 0;
    unsigned int prev3 = 0;
    unsigned int prev4 = 0;

    while (1)
    {
        middle = (left + right) / 2;

        sol = A(middle);

        // Left
        if (n < sol)
        {
            right = middle - 1;
            //middle = (left + middle) / 2;
        }
        // Right
        else
        {
            left = middle + 1;
            //middle = (right + middle) / 2;
        }

        prev4 = prev3;
        prev3 = prev2;
        prev2 = prev1;
        prev1 = middle;

        printf("%i %i %i %i %i %i\n", sol, middle, prev1, prev2, prev3, prev4);

        if (prev1 == prev3 && prev2 == prev4) {
            break;
        }
    }

    unsigned int answer = (prev1 > prev2) ? prev2 : prev1;
    return middle;
}

int main(void)
{
    printf("%i", A(60070));
    printf("%i", arrangeCoins(1804289383));
}
