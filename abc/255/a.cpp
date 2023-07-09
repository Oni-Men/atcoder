#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int r, c;
  cin >> r >> c;
  int mat[2][2];
  rep(y, 2) rep(x, 2) cin >> mat[y][x];

  cout << mat[r - 1][c - 1] << endl;
  return 0;
}