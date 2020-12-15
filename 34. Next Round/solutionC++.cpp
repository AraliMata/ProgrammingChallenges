#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    int n;
    int k;
    int temp;
    int cont = 0;
    vector<int> scores;

    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++){

        scanf("%d", &temp);
        scores.push_back(temp);
    }

    for(int i = 0; i < n; i++){
        if(scores[i] >= scores[k-1] && scores[i] > 0){
            cont++;
        }
    }

    printf("%d", cont);
    return 0;
}
