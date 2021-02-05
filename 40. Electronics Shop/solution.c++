#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

vector<string> split_string(string);

bool wayToSort(int i, int j) { return i > j; }

int getMoneySpent(vector<int> keyboards, vector<int> drives, int b) {
    sort(keyboards.begin(), keyboards.end(), wayToSort);
    sort(drives.begin(), drives.end(), wayToSort);
    int price = 0;
    int max_price = 0;

    for(int keyboard: keyboards){
        for(int drive: drives){
            price = keyboard + drive;
            if(max_price < price && price <= b){
                max_price = price;
            }
        }
    }
    
    if(max_price == 0)
        return -1;
    else
        return max_price;
}


    

int main()
{
    vector<int> keyboards{3,1};
    vector<int> drives{5,2,8};
    int b = 10;

    cout << getMoneySpent(keyboards,drives,b);
    return 0;
}

