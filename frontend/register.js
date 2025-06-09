async function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch("http://localhost:8080/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    if (res.ok) {
        alert("Înregistrare reușită! Mergi la login.");
        window.location.href = "login.html";
    } else {
        alert("Eroare la înregistrare");
    }
}
