async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch("http://localhost:8080/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    const data = await res.json();

    if (res.ok && data.user_id) {
        localStorage.setItem("user_id", data.user_id);
        window.location.href = "notes.html";
    } else {
        alert("Autentificare eșuată");
    }
}
