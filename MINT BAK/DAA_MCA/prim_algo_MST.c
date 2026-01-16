#include <stdio.h>

#define u 999

int main() {
    int n = 7;
    int cost[7][7] = {
        {0,1,5,u,u,u,u},
        {1,0,4,8,7,u,u},
        {5,4,0,6,u,2,u},
        {u,8,6,0,11,9,u},
        {u,7,u,11,0,3,10},
        {u,u,2,9,3,0,12},
        {u,u,u,u,10,12,0}
    };

    int visit[7] = {0};
    int mincost = 0;
    visit[0] = 1;

    for (int e = 0; e < n - 1; e++) {
        int min = u, o = 0, v = 0;

        for (int i = 0; i < n; i++) {
            if (visit[i]) {
                for (int j = 0; j < n; j++) {
                    if (!visit[j] && cost[i][j] < min) {
                        min = cost[i][j];
                        o = i;
                        v = j;
                    }
                }
            }
        }

        visit[v] = 1;
        mincost += min;
        printf("Edge %d-%d cost = %d\n", o, v, min);
    }

    printf("Minimum cost = %d\n", mincost);
    return 0;
}

