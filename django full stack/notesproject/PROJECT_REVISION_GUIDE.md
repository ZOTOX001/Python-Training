# Notes Project: Django, React, Flask, PostgreSQL, and Git

This guide is a practical revision path for this project. Complete the sections in order. Do not run the Django server and Flask server on the same port.

## 1. What you have now

`notesproject` is a Django project. Django currently does two jobs:

1. It renders HTML pages such as the notes list and note form.
2. It exposes a protected JSON API for another frontend to use.

Important folders:

```text
notesproject/
├── manage.py                 # Django commands start here
├── notes/                    # Django app: model, views, API, templates
│   ├── models.py              # Note database model
│   ├── views.py               # HTML page views
│   ├── api_views.py           # JSON API view set
│   ├── serializers.py         # Model -> JSON rules
│   ├── urls.py                # HTML page routes
│   ├── api_urls.py            # API routes
│   ├── templates/notes/       # page-specific HTML
│   └── static/notes/style.css # CSS
├── templates/base.html        # shared HTML layout
├── notesproject/settings.py   # settings, apps, database, API auth
└── notesproject/urls.py       # top-level routes
```

Current endpoints:

| URL | Purpose |
| --- | --- |
| `/` | Django-rendered notes page |
| `/api/token/` | Login endpoint; returns JWT tokens |
| `/api/token/refresh/` | Gets a new access token from a refresh token |
| `/api/notes/` | Protected JSON list/create endpoint |
| `/api/notes/<id>/` | Protected JSON detail/update/delete endpoint |

`NoteViewSet` requires a JWT token. It returns only notes whose `owner` is the signed-in user. The `owner` field is set automatically when a note is created through the API.

## 2. Start and test the Django API first

Work in the folder that contains `manage.py`.

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack/notesproject"
source venv/bin/activate
python manage.py runserver
```

Leave this terminal running. In a second terminal, activate the same environment and create a user if you do not already have one:

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack/notesproject"
source venv/bin/activate
python manage.py createsuperuser
```

Get a token. Replace the username and password with the user you created:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"YOUR_USERNAME","password":"YOUR_PASSWORD"}'
```

Copy the value of `access`, then test the API:

```bash
curl http://127.0.0.1:8000/api/notes/ \
  -H "Authorization: Bearer PASTE_ACCESS_TOKEN_HERE"
```

Create a note through the API:

```bash
curl -X POST http://127.0.0.1:8000/api/notes/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer PASTE_ACCESS_TOKEN_HERE" \
  -d '{"title":"API note","content":"Created with curl"}'
```

Expected learning:

- `curl` is an API client.
- The browser HTML page and the JSON API are two different interfaces to the backend.
- `401 Unauthorized` means the token is missing, expired, or invalid.

## 3. Allow React to call Django during development

React runs on a different development origin (`http://localhost:5173`), so Django must allow it with CORS.

Stop the Django server with `Ctrl+C`, then install the CORS package inside the Django virtual environment:

```bash
python -m pip install django-cors-headers
```

In `notesproject/settings.py`, add this entry near the other installed apps:

```python
INSTALLED_APPS = [
    # existing apps...
    "corsheaders",
]
```

Add the middleware near the top. It must be before `CommonMiddleware`:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # existing middleware...
]
```

Below your REST settings, add:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
```

Start Django again:

```bash
python manage.py runserver
```

For development, CORS lets only your local React dev server call this API. Do not use `CORS_ALLOW_ALL_ORIGINS = True` in a real deployed application.

## 4. Create the React frontend

Keep React as a sibling folder, not inside the Django app:

```text
django full stack/
├── notesproject/    # Django backend
└── notes-frontend/  # React frontend
```

First confirm Node and npm are installed:

```bash
node --version
npm --version
```

Vite currently requires Node.js 20.19+ or 22.12+. Create React with Vite:

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack"
npm create vite@latest notes-frontend -- --template react
cd notes-frontend
npm install
npm run dev
```

Open the URL shown by Vite, normally `http://localhost:5173`.

### Replace `src/App.jsx`

This small frontend proves the React + Django API connection. It logs in, lists the signed-in user's notes, and creates a new note.

```jsx
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
    setMessage("");

    const response = await fetch(`${API_URL}/api/token/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      setMessage("Login failed. Check the username and password.");
      return;
    }

    const data = await response.json();
    setAccessToken(data.access);
    setMessage("Logged in. Load your notes.");
  }

  async function loadNotes() {
    const response = await fetch(`${API_URL}/api/notes/`, {
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    if (!response.ok) {
      setMessage("Could not load notes. Log in again if the token expired.");
      return;
    }

    setNotes(await response.json());
  }

  async function addNote(event) {
    event.preventDefault();

    const response = await fetch(`${API_URL}/api/notes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ title, content }),
    });

    if (!response.ok) {
      setMessage("Could not create the note.");
      return;
    }

    setTitle("");
    setContent("");
    setMessage("Note created.");
    loadNotes();
  }

  if (!accessToken) {
    return (
      <main>
        <h1>Notes React Client</h1>
        <form onSubmit={login}>
          <input
            placeholder="Username"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
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
        <input
          placeholder="Title"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={(event) => setContent(event.target.value)}
        />
        <button>Add note</button>
      </form>

      <p>{message}</p>
      {notes.map((note) => (
        <article key={note.id}>
          <h2>{note.title}</h2>
          <p>{note.content}</p>
        </article>
      ))}
    </main>
  );
}
```

### Replace `src/App.css`

```css
main {
  font-family: Arial, sans-serif;
  max-width: 700px;
  margin: 40px auto;
}

form {
  display: grid;
  gap: 10px;
  margin: 20px 0;
}

input, textarea, button {
  font: inherit;
  padding: 10px;
}

article {
  background: #f3f6fb;
  border-radius: 8px;
  margin: 12px 0;
  padding: 12px;
}
```

### Run both applications

Use two terminals:

```bash
# terminal 1: Django
cd "/Users/aniketsingh/Desktop/python/django full stack/notesproject"
source venv/bin/activate
python manage.py runserver
```

```bash
# terminal 2: React
cd "/Users/aniketsingh/Desktop/python/django full stack/notes-frontend"
npm run dev
```

Log in to React with the same Django user. Then click **Load notes** and create a note.

What React adds:

- React owns the browser UI and state (`useState`).
- `fetch()` calls Django's JSON API.
- Django owns database access, permissions, and JWT authentication.
- React does not import Django models or directly access the database.

For this learning project, the access token stays only in React state, so a page refresh logs you out. Do not put passwords in source code. A production authentication design needs additional security decisions, including token storage and refresh handling.

## 5. Build a separate Flask API for comparison

Do this only after the React + Django API works. This is a separate, deliberately small project; it does not replace your Django backend.

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack"
mkdir flask-notes-api
cd flask-notes-api
python3 -m venv venv
source venv/bin/activate
python -m pip install Flask flask-cors
```

Create `app.py`:

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

notes = []


@app.get("/api/notes")
def list_notes():
    return jsonify(notes)


@app.post("/api/notes")
def create_note():
    data = request.get_json()
    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"],
    }
    notes.append(note)
    return jsonify(note), 201
```

Run it:

```bash
flask --app app run --debug
```

Test it in a second terminal:

```bash
curl http://127.0.0.1:5000/api/notes

curl -X POST http://127.0.0.1:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"Flask note","content":"Saved only in memory"}'
```

Comparison:

| Django REST API | Flask API exercise |
| --- | --- |
| Models, migrations, admin, users, JWT available | You write each part yourself when needed |
| Notes saved in a database | Notes disappear when Flask restarts |
| Router/viewset creates REST routes | Decorators define routes directly |
| Best for understanding a full structured backend | Best for understanding HTTP basics and minimal APIs |

Do not point the React JWT app at the Flask API yet. Flask has no token endpoint or database in this exercise. First understand each backend independently. Later, you can adapt React's API URL to `http://127.0.0.1:5000` and remove the login/token code to test the basic Flask list/create calls.

## 6. Move Django from SQLite to local PostgreSQL

Do this after the Django API works. Make a backup before changing databases.

### 6.1 Install and start PostgreSQL

Install a local PostgreSQL server using a trusted package manager or the PostgreSQL installer. Django 5.2 supports PostgreSQL 14+ and recommends the modern `psycopg` driver.

Confirm the command is available:

```bash
psql --version
```

Start the local PostgreSQL service using the method provided by your installer. Then create a database user and database:

```bash
createuser --interactive --pwprompt notes_user
createdb -O notes_user notes_db
```

Choose a password when prompted. If the commands say the role already exists, use the existing role or choose another name.

### 6.2 Install the Django database driver

Inside the Django virtual environment:

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack/notesproject"
source venv/bin/activate
python -m pip install "psycopg[binary]"
```

### 6.3 Keep secrets out of `settings.py`

Create a file named `.env` beside `manage.py`:

```text
POSTGRES_DB=notes_db
POSTGRES_USER=notes_user
POSTGRES_PASSWORD=YOUR_DATABASE_PASSWORD
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

For the first local exercise, you may temporarily write these values directly in `settings.py`. For a proper `.env` setup, install `python-dotenv` or use environment variables. Never commit `.env` to GitHub.

Replace the SQLite `DATABASES` setting in `notesproject/settings.py` with this configuration (substitute your values):

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "notes_db",
        "USER": "notes_user",
        "PASSWORD": "YOUR_DATABASE_PASSWORD",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

### 6.4 Create the schema in PostgreSQL

For a fresh local database, run:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 6.5 Optional: copy existing SQLite data

Only do this if you want to retain your current users and notes.

1. While `settings.py` still points to SQLite, export data:

   ```bash
   python manage.py dumpdata --natural-foreign --natural-primary \
     -e contenttypes -e auth.Permission > sqlite_backup.json
   ```

2. Change `DATABASES` to PostgreSQL.
3. Run `python manage.py migrate`.
4. Load the data:

   ```bash
   python manage.py loaddata sqlite_backup.json
   ```

5. Check the project:

   ```bash
   python manage.py check
   ```

Keep `db.sqlite3` as a backup until you verify your PostgreSQL data. Do not commit the backup JSON file if it contains real user data.

## 7. Requirements files

With the correct virtual environment activated, save the exact Python packages for Django:

```bash
cd "/Users/aniketsingh/Desktop/python/django full stack/notesproject"
source venv/bin/activate
python -m pip freeze > requirements.txt
```

Run it again after adding or upgrading any Python package.

For another computer:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

React does not use `requirements.txt`. Its dependencies are recorded in `package.json` and `package-lock.json`; restore them with:

```bash
npm install
```

## 8. GitHub: ignore environments and local secrets

Create `.gitignore` beside Django's `manage.py`:

```gitignore
# Python
venv/
.venv/
__pycache__/
*.py[cod]

# Django local/generated files
db.sqlite3
sqlite_backup.json
.env
staticfiles/

# React
node_modules/
dist/
.env.local

# Editor/OS
.DS_Store
.vscode/
```

If `venv` was already added to Git, remove it from Git's index without deleting the local folder:

```bash
git rm -r --cached venv
```

Then check what will be committed:

```bash
git status
```

You should commit source files, migrations, `requirements.txt`, `package.json`, `package-lock.json`, and `.gitignore`. Do not commit `venv`, `.env`, `node_modules`, or database backups containing real data.

## 9. Interview revision checklist

Be able to explain these statements in your own words:

- A Django **project** contains configuration; a Django **app** contains one feature area.
- `models.py` describes database tables; migrations apply model changes to the database.
- A serializer converts validated model data to and from JSON.
- A viewset groups CRUD operations; a router creates URL patterns for it.
- JWT login returns an access token; protected requests send it as `Authorization: Bearer <token>`.
- Authentication identifies the user; permissions decide whether the user may perform an action.
- `perform_create()` assigns `request.user` as the owner, preventing clients from choosing another user as owner.
- Django templates are server-rendered HTML. React renders UI in the browser and calls APIs using HTTP.
- CORS is a browser policy controlling which frontend origins can call a backend from browser JavaScript.
- SQLite is a local file database. PostgreSQL is a separate database server and is better suited to multi-user production-style systems.
- A virtual environment isolates Python packages per project; `requirements.txt` records those package versions.

## Official references

- Vite React setup: https://vite.dev/guide/
- Django database configuration: https://docs.djangoproject.com/en/5.2/ref/databases/
- Simple JWT setup: https://django-rest-framework-simplejwt.readthedocs.io/en/stable/getting_started.html
- Flask installation: https://flask.palletsprojects.com/en/stable/installation/
- Flask quickstart: https://flask.palletsprojects.com/en/stable/quickstart/
