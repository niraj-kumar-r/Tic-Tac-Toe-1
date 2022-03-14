let playerTurn = 1;
let singlePlayer = true;

let boardArray = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
];
let piecesAvailable = ["11", "12", "13", "21", "22", "23", "31", "32", "33"];

const board = document.getElementsByClassName("board")[0];

board.addEventListener("click", play);

function play(event) {
    if (singlePlayer) {
        playSinglePlayer(event);
    } else {
        playTwoPlayer();
    }
}

function playSinglePlayer(event) {
    if (piecesAvailable.includes(event.target.id)) {
        updateBoard(event.target);
        if (piecesAvailable.length !== 0) {
            setTimeout(updateBoard, 200, compAlgo(boardArray));
        }
    }
}

function playTwoPlayer(event) {
    if (piecesAvailable.includes(event.target.id)) {
        updateBoard(event.target);
    }
}

function updateBoard(piece) {
    piecesAvailable = piecesAvailable.filter((a) => a !== piece.id);

    boardArray[Number(piece.id[0]) - 1][Number(piece.id[1]) - 1] =
        playerTurn === 1 ? 1 : -1;

    piece.classList.add(`board-piece-active-${playerTurn}`);

    let winState = winCheck(boardArray);

    if (winState === 1) {
        showResult("Player Red won");
    } else if (winState === -1) {
        showResult("Player Green won");
    } else if (piecesAvailable.length === 0) {
        showResult("Tie");
    }

    playerTurn = playerTurn === 1 ? 2 : 1;
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
        dia2 += array[i][side - i - 1];

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

function showResult(result) {
    document.querySelector(".bottom-text").textContent = result;
    board.removeEventListener("click", play);
    board.style.opacity = 0.3;
}

/**
 * returns an available piece on the board according to algorithm
 *
 * @param {Array} array is the array representation of the current board state as an array of arrays
 * @param {Number} side is the number of pieces on one side of the board, like 3,4,5,etc.
 *
 * returns the piece chosen by the algorithm by document.getElementById(id)
 */
function compAlgo(array, side = 3) {
    const newArray = array.slice();
    const actualValue = playerTurn === 1 ? 1 : -1;

    for (let id of piecesAvailable) {
        // checking where I am winning
        newArray[Number(id[0] - 1)][Number(id[1] - 1)] = actualValue;
        let winStateTemp = winCheck(newArray, side);
        newArray[Number(id[0] - 1)][Number(id[1] - 1)] = 0;

        if (actualValue === winStateTemp) {
            return document.getElementById(id);
        }
    }

    for (let id of piecesAvailable) {
        // checking where the opponent is winning
        newArray[Number(id[0] - 1)][Number(id[1] - 1)] = -actualValue;
        let winStateTemp = winCheck(newArray, side);
        newArray[Number(id[0] - 1)][Number(id[1] - 1)] = 0;
        if (winStateTemp === -actualValue) {
            return document.getElementById(id);
        }
    }

    if (piecesAvailable.includes("22")) {
        return document.getElementById("22");
    } else {
        let randomId =
            piecesAvailable[Math.floor(Math.random() * piecesAvailable.length)];

        return document.getElementById(randomId);
    }
}
