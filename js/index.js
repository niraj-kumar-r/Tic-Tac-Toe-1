const board = document.getElementsByClassName("board")[0];
let playerTurn = 1;

board.addEventListener("click", function updateBoardState(event) {
    event.target.classList.add(`board-piece-active-${playerTurn}`);
    playerTurn = playerTurn === 1 ? 2 : 1;
});

function play() {
    const boardArray = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ];
    const piecesAvailable = [1, 2, 3, 4, 5, 6, 7, 8, 9];
}
