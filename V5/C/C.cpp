#include <iostream>
#include <set>

using namespace std;


int main() {
    int n;
    cin >> n;
    set<int> setik;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        if (setik.find(x) != setik.end()) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
        setik.insert(x);
    }
}
