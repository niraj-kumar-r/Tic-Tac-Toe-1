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
    console.log(compAlgo(boardArray));
    // if (singlePlayer) {
    //     updateBoard(event.target);
    //     updateBoard(compAlgo(boardArray));
    // } else {
    //     updateBoard(event.target);
    // }
}

function updateBoard(piece) {
    if (piecesAvailable.includes(piece.id)) {
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

function showResult(result) {
    document.querySelector(".bottom-text").textContent = result;
    board.removeEventListener("click", play);
    board.style.opacity = 0.3;
}

function compAlgo(array, side = 3) {
    const newArray = array.slice();
    const actualValue = playerTurn === 1 ? 1 : -1;

    for (let id in piecesAvailable) {
        newArray[Number(id[0])][Number(id[1])] = actualValue;
        let winStateTemp = winCheck(newArray, side);
        newArray[Number(id[0])][Number(id[1])] = 0;
        if (actualValue === winStateTemp) {
            console.log(document.getElementById(`$(id)`));
            return document.getElementById(`$(id)`);
        }
    }

    for (let id in piecesAvailable) {
        newArray[Number(id[0])][Number(id[1])] = -actualValue;
        let winStateTemp = winCheck(newArray, side);
        newArray[Number(id[0])][Number(id[1])] = 0;
        if (actualValue === -winStateTemp) {
            console.log(document.getElementById(`$(id)`));
            return document.getElementById(`$(id)`);
        }
    }

    if (piecesAvailable.includes("22")) {
        return document.getElementById("22");
    } else {
        return document.getElementById(
            piecesAvailable[Math.floor(Math.random * piecesAvailable.length)]
        );
    }
}
