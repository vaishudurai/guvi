#include <stdio.h>
 int main() {
        long long int n, d[100], i, j, temp;
        scanf("%lld", &n);
        for (i = 0; i < n; i++)
                scanf("%lld", &d[i]);

        for (i = 0; i < n-1; i++) {
                for (j = i + 1; j < n; j++) {
                        if (d[i] > d[j]) {
                                temp = d[i];
                                d[i] = d[j];
                                d[j] = temp;
                        }
                }
    }
        for (i = n-1; i >= 0; i--)
                printf("%lld", d[i]);

        return 0;
  }
