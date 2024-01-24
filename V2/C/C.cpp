#include <iostream>
#include <set>
using namespace std;
int main() {
    int n; cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) cin >> a[i];
    set<int> nums;
    for(int i = 0; i < n; i++) {
        set<int>::iterator lb = nums.lower_bound(a[i]);
        if(lb == nums.end() || *lb != a[i]) nums.insert(lb, a[i]);
        else nums.erase(lb);
	}
    cout << *nums.begin();
    return 0;
}