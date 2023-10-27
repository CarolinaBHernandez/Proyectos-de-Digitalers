let nombre = prompt('Ingrese su nombre:');
let apellido = prompt('Ingrese su apellido:');
let edad = prompt('Ingrese su edad:');

mensaje = 'El usuario se llama "+ nombre + " " + apellido + " y tiene " + edad + " años.';

alert(mensaje);
console.log(mensaje);
document.write(mensaje);

let sueldo = parseInt(prompt('Ingrese su sueldo: '));
let bonus = parseInt(prompt('Ingrese el monto del bonus: '));
let total = sueldo + bonus;

alert("Gana por mes: " + total)
