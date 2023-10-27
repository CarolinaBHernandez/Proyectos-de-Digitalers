function sumaArray(array){
    var suma = 0;
    for(var i = 0; i < array.length; i++){
        suma += array[i];
    }
    return suma;
}

var array = [1, 2, 3, 4, 5];

console.log(sumaArray(array));