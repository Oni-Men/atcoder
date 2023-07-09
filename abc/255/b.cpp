#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep1(i, n) for (int i = 1; i <= (n); i++)

int main() {
  int n, k;
  cin >> n >> k;

  vector<int> a(k);
  vector<long long> x(n), y(n);

  rep(i, k) cin >> a[i];
  rep(i, n) cin >> x[i] >> y[i];

  long long r = 0;

  rep(j, n) {
    long long m = 8e18;
    rep(i, k) {
      long long s = x[j] - x[a[i] - 1];
      long long t = y[j] - y[a[i] - 1];
      m = min(m, s * s + t * t);
    }
    r = max(r, m);
  }

  printf("%.12lf\n", sqrt((double)r));
  return 0;
}