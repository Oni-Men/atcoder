#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  long long x, a, d, n, l;
  cin >> x >> a >> d >> n;
  l = a + (n - 1) * d;

  if (x <= min(a, l)) {
    cout << min(a, l) - x << endl;
  } else if (x >= max(a, l)) {
    cout << x - max(a, l) << endl;
  } else {
    long long m;
    m = abs((x - a) % d);
    cout << min(m, abs(d) - m) << endl;
  }

  return 0;
}