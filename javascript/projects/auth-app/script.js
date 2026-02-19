// Fake JWT generator (for demo)
function generateJWT(user) {
  const header = btoa(JSON.stringify({ alg: "HS256", typ: "JWT" }));
  const payload = btoa(JSON.stringify({
    user,
    exp: Date.now() + 60 * 60 * 1000 // 1 hour
  }));
  const signature = btoa("fake-signature");

  return `${header}.${payload}.${signature}`;
}

// Register user
function register() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (!username || !password) {
    showMessage("Fill all fields");
    return;
  }

  const users = JSON.parse(localStorage.getItem("users")) || [];
  users.push({ username, password });
  localStorage.setItem("users", JSON.stringify(users));

  showMessage("Registered successfully");
}

// Login user
function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const users = JSON.parse(localStorage.getItem("users")) || [];
  const user = users.find(u => u.username === username && u.password === password);

  if (!user) {
    showMessage("Invalid credentials");
    return;
  }

  const token = generateJWT(username);
  localStorage.setItem("token", token);

  window.location.href = "dashboard.html";
}

// Protect dashboard
function checkAuth() {
  const token = localStorage.getItem("token");

  if (!token) {
    window.location.href = "index.html";
    return;
  }

  const payload = JSON.parse(atob(token.split(".")[1]));
  if (payload.exp < Date.now()) {
    logout();
  }
}

// Logout
function logout() {
  localStorage.removeItem("token");
  window.location.href = "index.html";
}

// Message display
function showMessage(msg) {
  document.getElementById("message").innerText = msg;
}

// Auto-check auth on dashboard
if (window.location.pathname.includes("dashboard")) {
  checkAuth();
}
