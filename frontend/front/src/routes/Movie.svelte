<script>
      let promise = getFilmes();
      async function getFilmes() {
      // faz um request GET para endpoint /filmes
          const res = await fetch(`http://localhost:8000/filmes/`);
          const text = await res.json();
          if (res.ok) { return text; } 
      else { throw new Error(text);}
      }

    async function favoritarFilme(movieId) {
      try {
        const res = await fetch(`http://localhost:8000/favorite_movie/1`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            movie_id: movieId,
          }),
        });
        if (res.ok) {
          alert('Filme favoritado com sucesso!');
        } 
        else if(res.status == 303){
          alert('O filme já foi favoritado.');
        }
        else {
          const text = await res.json();
          throw new Error(text);
        }
      } catch (error) {
        console.error(error);
        alert('Erro ao favoritar filme.');
      }
    }


  </script>
  

    {#await promise}
    <div class="d-flex justify-content-center">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    {:then filmes}

    <div class="container text-center">
        <h1>Lista de filmes</h1>
        <div class="row">
            {#each filmes as filme}
            <div class="col border m-2 rounded-2 p-2">
                <h4>{filme.title}</h4>
                <img src="{filme.image}" alt ="">
                <!-- svelte-ignore missing-declaration -->
                <button on:click={() => favoritarFilme(filme.id)} type="button" class="btn btn-outline-warning mt-2">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                    <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
                  </svg>
                  Favoritar
              </button>
            </div>
            {/each}
        </div>
      </div>

  {:catch error}
      <p style="color: red">{error.message}</p>
  {/await}