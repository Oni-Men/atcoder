#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<string> reels(n);
  vector<int> tlist;
  rep(i, n) cin >> reels[i];
  rep(i, 10) {
    vector<int> counts(10, 0);
    vector<int> times(10);
    rep(j, n) counts[reels[j].find('0' + i)]++;
    rep(j, 10) { times[j] = j + 10 * (counts[j] - 1); }
    tlist.push_back(*max_element(times.begin(), times.end()));
  }

  cout << *min_element(tlist.begin(), tlist.end()) << endl;
  return 0;
}