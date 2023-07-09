#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, k, q;
  cin >> n >> k >> q;
  vector<int> A(k), L(q);
  int index;
  rep(i, k) cin >> A[i];
  rep(i, q) cin >> L[i];

  rep(i, q) {
    int l = L[i] - 1;
    if (A[l] == n) {
      continue;
    }

    if (A[l] + 1 == A[l + 1]) {
      continue;
    }

    A[l]++;
  }

  rep(i, k) { cout << A[i] << ' '; }

  cout << endl;

  return 0;
}
