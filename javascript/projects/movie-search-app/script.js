const API_KEY = "your OMDb API key"; 
const moviesEl = document.getElementById("movies");

function searchMovie() {
  const query = document.getElementById("search").value.trim();

  if (query === "") {
    alert("Enter a movie name");
    return;
  }

  moviesEl.innerHTML = "Loading...";

  fetch(`https://www.omdbapi.com/?s=${query}&apikey=${API_KEY}`)
    .then(res => res.json())
    .then(data => {
      if (data.Response === "False") {
        moviesEl.innerHTML = "No movies found.";
        return;
      }

      moviesEl.innerHTML = "";
      data.Search.forEach(movie => fetchMovieDetails(movie.imdbID));
    })
    .catch(() => {
      moviesEl.innerHTML = "Error fetching movies.";
    });
}

function fetchMovieDetails(id) {
  fetch(`https://www.omdbapi.com/?i=${id}&apikey=${API_KEY}`)
    .then(res => res.json())
    .then(movie => {
      const div = document.createElement("div");
      div.classList.add("movie");

      div.innerHTML = `
        <img src="${movie.Poster !== "N/A" ? movie.Poster : 'https://via.placeholder.com/300'}">
        <h4>${movie.Title}</h4>
        <p>${movie.Year}</p>
        <p>${movie.imdbRating}</p>
      `;

      moviesEl.appendChild(div);
    });
}
