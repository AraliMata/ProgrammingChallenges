#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int n;
    int cont;
    string word;
    string abr;
    vector<string> words;

    cin >> n;

    for(int i = 0; i < n; i++){
        cont = 0;
        abr = "";
        cin >> word;

        if(word.length() > 10)
        {
            for(int j = 0; j < word.length(); j++)
            {
                if(j == 0){
                    abr += word[0];
                }
                else if(j == word.length() - 1){
                    abr += to_string(cont) + word[word.length() - 1];
                }  
                else
                    cont ++;
            }
            words.push_back(abr);
        }else
        {
            words.push_back(word);
        }

    }
    for(int i = 0; i < n; i++){
            cout << words[i] << endl;
    }

    return 0;
}
