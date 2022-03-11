let playerTurn = 1;

let boardArray = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
];
let piecesAvailable = ["11", "12", "13", "21", "22", "23", "31", "32", "33"];

const board = document.getElementsByClassName("board")[0];

board.addEventListener("click", function play(event) {
    let avail = updateBoard(event.target);
});

function updateBoard(piece) {
    if (piecesAvailable.includes(piece.id)) {
        piecesAvailable = piecesAvailable.filter((a) => a !== piece.id);

        boardArray[Number(piece.id[0]) - 1][Number(piece.id[1]) - 1] =
            playerTurn === 1 ? 1 : -1;

        if (winCheck(boardArray)) {
        }
        piece.classList.add(`board-piece-active-${playerTurn}`);

        playerTurn = playerTurn === 1 ? 2 : 1;
    } else if (!piecesAvailable.includes(piece.id)) {
        console.log("Place Occupied");
    }
}
