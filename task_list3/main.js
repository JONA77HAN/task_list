document.addEventListener("DOMContentLoaded", function() {
    const taskList = document.getElementById("task-list");
    const taskInput = document.getElementById("task-input");
    const addBtn = document.getElementById("add-btn");

    // Function to create a new task item
    function createTaskItem(taskContent) {
        const li = document.createElement("li");
        li.textContent = taskContent;
        
        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.classList.add("delete-btn");
        deleteBtn.addEventListener("click", function() {
            li.remove();
        });
        
        li.appendChild(deleteBtn);
        return li;
    }

    // Function to add a new task to the list
    function addTask() {
        const taskContent = taskInput.value.trim();
        if (taskContent !== "") {
            const taskItem = createTaskItem(taskContent);
            taskList.appendChild(taskItem);
            taskInput.value = "";
        }
    }

    // Event listener for the add button
    addBtn.addEventListener("click", addTask);

    // Event listener for pressing Enter in the input field
    taskInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            addTask();
        }
    });
});
