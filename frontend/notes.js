const userId = localStorage.getItem("user_id");

async function createNote() {
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    await fetch("http://localhost:8080/api/note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content, user_id: userId }),
    });

    loadNotes();
}

async function loadNotes() {
    const res = await fetch(`http://localhost:8080/api/notes/${userId}`);
    const notes = await res.json();

    const list = document.getElementById("notes-list");
    list.innerHTML = "";

    for (const note of notes) {
        const li = document.createElement("li");
        li.innerHTML = `
      <strong>${note.title}</strong>: ${note.content}<br>
      <em>Taguri:</em> <span id="tags-${note._id}">...</span><br>
      <input type="text" id="tag-input-${note._id}" placeholder="Adaugă tag">
      <button onclick="addTag('${note._id}')">Adaugă tag</button>
    `;

        list.appendChild(li);
        loadTags(note._id);
    }
}
async function loadTags(noteId) {
    const res = await fetch(`http://localhost:8080/api/tags/${noteId}`);
    const tags = await res.json();

    const tagSpan = document.getElementById(`tags-${noteId}`);
    tagSpan.textContent = tags.map(tag => tag.tag).join(", ");
}

async function addTag(noteId) {
    const input = document.getElementById(`tag-input-${noteId}`);
    const tagValue = input.value;

    await fetch("http://localhost:8080/api/tag", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ note_id: noteId, tag: tagValue }),
    });

    input.value = "";
    loadTags(noteId);
}


