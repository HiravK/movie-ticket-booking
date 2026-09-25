# Session Handover — Movie Ticket Booking (Flask + SQLite)

| Field | Value |
|---|---|
| Document ID | MTB-HANDOVER |
| Project | Movie Ticket Booking (Flask + SQLite) |
| Repository | [`HiravK/movie-ticket-booking`](https://github.com/HiravK/movie-ticket-booking) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Lets the next person (or AI session) pick up the work cold: what exists, what state it is in, what is unfinished, and exactly what to do next.


## 1. Handover summary

| Item | Detail |
|---|---|
| Handover date | 2026-09-25 |
| Handed over by | Hirav Kadikar |
| Repository state | `main` @ `a0ba709` — 1 commits, last change 2025-09-06 |
| Overall status | Learning project (Sept 2025) — complete demo |
| Live URL | — |
| Health | Green — demo complete |


## 2. Current state (plain English)

A finished single-commit demo from 2025-09-06. No work in progress.


## 3. What is done

- Seeded database, seat map, booking API


## 4. In progress / partially done

- Nothing.


## 5. Known issues and bugs

| # | Issue | Impact | Suggested fix |
|---|---|---|---|
| 1 | Username hard-coded "Hirav" in script.js | All bookings under one name | Add a name field |
| 2 | Check-then-update is not atomic | Two simultaneous requests could double-book | `UPDATE seats SET status='booked' WHERE … AND status='available'` and check rowcount |
| 3 | debug=True | Unsafe if exposed | Disable |
| 4 | README claims MIT licence but no LICENSE file | Unclear licence | Add LICENSE |


## 6. Next steps (prioritised)

1. Add a name field and atomic booking; add cancel booking.


## 7. How to resume work in 10 minutes

```bash
git clone https://github.com/HiravK/movie-ticket-booking.git
cd movie-ticket-booking
pip install flask
python app.py        # http://127.0.0.1:5000 (creates booking.db)
```


## 8. Access, accounts and secrets

Secrets are **never** stored in this repository. The table lists where each credential lives, not its value.

| System | What you need | Where it lives |
|---|---|---|
| GitHub HiravK/movie-ticket-booking | Write | GitHub |


## 9. Gotchas and tribal knowledge

_None recorded._


## 10. Key files to read first

| File | Why |
|---|---|
| `app.py` | All back-end logic |
| `static/script.js` | All front-end logic |


## 11. Recent history

```text
2025-09-06  a0ba709  Initial commit: Movie ticket booking system with Flask backend
```


## 12. Handover checklist

- [ ] Repository builds from a clean clone using the README steps
- [ ] Environment variables documented in the README / runbook
- [ ] Open risks recorded in the risk register
- [ ] Next steps above agreed with the product owner
- [ ] Access to hosting / third-party accounts transferred or shared
