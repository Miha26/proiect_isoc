// verifică dacă user-ul este logat, altfel redirectează
if (!localStorage.getItem("user_id")) {
    window.location.href = "login.html";
}

function logout() {
    localStorage.removeItem("user_id");
    window.location.href = "login.html";
}
