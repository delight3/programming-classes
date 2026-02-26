let board = JSON.parse(localStorage.getItem("kanban")) || {
  todo: [],
  progress: [],
  done: []
};

function saveBoard() {
  localStorage.setItem("kanban", JSON.stringify(board));
}

function createTaskElement(text, status, index) {
  const div = document.createElement("div");
  div.className = "task";
  div.draggable = true;
  div.innerText = text;

  div.addEventListener("dragstart", e => {
    e.dataTransfer.setData("text/plain", JSON.stringify({ status, index }));
  });

  return div;
}

function renderBoard() {
  ["todo", "progress", "done"].forEach(status => {
    const column = document.getElementById(status);
    column.innerHTML = "";

    board[status].forEach((task, index) => {
      const taskEl = createTaskElement(task, status, index);
      column.appendChild(taskEl);
    });
  });
}

function addTask(status) {
  const text = prompt("Task name:");
  if (!text) return;

  board[status].push(text);
  saveBoard();
  renderBoard();
}

// Drag & Drop handlers
document.querySelectorAll(".task-list").forEach(list => {
  list.addEventListener("dragover", e => e.preventDefault());

  list.addEventListener("drop", e => {
    const data = JSON.parse(e.dataTransfer.getData("text/plain"));
    const fromStatus = data.status;
    const taskIndex = data.index;
    const toStatus = list.id;

    const task = board[fromStatus][taskIndex];
    board[fromStatus].splice(taskIndex, 1);
    board[toStatus].push(task);

    saveBoard();
    renderBoard();
  });
});

renderBoard();
