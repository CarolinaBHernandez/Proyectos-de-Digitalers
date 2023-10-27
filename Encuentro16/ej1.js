/*Escribir una función que tome como parámetro una letra.
Validar si esa letra es una vocal. Si es vocal devuelve true, sino false. */

function esVocal(letra){
    if(letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u' || letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U'){
        console.log('Verdadero');
        return true;
    }else{
        console.log('False');
        return false;
    }
}

var respuesta = prompt('Ingrese una letra: ');
var vocal = esVocal(respuesta);