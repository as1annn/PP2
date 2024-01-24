#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    int x;
    cin >> x;
    int cnt = x, max = x;
    for( int i=1; i<n; i++){
        cin >> x;
        cnt+=x;
        if(max<x)
            max = x;
    }
    cout << cnt << " " << max << endl;

    return 0;
}