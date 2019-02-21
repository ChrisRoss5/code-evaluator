#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
#include <unistd.h>
#include <ctime>
#include <queue>
#include <cmath>
#include <set>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef long long ll;
typedef pair<int, int> P;
#define X first
#define Y second

const int MAX = 500500;
const ll INF = 1e18;

multiset <int> Kup;
multiset <int> Prod;
int st[MAX], p[MAX];

int main()
{
  int n;
  scanf("%d", &n);

  REP(i, n)
    scanf("%d%d", &st[i], &p[i]);

  ll sol = 0;
  REP(i, n) {
    if (st[i] == 2) Kup.insert(p[i]);
    else {
      ll dod = -INF;
      if (!Kup.empty())
	dod = p[i] - *Kup.begin();
      
      ll zam = -INF;
      if (!Prod.empty())
	zam = p[i] - *Prod.begin();

      if (dod > zam && dod > 0) {
	Prod.insert(p[i]);
	Kup.erase(Kup.begin());
	sol += dod;
      }
      else if (zam >= dod && zam > 0) {
	Prod.erase(Prod.begin());
	Prod.insert(p[i]);
	sol += zam;
      }
    }
  }

  printf("%lld\n", sol);
  
  return 0;
}
