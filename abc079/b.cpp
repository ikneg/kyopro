#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<long long> lucas(87);
    lucas.at(0) = 2;
    lucas.at(1) = 1;
    for (int i = 2; i <= 86; i++) {
        lucas.at(i) = lucas.at(i-2) + lucas.at(i-1);
    }

    int N;
    cin >> N;
    cout << lucas.at(N) << endl;
}