let passwordEl = document.getElementById("password");
let lengthEl = document.getElementById("length");
let uppercaseEl = document.getElementById("uppercase");
let lowercaseEl = document.getElementById("lowercase");
let numbersEl = document.getElementById("numbers");
let symbolsEl = document.getElementById("symbols");

const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lower = "abcdefghijklmnopqrstuvwxyz";
const numbers = "0123456789";
const symbols = "!@#$%^&*()_+{}[]<>?/";

function generatePassword() {
  let chars = "";
  let password = "";

  if (uppercaseEl.checked) chars += upper;
  if (lowercaseEl.checked) chars += lower;
  if (numbersEl.checked) chars += numbers;
  if (symbolsEl.checked) chars += symbols;

  if (chars === "") {
    alert("Select at least one character type");
    return;
  }

  for (let i = 0; i < lengthEl.value; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }

  passwordEl.value = password;
}

function copyPassword() {
  if (!passwordEl.value) return;

  navigator.clipboard.writeText(passwordEl.value);
  alert("Password copied to clipboard!");
}
