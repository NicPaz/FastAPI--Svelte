<script>
    let user_id = 1; // ou qualquer outro ID de usuário que você queira exibir os favoritos
  
    let promise = getFavoriteMovies();
    async function getFavoriteMovies() {
      const res = await fetch(`http://localhost:8000/favorite_movies/${user_id}`);
      const text = await res.json();
      if (res.ok) { return text; } 
      else { throw new Error(text);}
    }

    async function getMovieInfo(movie_id) {
    const res = await fetch(`http://localhost:8000/movie/${movie_id}`);
    const text = await res.json();
    if (res.ok) { return text; } 
    else { throw new Error(text);}
  }


  </script>
  
  {#await promise}
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  {:then favoriteMovies}
    <div class="container text-center">
        <h1>Favorite Movies</h1>
        <div class="row">
          {#each favoriteMovies as movie}
            {#await getMovieInfo(movie.movie_id)}
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            {:then movieInfo}
              <div class="col border m-2 rounded-2 p-2">
                <h4>{movieInfo.title}</h4>
                <img src="{movieInfo.image}" alt="{movieInfo.title}">
              </div>
            {:catch error}
              <p style="color: red">{error.message}</p>
            {/await}
          {/each}
        </div>
      </div>
    {:catch error}
      <p style="color: red">{error.message}</p>
    {/await}