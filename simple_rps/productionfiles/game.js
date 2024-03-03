document.addEventListener('DOMContentLoaded', function () {
    const choices = document.querySelectorAll('.choice');
    choices.forEach(choice => {
        choice.addEventListener('click', function () {
            const move = this.dataset.move;
            const player = this.parentNode.parentNode.id === 'player1' ? 1 : 2;
            makeMove(move, player);
        });
    });
});

function makeMove(move, player) {
    fetch(`/make_move?move=${move}`)
        .then(response => response.json())
        .then(data => {
            const winner = data.winner;
            const resultElement = document.getElementById('results');
            resultElement.innerHTML = `Player ${player} - ${winner}`;
        });
}
