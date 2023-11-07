<script>
	import { get } from "svelte/store";

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

  async function desfavoritarFilme(movie_id) {
    try {
      const res = await fetch(`http://localhost:8000/unfavorite_movie/1`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          movie_id: movie_id,
        }),
      });
     
      if (res.ok) {
        alert('Filme removido dos favoritos com sucesso!');
        promise= getFavoriteMovies();
      }
      else {
        const text = await res.json();
        throw new Error(text);
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao desfavoritar o filme');
    }
  }

  </script>
  
  {#await promise}
    <div class="d-flex justify-content-center">
    </div>
  {:then favoriteMovies}
    <div class="container text-center">
        <h1>Favorite Movies</h1>
        <div class="row">
          {#each favoriteMovies as movie}
            {#await getMovieInfo(movie.movie_id)}
              <div class="col-3 border m-2 rounded-2 p-2">
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
            {:then movieInfo}
              <div class="col-3 border m-2 rounded-2 p-2">
                <h4>{movieInfo.title}</h4>
                <img src="{movieInfo.image}" alt="{movieInfo.title}">
                <button on:click={() => desfavoritarFilme(movie.movie_id)} type="button" class="btn btn-outline-danger mt-2">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-half" viewBox="0 0 16 16">
                    <path d="M5.354 5.119 7.538.792A.516.516 0 0 1 8 .5c.183 0 .366.097.465.292l2.184 4.327 4.898.696A.537.537 0 0 1 16 6.32a.548.548 0 0 1-.17.445l-3.523 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256a.52.52 0 0 1-.146.05c-.342.06-.668-.254-.6-.642l.83-4.73L.173 6.765a.55.55 0 0 1-.172-.403.58.58 0 0 1 .085-.302.513.513 0 0 1 .37-.245l4.898-.696zM8 12.027a.5.5 0 0 1 .232.056l3.686 1.894-.694-3.957a.565.565 0 0 1 .162-.505l2.907-2.77-4.052-.576a.525.525 0 0 1-.393-.288L8.001 2.223 8 2.226v9.8z"/>
                  </svg>
                  Unfavorite
                </button>
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