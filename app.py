from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
DB_PATH = os.path.join(os.path.dirname(__file__), "booking.db")

# --- Database Setup ---
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Create movies table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            genre TEXT,
            duration TEXT
        )
        """)

        # Create seats table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS seats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            seat_number TEXT,
            status TEXT DEFAULT 'available',
            FOREIGN KEY(movie_id) REFERENCES movies(id)
        )
        """)

        # Create bookings table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            seat_number TEXT,
            username TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(movie_id) REFERENCES movies(id)
        )
        """)

def seed_data():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM movies")
        if cur.fetchone()[0] == 0:
            # Add 3 movies
            movies = [
                ("Inception", "Sci-Fi", "2h 28m"),
                ("Avengers: Endgame", "Action", "3h 2m"),
                ("Interstellar", "Sci-Fi", "2h 49m"),
            ]
            cur.executemany("INSERT INTO movies (title, genre, duration) VALUES (?, ?, ?)", movies)
            conn.commit()
            # Add 20 seats per movie (A1-E4)
            cur.execute("SELECT id FROM movies")
            movie_ids = [row[0] for row in cur.fetchall()]
            for movie_id in movie_ids:
                seats = [(movie_id, f"{chr(65+r)}{s+1}") for r in range(4) for s in range(5)]
                cur.executemany("INSERT INTO seats (movie_id, seat_number) VALUES (?, ?)", seats)
            conn.commit()

# Initialize DB and seed data on start
init_db()
seed_data()

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-movies")
def get_movies():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, title FROM movies")
        movies = cur.fetchall()
    return jsonify([{"id": m[0], "title": m[1]} for m in movies])

@app.route("/get-seats/<int:movie_id>")
def get_seats(movie_id):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT seat_number, status FROM seats WHERE movie_id=?", (movie_id,))
        seats = cur.fetchall()
    return jsonify(seats)

@app.route("/book", methods=["POST"])
def book_seat():
    data = request.json
    movie_id = data.get("movie_id")
    seat_numbers = data.get("seat_number")  # can be a single string or a list
    username = data.get("username", "Guest")

    if isinstance(seat_numbers, str):
        seat_numbers = [seat_numbers]

    booked_seats = []
    failed_seats = []

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for seat in seat_numbers:
            cur.execute("SELECT status FROM seats WHERE movie_id=? AND seat_number=?", (movie_id, seat))
            seat_row = cur.fetchone()
            if seat_row and seat_row[0] == "available":
                cur.execute("UPDATE seats SET status='booked' WHERE movie_id=? AND seat_number=?", (movie_id, seat))
                cur.execute("INSERT INTO bookings (movie_id, seat_number, username) VALUES (?, ?, ?)", (movie_id, seat, username))
                booked_seats.append(seat)
            else:
                failed_seats.append(seat)
        conn.commit()

    if failed_seats:
        return jsonify({"success": False, "message": f"Some seats could not be booked: {', '.join(failed_seats)}", "booked": booked_seats}), 400
    return jsonify({"success": True, "message": f"Seats booked successfully: {', '.join(booked_seats)}"})

if __name__ == "__main__":
    app.run(debug=True)