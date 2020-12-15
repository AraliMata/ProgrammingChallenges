#include <iostream>
#include "Busqueda.h"

int main()
{
    Busqueda::lector();
    cout << Busqueda::secuencial("AACCZZTTVXX");
    cout << Busqueda::binaria("AACCZZTTVXX") << endl;
    cout << Busqueda::secuencial("AAB");
    cout << Busqueda::binaria("AAB") << endl;
    cout << Busqueda::secuencial("CCAAXWWTT");
    cout << Busqueda::binaria("CCAAXWWTT") << endl;
    cout << Busqueda::secuencial("XXYYZZAAC");
    cout << Busqueda::binaria("XXYYZZAAC") << endl;
    
}

