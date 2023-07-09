#include "../stdc++.h"

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  rep(i, k) {
    vector<int> b;
    for (int j = i; j < n; j += k) {
      b.push_back(a[j]);
    }

    sort(b.begin(), b.end());

    for (int j = i; j < n; j += k) {
      a[j] = b[j / k];
    }
  }

  vector<int> tmp = a;
  sort(tmp.begin(), tmp.end());
  if (a == tmp)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}