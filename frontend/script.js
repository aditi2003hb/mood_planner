const baseURL = "http://127.0.0.1:8000";

const buttons = document.querySelectorAll(".mood-buttons button");
const quoteEl = document.getElementById("quote");
const suggestionEl = document.getElementById("suggestion");
const responseBox = document.getElementById("response-box");
const taskList = document.getElementById("task-list");

// Show mood response
buttons.forEach(btn => {
  btn.addEventListener("click", async () => {
    const mood = btn.getAttribute("data-mood");

    const res = await fetch(`${baseURL}/mood`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mood })
    });

    const data = await res.json();
    quoteEl.textContent = data.quote;
    suggestionEl.textContent = data.suggestion;
    responseBox.classList.remove("hidden");

    loadTasks();
  });
});

// Load all tasks
async function loadTasks() {
  const res = await fetch(`${baseURL}/tasks`);
  const tasks = await res.json();
  taskList.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = task.is_completed ? "completed" : "";

    li.innerHTML = `
      <span>${task.suggestion}</span>
      <div class="task-actions">
        ${!task.is_completed ? `<button onclick="completeTask(${task.id})">✅</button>` : ""}
        <button onclick="deleteTask(${task.id})">🗑️</button>
      </div>
    `;
    taskList.appendChild(li);
  });
}

async function completeTask(id) {
  await fetch(`${baseURL}/tasks/${id}`, { method: "PUT" });
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`${baseURL}/tasks/${id}`, { method: "DELETE" });
  loadTasks();
}

// Load all tasks initially
loadTasks();
