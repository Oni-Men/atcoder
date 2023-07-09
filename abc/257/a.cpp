#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, x;
  cin >> n >> x;

  char c = 'A' + ((x - 1) / n);
  cout << c << endl;
  return 0;
}