#include <stdio.h>
struct edge {
    char u, v;
    int w;
};
int parent[10];

int find(int i) {
    while (parent[i])
        i = parent[i];
    return i;
}
void uni(int i, int j) {
    parent[j] = i;
}
int main() {
    struct edge e[10] = {
        {'B','D',5}, {'A','B',6}, {'C','F',9}, {'F','E',10},
        {'B','C',11}, {'G','F',12}, {'A','G',15},
        {'C','D',17}, {'D','E',22}, {'C','G',25}
    };

    int i, count = 0, sum = 0;

    printf("Edges in the Minimum Spanning Tree:\n");

    for (i = 0; i < 10 && count < 6; i++) {
        int u = find(e[i].u - 'A');
        int v = find(e[i].v - 'A');

        if (u != v) {
            uni(u, v);
            printf("%c - %c : %d\n", e[i].u, e[i].v, e[i].w);
            sum += e[i].w;
            count++;
        }
    }

    printf("Total weight of MST = %d\n", sum);
    return 0;
}

