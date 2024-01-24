#include <iostream>

#define ll long long
#define pb push_back
#define vi vector<int>
#define sz(a) (int((a).size()))
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>

using namespace std;

int a, b;
int x, y;

int main() {

	cin >> x >> y >> a >> b;
	
	if (x >= a && x - a + y >= b) 
	cout << "Yes\n";
	else cout << "No\n";
	
	return 0;
}