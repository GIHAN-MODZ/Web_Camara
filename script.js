// Existing login function remains...
function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const error = document.getElementById("error");

  if (username === "Gihan" && password === "12345") {
    window.location.href = "https://www.google.com";
  } else {
    error.textContent = "Invalid Username or Password!";
  }
}
//
