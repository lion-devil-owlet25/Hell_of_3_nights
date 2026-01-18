#include <stdio.h>
struct job {
    char id;
    int deadline;
    int profit;
};
int main() {
    struct job j[5] = {
        {'A',2,60},
        {'B',1,100},
        {'C',3,20},
        {'D',2,40},
        {'E',1,20}
    };

    int n = 5, max = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int k = i + 1; k < n; k++) {
            if (j[i].profit < j[k].profit) {
                struct job temp = j[i];
                j[i] = j[k];
                j[k] = temp;
            }
        }
    }
    for (int i = 0; i < n; i++)
        if (j[i].deadline > max)
            max = j[i].deadline;

    char slot[max];
    for (int i = 0; i < max; i++)
        slot[i] = '-';

    int totalProfit = 0;
    for (int i = 0; i < n; i++) {
        for (int k = j[i].deadline - 1; k >= 0; k--) {
            if (slot[k] == '-') {
                slot[k] = j[i].id;
                totalProfit += j[i].profit;
                break;
            }
        }
    }

    printf("Job sequence: ");
    for (int i = 0; i < max; i++)
        printf("%c ", slot[i]);

    printf("\nTotal Profit = %d\n", totalProfit);

    return 0;
}

