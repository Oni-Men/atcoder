#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  vector<vector<int>> xy(2, {0, 0});
  int c = 0;
  rep(i, h) {
    cin >> s[i];
    rep(k, s[i].size()) {
      if (s[i][k] == 'o') {
        xy[c] = {k, i};
        c++;
      }
    }
  };

  cout << abs(xy[0][0] - xy[1][0]) + abs(xy[0][1] - xy[1][1]) << endl;

  return 0;
}