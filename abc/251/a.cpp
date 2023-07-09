#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define range(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  string s;
  cin >> s;

  string ans = "";
  for (;;) {
    ans += s;
    if (ans.size() == 6) {
      cout << ans << endl;
      break;
    }
  }

  return 0;
}
