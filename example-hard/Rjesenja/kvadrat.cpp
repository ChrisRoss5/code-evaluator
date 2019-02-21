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

const int MAX = 405;
const ll INF = 1e18;

ll p[MAX][MAX];
ll pref[MAX][MAX];
int n;

ll get_sum(int r1, int r2, int s1, int s2) {
  return pref[r2][s2] - pref[r1-1][s2] - pref[r2][s1-1] + pref[r1-1][s1-1];
}

int main()
{
  scanf("%d", &n);

  FOR(i, 1, n+1) {
    ll sum = 0;
    FOR(j, 1, n+1) {
      scanf("%lld", &p[i][j]);
      sum += p[i][j];
      pref[i][j] = pref[i-1][j] + sum;
    }
  }

  ll sol = -INF;

  REP(st, 2) {
    FOR(red, 1, n+1) {
      FOR(stup, 1, n+1) {
	int r1 = red, r2 = red+st, s1 = stup, s2 = stup+st;
	if (r2 > n || s2 > n) continue;
	ll sum = get_sum(r1, r2, s1, s2);
	sol = max(sol, sum);
      
	while (r1>1 && r2<n && s1>1 && s2<n) {
	  r1--; r2++; s1--; s2++;
	  sum += get_sum(r1, r2, s1, s2);
	  sol = max(sol, sum);
	}
      }    
    }
  }

  printf("%lld\n", sol);

  return 0;
}
