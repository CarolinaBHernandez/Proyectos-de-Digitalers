//Esta es una linea de comentarios.

/*Esto es un bloque
de comentarios*/

alert('Hola de nuevo');

var edad = 25;//entero
var precio = 15.40;//float
var cadenaDeTexto = 'Esto es una String'// string
var pregunta = true;// booleano
var noDefinido = undefined;

var persona = {
    nombre: 'Carolina', //Key value pair.
    edad: 30,
    ciudad:'Rosario'
}
 //Array

 /*const numeros = [1,2,3,4,5];

 console.log(numeros[0]); //Elemento 1
 console.log(numeros.length); //Tamaño del array
 numeros.push(6); // Agrega un elemento al final del Array
 console.log(numeros);
 numeros.pop(); //Elimina el ultimo elemento del Array.
 console.log(numeros);
 numeros.forEach(numero => {
    console.log(numero);
 }) */
 //
 document.write( '<h1>Hola como te va </h1>');
 document.write('<p>Esto es un <strong>parrafo.</strong></p>');
 //

 /* var nombre = prompt('Ingrese su nombre');
 var age = prompt('Ingrese su edad');
 alert(nombre);
 alert(age);
 var confirmacion = confirm('Su nombre es ' + nombre + ' y tiene ' + age + ' años.\n Confirma los datos?')
alert(confirmacion);

if(confirmacion) {
    alert('Bienvenido ' + nombre)
}*/

//var x = 10;
//var y = 20;
/* Test A */
//x = x + x + 1;
//y = y - y - x;
//console.log('Valor de X: ' + x);
//console.log('Valor de Y: ' + y); 
/* Test B */
//x = (x - y) + 4;
//y = 4 + (y + 5);
//console.log('Valor de X: ' + x);
//console.log('Valor de Y: ' + y);
/* Test C */
//x = x * 2 - 4;
//y = 4 - y * 2;
//console.log('Valor de X: ' + x);
//console.log('Valor de Y: ' + y);
/* Test D */
//x = (20 - x) / y;
//y = x + 2 / y;
//console.log('Valor de X: ' + x);
//console.log('Valor de Y: ' + y);
/* Test E */
//x = ((1 - x) * (y / 8)) * 4 * 0;
//y = (x + 3) / x;
//alert("Valor de X: " + x);
//alert("Valor de Y: " + y);

//console.log(edad);
//edad++;
//console.log(edad);
//edad--;
//console.log(edad);

var suma = 2 + 2; //Operador de Suma
var resta = 2 - 1; //Operador de Resta
var multiplicacion = 2 * 2; //Operador de Multiplicacion
var division = 10 / 2; //Operador de Division
var modulo = 10 % 2; //Operador de Modulo

console.log('El resultado de la suma es: '+suma);
console.log(typeof(suma));
/*var cadena = 'El resultado de la suma es: '+suma;
console.log(typeof(cadena)); convertir de entero a string

console.log(!pregunta);
var vacio = !suma;
*/ 

//&& y || --> and y or:
var valorA = true;
var valorB = false;

resultado1 = valorA && valorB;
resultado2 = valorB || valorB;

//Operadores relacionales

var numero1 = 1;
var numero2 = 20;

resultado1 = numero1 > numero2; //false
resultado2 = numero1 < numero2; //true

numero1 = 10;
numero2 = 20;

resultado = numero1 <= numero2; //true
resultado = numero1 >= numero2; //true
resultado = numero1 == numero2; //true
resultado = numero1 != numero2; //false

// Operador de igualdad estricta:
console.log(5 == 5); //true
console.log(5 == '5'); //true
console.log(5 === '5'); //false
console.log(5 === 5) //true
console.log(5 === '6'); //false

numb1 = '500';
numb2 = '200';
console.log('La suma de los valores es: ' +parseInt(numb1) + parseInt(numb2));

/* var edad = 20;
if(edad >= 18) {
    console.log("Sos mayor de edad.")
}else if(edad > 13 && edad > 18){
    console.log("Sos adolescente.")    
}
else{
    console.log("Sos menor de edad.")
}*/

/*var edad = prompt("Cual es tu edad?");
if (edad >= 20) {
    let nombre = prompt("Cual es tu nombre?.");
    if (nombre === "Pedro") {
        alert("Hola Pedro.");
    } else {
        alert("Tenes 20 años, pero tu nombre no es Pedro.");
    }
} else {
    alert("Tenes menos de 20 años.");
}*/

var estadoCivil = prompt("Ingrese su estado civil (soltero, casado, divorciado o viudo):");


switch (estadoCivil) {
    case "soltero":
        console.log("Usted está soltero.");
        break;
    case "casado":
        console.log("Usted está casado.");
        break;
    case "divorciado":
        console.log("Usted está divorciado.");
        break;
    case "viudo":
        console.log("Usted es viudo.");
        break;
    default:
        console.log("Estado civil no reconocido.");
        break;
}
/* Lo mismo que lo anterior pero con if anidados.

if (estadoCivil == "soltero") {
    console.log("Estas soltero!");
} else if (estadoCivil == "casado"){
    console.log("Estas casado!");
} else if (estadoCivil == "divorciado"){
    console.log("Estas divorciado!");
} else if (estadoCivil == "viudo"){
    console.log("Lo siento");
} else {
    console.log ("No reconozco ese estado civil");
}
 */

/*var respuestCorrecta = false;

switch (opcion) {
    case "1": 
        console.log("El caso 1 está vacío.");
        break;
    case "2":
        console.log("El caso 2 está vacío.");
        break;
    case "3":
        console.log("El caso 3 está vacío.");
        break;
    case "4":
        console.log("El caso 4 está vacío.");
        break;
    default:
        console.log("Opción no válida.");
        break;
}
*/

//La clase Date();

/*var fecha = new Date();
var dia = fecha.getDate();
var diaDeLaSemana= fecha.getDay();
var mes = fecha.getMonth();
var anio = fecha.getFullYear();

var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
var semana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
mes = meses [mes];
diaDehoy= semana[diaDeLaSemana];
console.log(dia);
console.log(mes);
console.log(anio);

document.write("Hoy es " +diaDehoy+ ' ' +dia+ " de" +mes+" del año" +anio )
console.log(diaDeLaSemana);
*/

//getElementById()

/*
var enunciado = document.getElementById(enunciado)
console.log(enunciado.innerHTML);
enunciado.innerHTML = 'Este es mi enunciado modificado';
console.log(enunciado.innerHTML);*/

//var otro_enunciado = document.querySelector('h1');
//console.log(otro_enunciado.innerHTML); 

/*var otro_enunciado = document.querySelectorAll('h1');
console.log(otro_enunciado); //Para traer todos los elementos


var otro_enunciado = document.querySelector('h1');
console.log(otro_enunciado[1].innerHTML);  //Para traer un elemento especifico del array.
*/

//WHILE Y DO WHILE:

var incremento = 0;
var maximo = 50;

while(incremento >= maximo){
    //Bloque de codigo a ejecutar
    incremento++;
    console.log(incremento);
}
//------------

do {
    //Bloque de codigo a ejecutar
    incremento++;
    document.write('Incremento vale: ' +incremento)
} while (incremento <= maximo);
