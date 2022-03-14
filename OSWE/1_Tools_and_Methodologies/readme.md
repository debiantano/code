### JavaScript
```
/sol/                //1ra coincidencia
/cena/g              //global
/LA/i                //insensitive
/[eo]/ o /[0-5]/g    //encontrar cualquiera de los simbolos dentro de []
/[^0-9]/g            //todas las coincidencia q no marquen 0 a 9
/.h/g                //cualquier caracter
/\d/g                //encontrar un digito
/\D/g                //Todo lo q no sea digito
/\w/g                //solo caracteres q no sean simbolos
/\W/g                // todo - (alfabeto + digitos)
/\babc/g             //buscar 'abc' que se encuentre al inicio de la busqueda
/abc\b/g             //buscar 'abc' que se encuentre al final de la busqueda
/abc+/g              //buscar por lo menos abc,abcc,abccc,abccc..
/0*55/g              //buscar entre 0 a mas coincidencias 055,55
/abz?/g              //buscar entre 0 o 1 elemento q cumplan la secuencia "ab o abz"
/(lol){2}/g          //buscar las primeras 2 coincidencias
/(com)$/             //buscar una expresion al final del texto
/^(www)/             // al inicio de la cadena
/(?=)/               //
```

----

Compilar c#: `csc test.cs`


