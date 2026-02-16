// Show/Hide password with rotation animation
function showPass(icon) {
    const password = document.getElementById("password");

    // Toggle password type
    if (password.type === "password") {
        password.type = "text";
        icon.classList.replace("fa-eye-slash", "fa-eye");
    } else {
        password.type = "password";
        icon.classList.replace("fa-eye", "fa-eye-slash");
    }

    // Animate eye icon
    icon.classList.add("animate");
    setTimeout(() => icon.classList.remove("animate"), 350);
}

// Dark mode toggle
function toggleTheme() {
    document.body.classList.toggle("dark");
}
