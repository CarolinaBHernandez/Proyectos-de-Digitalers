
// Paso 1: Pedir el rol al usuario
const rol = prompt('Ingrese su rol (admin o recursos):');

// Paso 2: Verificar si el rol es correcto
if (rol === 'admin' || rol === 'recursos') {
    // Paso 3: Pedir la clave al usuario
    const clave = prompt('Ingrese la clave:');

    // Paso 4: Verificar si la clave es correcta (clave = 1234)
    if (clave === '1234') {
        // Paso 5: Pedir el nombre de usuario al usuario
        const nombreUsuario = prompt('Ingrese su nombre de usuario:');

        // Paso 6: Imprimir el nombre de usuario en el contenedor con innerHTML
        const contenedor = document.createElement('h1');
        contenedor.innerHTML = `Hola ${nombreUsuario}, bienvenida a nuestra aplicación`;
        document.body.appendChild(contenedor);
    } else {
        alert('Clave incorrecta. Por favor, intente nuevamente.');
    }
} else {
    alert('Ha habido un error, pregunte a su supervisor rol y contraseñas correctas.".');
}
