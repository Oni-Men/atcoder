#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;

  int max = 0;
  vector<int> maxs;
  vector<int> a(n);
  vector<int> b(k);

  int t;
  rep(i, n) {
    cin >> t;
    if (t > max) {
      max = t;
      maxs.clear();
      maxs.shrink_to_fit();
    }
    if (t == max) {
      maxs.push_back(i + 1);
    }
  };

  bool res = false;

  rep(i, k) {
    cin >> t;
    rep(j, maxs.size()) {
      if (maxs[j] == t) {
        res = true;
      }
    }
  };

  if (res) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}