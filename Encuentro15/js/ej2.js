/*Crear un Objeto Literal llamado coche. Agregar como keys:

- marca
- modelo
- color
- numeroRuedas
- numeroPuertas
- precio

Como valor de cada key pongan lo que deseen.
Luego imprimir por consola un texto que involucre todos los keys mencionados.
 Se debe alternar una vez cada uno de los métodos para traer cada valor
 (uno con punto y otro con [])*/



var coche = {marca: "Honda", modelo: "Civic", color: "Azul", numeroRuedas: 4, numeroPuertas: 4, precio: 10630000};
  
  console.log("Información del coche:");
  console.log("Marca: " + coche.marca);
  console.log("Modelo: " + coche["modelo"]);
  console.log("Color: " + coche.color);
  console.log("Número de ruedas: " + coche["numeroRuedas"]);
  console.log("Número de puertas: " + coche.numeroPuertas);
  console.log("Precio: $" + coche["precio"]);
  