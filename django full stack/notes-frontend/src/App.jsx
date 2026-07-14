import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [accessToken, setAccessToken] = useState("");
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");

  async function login(event) {
    event.preventDefault();

    const response = await fetch(`${API_URL}/api/token/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      setMessage("Login failed.");
      return;
    }

    const data = await response.json();
    setAccessToken(data.access);
    setMessage("Logged in.");
  }

  async function loadNotes() {
    const response = await fetch(`${API_URL}/api/notes/`, {
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    setNotes(await response.json());
  }

  async function addNote(event) {
    event.preventDefault();

    await fetch(`${API_URL}/api/notes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ title, content }),
    });

    setTitle("");
    setContent("");
    loadNotes();
  }

  if (!accessToken) {
    return (
      <main>
        <h1>Notes</h1>
        <form onSubmit={login}>
          <input placeholder="Username" value={username}
            onChange={(e) => setUsername(e.target.value)} />
          <input type="password" placeholder="Password" value={password}
            onChange={(e) => setPassword(e.target.value)} />
          <button>Log in</button>
        </form>
        <p>{message}</p>
      </main>
    );
  }

  return (
    <main>
      <h1>My Notes</h1>
      <button onClick={loadNotes}>Load notes</button>

      <form onSubmit={addNote}>
        <input placeholder="Title" value={title}
          onChange={(e) => setTitle(e.target.value)} />
        <textarea placeholder="Content" value={content}
          onChange={(e) => setContent(e.target.value)} />
        <button>Add note</button>
      </form>

      {notes.map((note) => (
        <article key={note.id}>
          <h2>{note.title}</h2>
          <p>{note.content}</p>
        </article>
      ))}
    </main>
  );
}