document.addEventListener('DOMContentLoaded', function() {
    let carouselImages = document.querySelector('.carousel-images');
    let images = carouselImages.querySelectorAll('img');
    let currentIndex = 0;

    function updateCarousel() {
        const offset = -currentIndex * (images[0].offsetWidth + 20); // Considera a largura da imagem e o espaçamento
        carouselImages.style.transform = `translateX(${offset}px)`;
    }

    document.querySelector('.carousel-button.left').addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = images.length - 1;
        }
        updateCarousel();
    });

    document.querySelector('.carousel-button.right').addEventListener('click', function() {
        if (currentIndex < images.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateCarousel();
    });

    updateCarousel(); // Inicializa o carrossel na posição correta
});
