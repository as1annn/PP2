#include <iostream>
#include <cmath>

using namespace std;
int main()
{
    int n;
    int people;
    cin >> n;
    int cnt = 0;
    people = n;
    while (people > 0){
        if(cnt % 7 != 0){
            if (cnt % 2 != 0)
                people += 3;
            else
                people -= 4;
        }
        cnt++;
    }
    cout << cnt;

    return 0;
}