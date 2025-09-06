# Movie Ticket Booking System

This project is a web application for booking movie tickets. It allows users to view available movies, select seats, and complete the booking process. The application is built using Flask for the backend and utilizes SQLite for data storage.

## Project Structure

```
movie_ticket_booking
├── app.py               # Main application file that sets up the Flask web server and handles routing
├── booking.db           # SQLite database file that stores movies, seats, and bookings
├── templates
│   ├── index.html      # HTML structure for the home page displaying available movies
│   └── booking.html     # HTML structure for the booking page with seat selection
├── static
│   ├── style.css       # CSS styles for the application
│   └── script.js       # JavaScript code for dynamic interactions on the front end
└── README.md           # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd movie_ticket_booking
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then, install Flask:
   ```
   pip install Flask
   ```

3. **Initialize the database**:
   The database will be automatically created when you run the application for the first time.

4. **Run the application**:
   Execute the following command to start the Flask server:
   ```
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to view the list of available movies.
- Click the "Book Now" button for the desired movie to proceed to the booking page.
- Select your seats on the seat map and click "Book Now" to confirm your booking.
- A confirmation message will be displayed upon successful booking.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.