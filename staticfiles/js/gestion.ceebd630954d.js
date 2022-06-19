/*
ARCHIVO CREADO MANUALMENTE PARA EL CONTROL DE EVENTOS EN EL TEMPLATE GESTION CURSO, ESTA SE IMPORTA EN EL TEMPLATE
Y REALIZA LAS FUNCIONES QUE ESTAN A CONTINUACION.
PARA INPUTS, SE LES AGREGA UN ID EN EL TEMPLATE Y LUEGO SE ASIGNAN A OTRA VARIABLE LOCAL EN ESTE ARCHIVO
(IDEALMENTE DEL MISMO NOMBRE) SI SON SINGULARES. SI SON PLURALES (CLASES) SE DEBE ASIGANR LA VARIABLE CON UN . ANTES DEL NOMBRE
*/
// ESTA VARIABLE CORRESPONDE AL FORMULARIO DONDE ESTAN EL INPUT NOMBRE Y EL INPUT CREDITOS
const $formularioCurso = document.getElementById('formularioCurso');
// ESTA VARIABLE CORRESPONDE AL NOMBRE CON EL QUE SE INGRESARAN LOS CURSOS
const $txtNombre = document.getElementById("txtNombre");
// ESTA VARIABLE CORRESPONDE A LA CLASE DE TODOS LOS BOTONES QUE SEAN DE ELIMINACION
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');
// ESTA VARIABLE SE UTILIZA PARA EL BOTON GUARDAR - NO SE QUE HACE
const form = document.querySelector('#formularioCurso');
// ESTA VARIABLE CORRESPONDE AL FORMULARIO DE GESTION DE DOCENTES
const $formularioDocente = document.getElementById('formularioDocente');

// FUNCION VALIDA PARA GESTION DE CURSOS Y DOCENTES
(function() {
    /* 
    Swal.fire({
        titleText : "Hola",
        text : "Mensaje de prueba",
        icon : "success",
        confirmButtonText: "Ok!",
    });
    */
    // ADDEVENTLISTENER SOBRE EL FORMULARIO DONDE SE GUARDEN LOS CURSOS
    $formularioCurso.addEventListener('submit', function(e) {
        // SE EXTRAE COMO STRING LA VARIABLE TXTNOMBRE ORIGINAL, Y SE USA .TRIM PARA ELIMINAR ESPACIOS VACIOS
        let nombre = String($txtNombre.value).trim();
        // SI NO QUEDA NADA EN EL STRING NOMBRE, SIGNIFICA QUE ESTA VACIO Y SE RESTRINGE SU GUARDADO
        if(nombre.length < 3){
            e.preventDefault();
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El nombre del curso es muy corto!',
            });
        } else {
            e.preventDefault();
            Swal.fire({
                // SE DA LA OPCION PARA CONFIRMAR SI QUIERE O NO GUARDAR LOS CAMBIOS
                title: 'Quieres guardar los cambios?',
                showCancelButton: true,
                confirmButtonText: 'Guardar',
            }).then((result) => {
                // SI SE QUIEREN GUARDAR, SE NOTIFICA SE GUARDA
                if (result.isConfirmed) {
                    Swal.fire({
                        titleText : "'Guardado!'",
                        text : "",
                        icon : "success",
                        confirmButtonText: "Ok!",
                    }).then((result) => {
                        form.submit();
                    });
                }
            });
        }
    });
    
    // ACCIONES PARA BOTONES ELIMINAR, SI SE CONFIRMA EL RESULTADO, SE CONTINUA AL LINK
    btnsEliminacion.forEach(btn => {
        // SOBRE EL CLICK
        btn.addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                title: 'Estas seguro?',
                text: " ",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, eliminar!',
              }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire({
                        title: 'Eliminado!',
                        text: 'El curso ha sido eliminado.',
                        icon: 'success',
                    }).then((result) => {
                        location.href = e.target.href;
                    });
                }
              });
            /*  
            Swal.fire({
                title: "Confirma la eliminación del curso?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm:()=>{
                    location.href = e.target.href;
                },
                allowOutsideClick:() => false,
                allowEscapeKey: () => false,
            });
            */
        });
    });

    // FUNCION QUE GESTIONA EL FORMULARIO DE GESTION DE DOCENTES
    $formularioDocente.addEventListener('submit', function(e) {
    
    });
    
})();