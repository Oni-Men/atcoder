#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> a(n), x(q);
  rep(i, n) cin >> a[i];

  sort(a.begin(), a.end());

  vector<long long> rw(n + q, 0);
  for (long long i = 0; i < n; i++) rw[i + 1] = rw[i] + a[i];

  rep(i, q) {
    long long x;
    cin >> x;

    int st = 0, fi = n - 1;
    while (st <= fi) {
      int te = (st + fi) / 2;
      if (a[te] < x) }
  }

  return 0;
}
