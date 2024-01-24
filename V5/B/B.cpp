#include<iostream>
using namespace std;
int a, b;
int x, y, xx, yy;
int main(){
    cin >> x >> y >> xx >> yy >> a >> b;
    if (x <= a  && a <= xx && yy <= b && b <= y)
        cout << "yes";
    else
        cout << "no";
    return 0;
}