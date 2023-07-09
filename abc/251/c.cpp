#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int n, t;
  cin >> n;
  string s;
  rep(i, n) cin >> s >> t;

  set<int> scores;
  set<string> excludee;

  rep(i, n) {
    if (excludee.contains(s[i])) {
      continue;
    }
  }

  return 0;
}
