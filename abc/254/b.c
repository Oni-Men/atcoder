#include <stdio.h>
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  scanf("%d", &n);
  int a[n][30];

  rep(i ,n) {
    a[i][0] = a[i][i] = 1;
    for (int j = 1; j < i; j++) {
      a[i][j] = a[i-1][j-1] + a[i-1][j];
    }

    rep(j, i+1) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
}
