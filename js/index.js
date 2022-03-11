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

        piece.classList.add(`board-piece-active-${playerTurn}`);

        let winState = winCheck(boardArray);

        if (winState === 1) {
            document.querySelector(".bottom-text").textContent = "Player 1 won";
        } else if (winState === -1) {
            document.querySelector(".bottom-text").textContent = "Player 2 won";
        }

        playerTurn = playerTurn === 1 ? 2 : 1;
    } else if (!piecesAvailable.includes(piece.id)) {
        console.log("Place Occupied");
    }
}

function winCheck(array, side = 3) {
    const sumArray = [];
    let dia1 = 0;
    let dia2 = 0;

    for (let i = 0; i < side; i++) {
        let rowSum = 0;
        let colSum = 0;

        for (let j = 0; j < side; j++) {
            rowSum += array[i][j];
            colSum += array[j][i];
        }

        dia1 += array[i][i];
        dia2 = +array[i][side - i - 1];

        sumArray.push(rowSum);
        sumArray.push(colSum);
    }

    sumArray.push(dia1);
    sumArray.push(dia2);

    // row1 ,col1,row2,col2,row3,col3,dia1,dia2

    if (sumArray.includes(side)) {
        return 1;
    } else if (sumArray.includes(-side)) {
        return -1;
    } else {
        return 0;
    }
}
