#include <iostream>
#include <map>
using namespace std;

int main(){
    int n, m;
    cin >> n;
    map<string, int> k;
    string s;
    for(int i=0; i<n; i++){
        cin >> s;
        k[s]++;
    }
    cin >> m;
    for(int i=0; i<m; i++){
        cin >> s;
        k[s]++;
    }
    map<string, int>:: iterator it;
    for(it = k.begin(); it!=k.end(); it++){
        if(it->second == 1)
            cout << it->first << endl;
    }

    return 0;
}