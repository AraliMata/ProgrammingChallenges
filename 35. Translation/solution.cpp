#include <iostream>

using namespace std;

int main()
{
    string s;
    string t;
    string result = "YES";
    int c = 0;

    cin >> s;
    cin >> t;

    for(int i = s.length() - 1; i >= 0; i--){
        if(s[i] != t[c]){
            result = "NO";
            break;
        }
        c++;
    }

    cout << result;
    return 0;
}
