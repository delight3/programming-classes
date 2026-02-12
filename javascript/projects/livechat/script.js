const chatArea = document.getElementById("chatArea");
const input = document.getElementById("customerInput");
const sendBtn = document.getElementById("sendCustomer");

let typingIndicator = null;

// Get time
function getTime() {
  const d = new Date();
  return d.getHours() + ":" + String(d.getMinutes()).padStart(2, "0");
}

// Show message
function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = sender;

  msg.innerHTML = `
    ${text}
    <div class="time">${getTime()}</div>
  `;

  chatArea.appendChild(msg);
  chatArea.scrollTop = chatArea.scrollHeight;
}

// Typing indicator
input.addEventListener("input", () => {
  if (!typingIndicator) {
    typingIndicator = document.createElement("div");
    typingIndicator.className = "typing";
    typingIndicator.textContent = "Customer is typing...";
    chatArea.appendChild(typingIndicator);
  }

  clearTimeout(input.typingTimer);
  input.typingTimer = setTimeout(() => {
    typingIndicator?.remove();
    typingIndicator = null;
  }, 1000);
});

// Send customer message
sendBtn.addEventListener("click", () => {
  if (input.value.trim() === "") return;

  addMessage(input.value, "customer");
  input.value = "";

  typingIndicator?.remove();
  typingIndicator = null;

  // Simulated bank response
  setTimeout(() => {
    showSupportTyping();
  }, 500);
});

// Support typing indicator
function showSupportTyping() {
  const typing = document.createElement("div");
  typing.className = "typing";
  typing.textContent = "Bank support is typing...";
  chatArea.appendChild(typing);

  setTimeout(() => {
    typing.remove();
    addMessage("Thank you for contacting Keeper Bank. How can I help you today?", "care");
  }, 1500);
}
