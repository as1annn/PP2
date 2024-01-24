#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int a,b,c,m1 = 0,m2 = 0,m3=0, premax = 0, premin = 0;
    cin>>a>>b>>c;
    premax = max(a,b);
    premin = min(a,b);

    if(c>=premax)
    {
        m1 = c;
        m2 = premax;
        m3 = premin;
    }
    else if(c<premax && c>=premin)
    {
        m1 = premax;
        m2 = c;
        m3 = premin;
    }
    else 
    {
        m1 = premax;
        m2 = premin;
        m3 = c;
    }
    cout<<m1<<" "<<m2<<" "<<m3;
    
    
    return 0;
}

