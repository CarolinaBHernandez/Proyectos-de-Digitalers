var array =['Juan', 'Pedro', 'Jose','Alicia'];

//ARRAYS:

// length - me da la longitud -> array.length

// push - Agrega elemento al final -> array.push(10)

// pop - Elimina el último elemento -> array.pop()

// shift - Elimina el primer elemento -> array.shift()

// unshift - Agrega un elemento en la primer posición -> array.unshift(40)

// indexOf - Me devuelve el nro de índice de un elemento -> array.indexOf('Pedro')
// slice - Obtiene un porción del array. Se pasan 2 índices, el primero es desde donde
// empieza a cortar y el último es hasta donde llega pero no es incluido.
// array.slice(1, 2)

// splice - Modifica el array eliminando y agregando elementos. Se pasan índices donde el primer
// número corresponde al índice donde se comenzará a borrar. El 2do número corresponde a la cantidad
// de elementos a eliminar. Luego se pasan cualquier cantidad de valores que se quieran agregar.
// array.splice(1, 2, 'Jose', 4, 'Juliana')

// sort - Método para ordenar un array -> array.sort()
// PARA NUMEROS!!: array2.sort((a, b) => a - b);

// concat - Une diferentes arrays - var unificados = array.concat(array2);

//OBJETOS LITERALES:

/*
Para acceder a los elementos tenemos 2 alternativas:
console.log(persona.nombre);
console.log(persona['nombre']);

##########
Para modificar algún elemento:
persona.edad = 31;
console.log(persona.edad);

##########
Para agregar una nueva propiedad:
persona.calle = 'piedras 3321';

##########
Para eliminar una propiedad:
delete persona.provincia;

##########
Objetos anidados
var persona = {
    nombre: 'Juan',
    edad: 30,
    direccion: {
        calle: 'Piedras',
        altura: 3321,
        provincia: 'Buenos Aires'
    }
};
console.log(persona.direccion.calle);

##########
Object.assign() - Copia 2 o más objetos en uno solo
var datos = Object.assign({}, persona, direccion);

##########
Desestructuración en un Objeto
var { nombre, edad } = persona;
##########
Arrays de Objetos

var empleados = [
    {
        nombre: 'Juan',
        apellido: 'Gonzalez',
        edad: 40
    },
    {
        nombre: 'Ana',
        apellido: 'Gutierrez',
        edad: 25
    },
    {
        nombre: 'Fernando',
        apellido: 'Perez',
        edad: 34
    }
]

empleados.sort((a, b) => a.edad - b.edad);
var empleado = empleados[empleados.length - 1];
document.write('El empleado se llama ' + empleado.nombre + ' ' + empleado.apellido);

##########
Insertar lista en un contenedor
var empleados = ['Juan', 'Alicia', 'Pedro'];
document.getElementById('caja').innerHTML = empleados;

// BUCLE FOR

// for (inicialización; condición; expresión de actualización) {
        // Bloque de código a repetir
//}

/* 
- inicialización: variable de control que se inicializa antes que comience el bucle
- condición: Se evalúa una condición que dará verdadero o falso
- actualización: expresión que se evalúa después de cada iteración

for(let i = 1; i <= 5; i++) {
    console.log(i);
}

EJEMPLO
#######

var empleados = [
    {
        nombre: 'Juan',
        apellido: 'Gonzalez',
        edad: 40
    },
    {
        nombre: 'Ana',
        apellido: 'Gutierrez',
        edad: 25
    },
    {
        nombre: 'Fernando',
        apellido: 'Perez',
        edad: 34
    }
]

var mensaje = '';

for(let i = 0; i < empleados.length; i++) {
    mensaje += empleados[i].nombre + ' ' + empleados[i].apellido + ' - ';
}

console.log(mensaje);

*/
/*Dado un número entero, el script debe mostrar una cuenta hacia atrás, es decir, 
una lista de numeros separados por coma desde el número pasado por teclado hasta el 0.

var contar, numero, mensaje='';

numero = parseInt(prompt("Coloque un numero entero"));
for(contar = numero; contar > 0;  contar--) {
  mensaje += contar + ", ";
}
mensaje += contar; 
alert(mensaje);
*/