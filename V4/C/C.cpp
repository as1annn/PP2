#include <iostream>
#include <set>
#include <string>

using namespace std;


int main() {
    int n;
    cin >> n;
    set<string> setik;
    for (int i = 0; i < n; ++i) {
        string x;
        cin >> x;
        setik.insert(x);
    }
    cout << setik.size() << endl;
}
