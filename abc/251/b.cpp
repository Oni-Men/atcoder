#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, w;
  cin >> n >> w;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  vector<bool> ok(w + 1, false);

  rep(i, n) if (a[i] <= w) ok[a[i]] = true;
  rep(i, n) {
    rep(j, i) {
      if (i != j && a[i] + a[j] <= w) {
        ok[a[i] + a[j]] = true;
      }
    }
  }

  rep(i, n) {
    rep(j, i) {
      rep(k, j) {
        if ((i != j && j != k) && a[i] + a[j] + a[k] <= w) {
          ok[a[i] + a[j] + a[k]] = true;
        }
      }
    }
  }

  int ans = 0;
  rep(i, ok.size()) {
    if (ok[i]) ans++;
  }

  cout << ans << endl;

  return 0;
}
