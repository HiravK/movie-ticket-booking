const moviesContainer = document.getElementById("movies-container");
const bookingSection = document.getElementById("booking-section");
const seatMapContainer = document.getElementById("seat-map");
const movieTitle = document.getElementById("movie-title");
const countEl = document.getElementById("count");
const totalEl = document.getElementById("total");
const bookBtn = document.getElementById("book-btn");

let selectedSeats = [];
let currentMovieId = null;
const seatPrice = 150;

// Load movies from backend
async function loadMovies() {
  try {
    const res = await fetch("/get-movies");
    const movies = await res.json();

    moviesContainer.innerHTML = "";
    movies.forEach(movie => {
      const card = document.createElement("div");
      card.classList.add("movie-card");

      card.innerHTML = `
        <h3>${movie.title}</h3>
        <button class="book-btn" data-id="${movie.id}">Book Seats</button>
      `;

      moviesContainer.appendChild(card);

      card.querySelector(".book-btn").addEventListener("click", () => {
        currentMovieId = movie.id;
        movieTitle.textContent = movie.title;
        bookingSection.style.display = "block";
        loadSeats(movie.id);
      });
    });
  } catch (err) {
    console.error("Error loading movies:", err);
  }
}

// Load seats for selected movie
async function loadSeats(movieId) {
  try {
    const res = await fetch(`/get-seats/${movieId}`);
    const seats = await res.json();

    seatMapContainer.innerHTML = "";
    selectedSeats = [];
    countEl.textContent = 0;
    totalEl.textContent = 0;

    // Group seats by rows dynamically (5 seats per row)
    const seatsPerRow = 5;
    for (let i = 0; i < seats.length; i += seatsPerRow) {
      const rowDiv = document.createElement("div");
      rowDiv.classList.add("row");

      const rowSeats = seats.slice(i, i + seatsPerRow);
      rowSeats.forEach(seatData => {
        const seatDiv = document.createElement("div");
        seatDiv.classList.add("seat");
        seatDiv.dataset.seat = seatData[0];
        seatDiv.textContent = seatData[0];

        if (seatData[1] === "booked") seatDiv.classList.add("booked");

        seatDiv.addEventListener("click", () => toggleSeat(seatDiv));
        rowDiv.appendChild(seatDiv);
      });

      seatMapContainer.appendChild(rowDiv);
    }
  } catch (err) {
    console.error("Error loading seats:", err);
  }
}

function toggleSeat(seatDiv) {
  if (seatDiv.classList.contains("booked")) return;
  seatDiv.classList.toggle("selected");
  const seatNum = seatDiv.dataset.seat;

  if (seatDiv.classList.contains("selected")) {
    selectedSeats.push(seatNum);
  } else {
    selectedSeats = selectedSeats.filter(s => s !== seatNum);
  }

  countEl.textContent = selectedSeats.length;
  totalEl.textContent = selectedSeats.length * seatPrice;
}

bookBtn.addEventListener("click", async () => {
  if (!selectedSeats.length) return alert("Please select at least one seat.");

  try {
    const res = await fetch("/book", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ movie_id: currentMovieId, seat_number: selectedSeats, username: "Hirav" })
    });
    const data = await res.json();

    if (data.success) {
      alert(`Seats booked successfully: ${selectedSeats.join(", ")}`);
    } else {
      alert(`Failed to book seats: ${data.message}`);
    }

    loadSeats(currentMovieId);
  } catch (err) {
    console.error("Error booking seats:", err);
  }
});

loadMovies();