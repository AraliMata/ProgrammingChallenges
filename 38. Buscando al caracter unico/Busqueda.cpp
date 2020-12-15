#include "Busqueda.h"

void Busqueda::lector()
{
    int numeroCadenas = 0;
    string cadena;
    vector<string> cadenas;

    cin >> numeroCadenas;

    for (int i = 0; i < numeroCadenas; i++) 
    {
        cin >> cadena;
        cadenas.push_back(cadena);
    }
    
    for (int i = 0; i < numeroCadenas; i++)
        cout << secuencial(cadenas[i]) + binaria(cadenas[i]) << endl;
 
}

string Busqueda::secuencial(string linea)
{
    int contador = 0;
    int i = 1;
    string letraEspecial = " ";

    if (linea[linea.length() - 1] != linea[linea.length() - 2]) 
    {
        letraEspecial = linea[linea.length() - 1];
        contador = 1;
    }

    while (letraEspecial == " ") 
    {
        if (linea[i] != linea[i - 1])
            letraEspecial = linea[i - 1];
            
        i += 2;
        contador++;
    }

    return letraEspecial + " " + to_string(contador) + " ";
}

string Busqueda::binaria(string cadena)
{
    string subcadena = cadena;
    string letraEspecial = " ";
    string parteLinea = "";
    int mitad = 0;
    int contador = 0;
    int indicador = 0;
    int letraIzquierda, letraCentro, letraDerecha;

    while (letraEspecial == " ") 
    {
        mitad = subcadena.length() / 2 ;
        letraCentro = mitad;
        letraIzquierda = mitad - 1;
        letraDerecha = mitad + 1;
        int uno = subcadena.length() - 1;

        
        if ((subcadena.length() - 1) % 4 == 0) 
        {
            if (subcadena[letraCentro] != subcadena[letraIzquierda] && subcadena[letraCentro] != subcadena[letraDerecha]) 
                letraEspecial = subcadena[letraCentro];
    
            else if (subcadena[letraCentro] != subcadena[letraIzquierda] && subcadena[letraCentro] == subcadena[letraDerecha]) 
                subcadena = subcadena.substr(letraDerecha);
                
            else if (subcadena[letraCentro] == subcadena[letraIzquierda] && subcadena[letraCentro] != subcadena[letraDerecha]) 
                subcadena = subcadena.substr(0, letraIzquierda);
              
        }
        else if ((subcadena.length() - 1) % 4 != 0) 
        {
            if (subcadena[letraCentro] != subcadena[letraIzquierda] && subcadena[letraCentro] != subcadena[letraDerecha]) 
                letraEspecial = subcadena[letraCentro];

            else if (subcadena[letraCentro] == subcadena[letraIzquierda] && subcadena[letraCentro] != subcadena[letraDerecha]) 
            {
                if (subcadena.length() == 3) {
                    letraEspecial = subcadena[letraDerecha];
                }

                subcadena = subcadena.substr(letraDerecha);
            }
            else if (subcadena[letraCentro] != subcadena[letraIzquierda] && subcadena[letraCentro] == subcadena[letraDerecha]) 
            {
                if (subcadena.length() == 3) {
                    letraEspecial = subcadena[letraIzquierda];
                }

                subcadena = subcadena.substr(0, letraIzquierda);
            }

        }

        if (subcadena.length() == 1) 
            letraEspecial = subcadena[0];

        contador++;
    }

    return letraEspecial + " " + to_string(contador);
}


