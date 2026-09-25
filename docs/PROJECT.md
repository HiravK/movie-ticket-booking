# Project Overview (In Depth) — Movie Ticket Booking (Flask + SQLite)

| Field | Value |
|---|---|
| Document ID | MTB-PROJECT |
| Project | Movie Ticket Booking (Flask + SQLite) |
| Repository | [`HiravK/movie-ticket-booking`](https://github.com/HiravK/movie-ticket-booking) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** The complete, plain-English explanation of this project: why it exists, what it does, how every part works, how it evolved, its quality, security, risks and vocabulary.


## 1. The project in one paragraph

**movie-ticket-booking** is a beginner full-stack project. On start, `app.py` creates a SQLite database (`booking.db`)
with `movies`, `seats` and `bookings` tables and seeds three films (Inception, Avengers: Endgame, Interstellar) with 20
seats each (A1–D5). The home page loads movies from `/get-movies`; choosing one shows a seat map from
`/get-seats/<id>`; selecting seats updates a count and total at ₹150 per seat; **Book Now** posts to `/book`, which marks
available seats as booked and records each booking. Already-booked seats are reported back as failures.


## 2. Background and why it exists

Learners need a compact example that connects a front-end seat map to a back-end API and a database.


## 3. Fact sheet

|  |  |
|---|---|
| Repository | Public — `HiravK/movie-ticket-booking` |
| Status | Learning project (Sept 2025) — complete demo |
| Live URL | — |
| Hosting | Not deployed — runs locally |
| Primary language | Python + JavaScript |
| Default branch | `main` |
| History | 1 commits from 2025-09-06 to 2025-09-06 |
| Contributors | hiravk (1 commits) |


## 4. Features explained


### Auto database setup

Tables created and seeded on first run


### Movie list

GET /get-movies


### Seat map

GET /get-seats/<movie_id> returns seat numbers and status


### Booking

POST /book with movie_id, seat_number (string or list) and username; partial failures reported


### Pricing

₹150 per seat calculated in the browser


## 5. How it works end to end

One Flask app serves two templates and a JSON API; static JS drives the UI. SQLite (`booking.db`, git-ignored) is
opened per request with `sqlite3.connect`. Booking loops over requested seats, checks `status`, updates to `booked` and
inserts a booking row, then commits once.


### Book seats

1. Open http://127.0.0.1:5000
1. Pick a movie
1. Click seats (count and total update)
1. Click Book Now → alert shows success or which seats failed

Diagrams and component detail: [ARCHITECTURE.md](ARCHITECTURE.md).


## 6. Technology choices

| Layer | Technology | Why it is used |
|---|---|---|
| Backend | Python 3, Flask | Routes and API |
| Database | SQLite (sqlite3) | Storage |
| Frontend | HTML, CSS, vanilla JS | Seat map |


## 7. Codebase tour

```text
movie-ticket-booking/
├── app.py
├── templates/index.html, booking.html
├── static/script.js, style.css
└── README.md
```

| Component | Location | What it does |
|---|---|---|
| Flask app | `app.py` | DB init + seed, routes |
| Templates | `templates/index.html, templates/booking.html` | Pages |
| Front-end logic | `static/script.js` | Load movies/seats, selection, price, booking call |
| Styles | `static/style.css` | Layout |


## 8. Project timeline

| Phase | Scope | Status |
|---|---|---|
| v1 (2025-09-06) | Movies, seats, booking | Done |
| v2 | Username input, atomic booking, cancel booking | Proposed |

Recent commits:

```text
2025-09-06  Initial commit: Movie ticket booking system with Flask backend
```


## 9. Team and ownership

| Person / group | Role | Interest |
|---|---|---|
| Hirav Kadikar | Developer | Learning Flask and SQLite |


## Quality and testing

No automated tests.

Acceptance checks to run before every release:

| # | Area | Check | Expected result |
|---|---|---|---|
| 1 | Seed | First run | 3 movies, 20 seats each |
| 2 | Booking | Book A1 | Success; A1 shows booked |
| 3 | Booking | Book A1 again | Failure listing A1 |
| 4 | Reset | Delete booking.db and restart | Fresh seed |


## Security and privacy

| Area | Current state |
|---|---|
| Authentication | None — no user accounts. |
| Authorisation | Not applicable. |
| Data handled | Demo data only (usernames). |
| Secrets | No secrets required. |
| Transport | HTTPS via the hosting provider. |

| Threat | Scenario | Mitigation | Status |
|---|---|---|---|
| Tampering | Anyone books all seats via API | Auth/rate limit (out of scope for demo) | Accepted |
| Elevation of privilege | Flask debugger exposed | Disable debug | Open |


## Risks and technical debt

| ID | Category | Risk | Score (L×I) | Mitigation |
|---|---|---|---|---|
| R-01 | Quality | Double booking under concurrency | 4 (Low) | Atomic update |


## How to use it


### Book seats

1. Run the app and open http://127.0.0.1:5000
1. Choose a movie, click seats, press Book Now


## Glossary

| Term | Meaning |
|---|---|
| **Flask** | Python web framework |
| **Seat map** | Grid of seats showing available/booked |
| **SQLite** | File-based SQL database |
