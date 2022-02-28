function sumatoria(arreglo) {
    var total = 0;

    for(var i=0; i < arreglo.length; i++) {
        total += arreglo[i];
    }

    return total;
}

function numeroMayor(arreglo) {

    for(var i=0; i<arreglo.length; i++) {
        if(numMayor < arreglo[i]) {
            numMayor = arreglo[i];
        }
    }
    
    return numMayor;
}

function promedio(arreglo) {
    //Debe de obtener el promedio dado un arreglo
    var prom = 0;

    for(var i=0; i<arreglo.length;i++) {
        prom += arreglo[i];
    }

    return prom/arreglo.length;
}

function existeElemento(arreglo, elemento) {
    //Debe de regresar verdadero o falso (true or false) si el elemento que ingresamos 
    //se encuentra en el arreglo
    
    for(var i=0; i<arreglo.length; i++) {
        if(arreglo[i] === elemento) {
            return true;
        }
    }

    return false;

}