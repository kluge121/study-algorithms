#include<iostream>

using namespace std;

int f(int n, int k)
{
    if (k == n) return 1;
    else if (k == 1) return n;
    else return f(n - 1, k - 1) + f(n - 1, k);
}

int main()
{
    int n, k;
    cin >> n >> k;
    cout << f(n, k) << endl;

    return 0;
}
