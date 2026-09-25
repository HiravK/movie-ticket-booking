# Product Requirements Document (PRD) — Movie Ticket Booking (Flask + SQLite)

| Field | Value |
|---|---|
| Document ID | MTB-PRD |
| Project | Movie Ticket Booking (Flask + SQLite) |
| Repository | [`HiravK/movie-ticket-booking`](https://github.com/HiravK/movie-ticket-booking) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Defines what the product must do, for whom, and how success is measured. It is the single source of truth for scope.


## 1. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-09-25 | Hirav Kadikar | Full documentation suite generated from a complete review of the repository. |


## 2. Executive summary

**movie-ticket-booking** is a beginner full-stack project. On start, `app.py` creates a SQLite database (`booking.db`)
with `movies`, `seats` and `bookings` tables and seeds three films (Inception, Avengers: Endgame, Interstellar) with 20
seats each (A1–D5). The home page loads movies from `/get-movies`; choosing one shows a seat map from
`/get-seats/<id>`; selecting seats updates a count and total at ₹150 per seat; **Book Now** posts to `/book`, which marks
available seats as booked and records each booking. Already-booked seats are reported back as failures.


## 3. Problem statement

Learners need a compact example that connects a front-end seat map to a back-end API and a database.


## 4. Goals and non-goals


### 4.1 Goals

- Show a complete select-seats → book flow with persistence.
- Keep the code small enough to read in one sitting.


### 4.2 Non-goals (explicitly out of scope)

- Payments, user accounts, showtimes, real cinemas.


## 5. Stakeholders (RACI)

| Stakeholder | Role | R/A/C/I | Interest |
|---|---|---|---|
| Hirav Kadikar | Developer | R/A | Learning Flask and SQLite |


_R = Responsible, A = Accountable, C = Consulted, I = Informed._


## 6. Users and personas


### Moviegoer (demo)

**Needs:**
- See movies
- Pick seats
- Confirm booking


## 7. User stories

| ID | As a… | I want to… | So that… | Priority |
|---|---|---|---|---|
| US-01 | moviegoer | to see available movies | I can choose one | Must |
| US-02 | moviegoer | to pick seats on a map | I sit where I want | Must |
| US-03 | moviegoer | to see the total price | I know the cost | Should |
| US-04 | moviegoer | to be told if a seat is taken | I pick another | Must |


## 8. Functional requirements

| ID | Area | Requirement | MoSCoW | Status |
|---|---|---|---|---|
| FR-01 | Data | Create and seed SQLite tables | Must | Done |
| FR-02 | API | List movies and seats | Must | Done |
| FR-03 | Booking | Book available seats; reject booked ones | Must | Done |
| FR-04 | Users | Real user names | Could | Not done — username is hard-coded "Hirav" in script.js |
| FR-05 | Concurrency | Prevent two users booking the same seat at the same time | Should | Partly — check-then-update is not atomic |


## 9. Non-functional requirements

| ID | Category | Requirement | Current status |
|---|---|---|---|
| NFR-01 | Simplicity | Single Flask file | Met |
| NFR-02 | Consistency | No double bookings | Partly met |
| NFR-03 | Security | Debug off outside development | Not met — debug=True |


## 10. User experience and key flows


### Book seats

1. Open http://127.0.0.1:5000
1. Pick a movie
1. Click seats (count and total update)
1. Click Book Now → alert shows success or which seats failed


## 11. Success metrics (KPIs)

| Metric | Target | How it is measured |
|---|---|---|
| Double bookings | 0 | bookings table vs seats |


## 12. Assumptions, constraints and dependencies


### Assumptions

_None recorded._


### Constraints

_None recorded._


### External dependencies

| Dependency | Used for | Risk if unavailable |
|---|---|---|
| Flask | Web server | — |
| SQLite | Storage | Single-writer database |


## 13. Release plan and roadmap

| Phase | Scope | Status |
|---|---|---|
| v1 (2025-09-06) | Movies, seats, booking | Done |
| v2 | Username input, atomic booking, cancel booking | Proposed |


## 14. Open questions

_None open._


## 15. Acceptance and sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Product owner | Hirav Kadikar | Approved (baseline of current build) | 2026-09-25 |
