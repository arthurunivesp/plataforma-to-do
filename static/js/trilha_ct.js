document.addEventListener("DOMContentLoaded", function() {
    // Função para mover o avatar e o nome
    const userProfile = document.getElementById("user-profile");
    let isDragging = false;
    let offsetX, offsetY;

    userProfile.addEventListener("mousedown", function(e) {
        isDragging = true;
        offsetX = e.clientX - userProfile.offsetLeft;
        offsetY = e.clientY - userProfile.offsetTop;
        userProfile.style.position = "absolute";
        userProfile.style.zIndex = 5;
    });

    document.addEventListener("mousemove", function(e) {
        if (isDragging) {
            userProfile.style.left = (e.clientX - offsetX) + "px";
            userProfile.style.top = (e.clientY - offsetY) + "px";
        }
    });

    document.addEventListener("mouseup", function() {
        isDragging = false;
    });

    // Função para animação dos cursos
    const cursos = document.querySelectorAll(".curso");

    cursos.forEach(function(curso) {
        curso.addEventListener("mouseover", function() {
            curso.style.transform = "translateY(-10px)";
            curso.style.backgroundColor = "#7FFFD4";
            curso.style.transition = "transform 0.3s, background-color 0.3s";
        });
        curso.addEventListener("mouseout", function() {
            curso.style.transform = "translateY(0)";
            curso.style.backgroundColor = "#fff";
            curso.style.transition = "transform 0.3s, background-color 0.3s";
        });
    });
});
