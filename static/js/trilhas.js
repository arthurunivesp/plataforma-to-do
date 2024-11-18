document.addEventListener('DOMContentLoaded', function() {
    // Selecionar todos os cartões de trilha
    let cards = document.querySelectorAll('.trilha-card');
    let currentIndex = 0;

    // Função para atualizar a exibição do cartão
    function updateCardDisplay() {
        cards.forEach((card, index) => {
            if (index === currentIndex) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
        
        // Exibir ou ocultar o botão de alerta
        if (currentIndex === cards.length - 1) {
            document.querySelector('.trilha-alert').innerText = 'Você será o nosso TO-DO';
        } else {
            document.querySelector('.trilha-alert').innerText = 'Próxima Trilha';
        }
    }

    // Função para avançar para a próxima trilha
    function nextCard() {
        if (currentIndex < cards.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateCardDisplay();
    }

    // Adiciona evento de clique para o botão "Próxima Trilha"
    document.querySelector('.trilha-alert').addEventListener('click', nextCard);

    // Inicializar a exibição do cartão
    updateCardDisplay();
});
