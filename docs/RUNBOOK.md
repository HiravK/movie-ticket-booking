# Operations Runbook — Movie Ticket Booking (Flask + SQLite)

| Field | Value |
|---|---|
| Document ID | MTB-RUNBOOK |
| Project | Movie Ticket Booking (Flask + SQLite) |
| Repository | [`HiravK/movie-ticket-booking`](https://github.com/HiravK/movie-ticket-booking) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Step-by-step instructions to set up, deploy, operate, monitor, recover and support the system.


## 1. Service overview

| Item | Detail |
|---|---|
| Service | Movie Ticket Booking (Flask + SQLite) |
| Hosting | Not deployed — runs locally |
| Live URL | — |
| Owner / on-call | Hirav Kadikar |
| Criticality | Low — non-revenue critical |
| Target availability | Best effort (no contractual SLA) |


## 2. Environments

| Environment | Where | Notes |
|---|---|---|
| Local | http://127.0.0.1:5000 | Flask dev server |


## 3. Local setup


### Prerequisites

- Python 3.9+


### Steps

```bash
git clone https://github.com/HiravK/movie-ticket-booking.git
cd movie-ticket-booking
pip install flask
python app.py        # http://127.0.0.1:5000 (creates booking.db)
```


## 4. Configuration and secrets

No configuration required.


## 5. Build and release

_Not deployed._


## 6. Rollback

1. Revert the offending commit on the default branch (`git revert <sha>`) and push; the host redeploys the previous good state.
1. If the host keeps previous deployments (e.g. Vercel/Netlify), promote the last good deployment from the dashboard for an instant rollback.


## 7. Monitoring and logging

No monitoring is configured. Minimum recommendation: an uptime check on the live URL and error alerts from the host.


## 8. Backup and disaster recovery

Source code is the only asset and is backed up by GitHub. Re-deploying from the default branch fully restores the service.

| Metric | Target |
|---|---|
| RPO (max data loss) | 0 — code is in Git |
| RTO (max downtime) | < 1 hour — redeploy from Git |


## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| All seats booked | Previous demo runs | Delete booking.db and restart |


## 10. Incident response

1. **Detect** — alert, user report or failed check.
1. **Triage** — confirm impact; classify: SEV1 (site down / data exposed), SEV2 (major feature broken), SEV3 (minor).
1. **Mitigate** — roll back (section 6) before debugging if users are affected.
1. **Fix** — reproduce locally, patch on a branch, test, deploy.
1. **Review** — write a short blameless post-mortem: timeline, root cause, actions; add new risks to the risk register.


## 11. Routine maintenance

- Monthly: update dependencies and re-run the test plan.
- Quarterly: rotate secrets and review access.
- Per release: update CHANGELOG.md and the session handover.
