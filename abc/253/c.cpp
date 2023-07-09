#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;

  multiset<int> set;
  int q, c, x;
  rep(i, n) {
    cin >> q;
    if (q == 1) {
      cin >> x;
      set.insert(x);
    } else if (q == 2) {
      cin >> x >> c;
      while (c-- && set.find(x) != set.end()) {
        set.erase(set.find(x));
      }
    } else {
      cout << *set.rbegin() - *set.begin() << endl;
    }
  }

  return 0;
}