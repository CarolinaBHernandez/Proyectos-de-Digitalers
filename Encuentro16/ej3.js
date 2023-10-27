/*Generar 4 botones y escribir 1 sola función. 
Cada botón hace referencia a un color diferente.

Al hacer click en cada botón imprimir por consola:
El color es: 
 */

function miFuncion(color) {
    console.log('El color es: ' +color);
}

var boton = docoument.getElementsbyTagName('button');

for(var i= 0; i < boton.length; i++) {
    boton[i].onclick = function() {
        miFuncion(this.innerHTML);
    };
}
