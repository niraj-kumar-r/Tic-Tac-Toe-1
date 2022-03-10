const board = document.getElementsByClassName("board")[0];
console.log(board);

board.addEventListener("click", (event) => {
    console.log(event.target.id);
    event.target.classList.add("board-piece-active-1");
});
