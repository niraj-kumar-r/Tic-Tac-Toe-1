const board = document.getElementsByClassName("board")[0];
let playerTurn = 1;

board.addEventListener("click", function updateBoardState(event) {
    event.target.classList.add(`board-piece-active-${playerTurn}`);
    playerTurn = playerTurn === 1 ? 2 : 1;
});
