#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  vector<bool> b(4);
  rep(i, n) cin >> a[i];

  int p = 0;
  rep(i, n) {
    b[0] = true;
    for (int j = 3; j >= 0; j--) {
      int k = j + a[i];
      if (k > 3) {
        p++;
      } else {
        b[j + a[i]] = true;
        b[j] = false;
      }
    }
  }

  return 0;
}
