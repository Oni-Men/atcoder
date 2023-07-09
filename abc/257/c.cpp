#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n;
  string s;
  cin >> n;
  cin >> s;
  vector<int> w(n);
  rep(i, n) cin >> w[i];

  vector<int> a(n, 0), c(n, 0);
  rep(i, n) {
    if (i >= 1) {
      c[i] = c[i - 1];
    }
    if (s[i] == '0') {
      c[i]++;
    }

    if (i >= 1) {
      a[i] = a[i - 1];
    }
    if (s[i] == '0') {
      a[i]++;
    }
  }

    return 0;
}
