// Filtro de búsqueda para la tabla de estudiantes
document.addEventListener("DOMContentLoaded", function () {
    var filtro = document.getElementById("filtro");
    var tabla = document.getElementById("tabla-estudiantes");
    if (!filtro || !tabla) return;

    filtro.addEventListener("input", function () {
        var texto = filtro.value.toLowerCase();
        tabla.querySelectorAll("tbody tr").forEach(function (fila) {
            fila.style.display = fila.textContent.toLowerCase().includes(texto) ? "" : "none";
        });
    });
});
