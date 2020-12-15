#include <iostream>
#include <vector>

using namespace std;
int main()
{
    int t;
    int a, b;
    int cont = 0;
    vector<int> move;

    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> a;
        cin >> b;

        if(a % b == 0){
            move.push_back(0);
        }else if(a % b != 0){
            while (a % b != 0){
                a += 1;
                cont += 1;
            }
            move.push_back(cont);
            cont = 0;
        }
    }

    for(int i = 0; i < t; i++){
        cout << move[i] << endl;
    }
    return 0;
}
