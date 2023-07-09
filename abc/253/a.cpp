#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  vector<int> ar{a, b, c};

  sort(ar.begin(), ar.end());

  if (ar[1] == b)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}