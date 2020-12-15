#include <cstdio>

using namespace std;
int main()
{
    int fr1, fr2, fr3;
    int n;
    int cont;
    int cont1 = 0;

    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){

        cont = 0;
        scanf("%d %d %d", &fr1, &fr2, &fr3);
        
        if(fr1 == 1)
            cont ++;
        if(fr2 == 1)
            cont ++;
        if(fr3 == 1)
            cont ++;
        
        if(cont >= 2)
            cont1 ++;
    }

    printf("%d", cont1);

    return 0;
}

