# book-review
## 📚 Book Review API

A Django-based Book Review system with REST API, Redis caching, unit testing, and real-time WebSocket support (via Django Channels).

---

### 🔧 Features

* 📖 Book listing and creation
* 📝 Review creation and listing
* ✅ Prevents duplicate reviews by the same reviewer
* ⚡ Redis caching for book listing
* 🧪 Unit and integration tests using Django's `APITestCase`
* 🔌 Optional WebSocket integration for real-time notifications using Django Channels
* 🐳 Docker-ready setup possible for Redis and RabbitMQ (if extended)

---

### 🚀 Technologies Used

* Python 3.x
* Django 5.x
* Django REST Framework
* Redis (for caching and Channels backend)
* Django Channels (for WebSocket support)
* SQLite (default) or PostgreSQL
* Unit testing (`APITestCase`)

---

### 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/book-review-api.git
cd book-review-api
```

2. **Create virtual environment**

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Redis (Required)**

Make sure Redis server is running:

```bash
# Windows (if installed)
redis-server
or
.\redis-server.exe (command)

# Linux/Mac
sudo service redis-server start
```

5. **Apply Migrations**

```bash
python manage.py migrate
```

6. **Run Server**

```bash
python manage.py runserver
```

---

### 🧪 Running Tests

```bash
python manage.py test
```

Test coverage includes:

* Creating a book
* Creating a review
* Preventing duplicate reviews
* Caching integration for book list

---

### 📱 WebSocket Setup (Optional)

If you're using WebSockets:

* Redis must be running
* `ASGI_APPLICATION` and `CHANNEL_LAYERS` are configured in `settings.py`
* Use browser console or JS client to test:

```javascript
const socket = new WebSocket("ws://localhost:8000/ws/reviews/");
socket.onmessage = (e) => console.log("Review Notification:", e.data);
```

---

### 📂 API Endpoints

| Method | Endpoint                    | Description            |
| ------ | --------------------------- | ---------------------- |
| `GET`  | `/books/`                   | List books             |
| `POST` | `/books/`                   | Add new book           |
| `GET`  | `/books/<book_id>/reviews/` | List reviews of a book |
| `POST` | `/books/<book_id>/reviews/` | Add review for a book  |

---

### 🔒 Authentication

* Currently **open** (no authentication)
* Easily extendable to token-based or session authentication 

---
