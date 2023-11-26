<script>

    let user_id = 1; 

    import Modal from './Modal.svelte';

    let showModal = false;
    let artistaModal = {};
    let artista = [];

    async function abrirModal(artist_id) {
    try {
      const res = await fetch(`http://localhost:8000/artist/${artist_id}`);
      const artistInfo = await res.json();

      if (res.ok) {
        artistaModal = artistInfo;
        showModal = true;
      } else {
        throw new Error(artistInfo);
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao carregar informações do artista.');
    }
  }
  
    let promise = getFavoriteArtist();
    async function getFavoriteArtist() {
      const res = await fetch(`http://localhost:8000/favorite_artist/${user_id}`);
      const text = await res.json();
      if (res.ok) { return text; } 
      else { throw new Error(text);}
    }

    async function getArtistInfo(artist_id) {
    const res = await fetch(`http://localhost:8000/artist/${artist_id}`);
    const text = await res.json();
    if (res.ok) { return text; } 
    else { throw new Error(text);}
  }

  async function desfavoritarArtist(artist_id) {
    try {
      const res = await fetch(`http://localhost:8000/unfavorite_artist/1`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          artist_id: artist_id,
        }),
      });
     
      if (res.ok) {
        alert('Artista removido dos favoritos com sucesso!');
        promise= getFavoriteArtist();
      }
      else {
        const text = await res.json();
        throw new Error(text);
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao desfavoritar o artista');
    }
  }

  </script>
  
  {#await promise}
    <div class="d-flex justify-content-center">
    </div>
  {:then favoriteArtist}
    <div class="container text-center">
        <h1>Favorite Artists</h1>
        <div class="row">
          {#each favoriteArtist as artist}
            {#await getArtistInfo(artist.artist_id)}
              <div class="col-3 border m-2 rounded-2 p-2">
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
            {:then artistInfo}
              <div class="col-3 border m-2 rounded-2 p-2">
                <h4>{artistInfo.name}</h4>
                <img src="{artistInfo.image}" alt="{artistInfo.name}">
                <button on:click={() => abrirModal(artist.artist_id)} type="button" class="btn btn-outline-primary mt-2" data-toggle="modal" data-target="#exampleModalLong">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
          </svg>
                    Details
                  </button>
                <button on:click={() => desfavoritarArtist(artist.artist_id)} type="button" class="btn btn-outline-danger mt-2">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-half" viewBox="0 0 16 16">
                    <path d="M5.354 5.119 7.538.792A.516.516 0 0 1 8 .5c.183 0 .366.097.465.292l2.184 4.327 4.898.696A.537.537 0 0 1 16 6.32a.548.548 0 0 1-.17.445l-3.523 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256a.52.52 0 0 1-.146.05c-.342.06-.668-.254-.6-.642l.83-4.73L.173 6.765a.55.55 0 0 1-.172-.403.58.58 0 0 1 .085-.302.513.513 0 0 1 .37-.245l4.898-.696zM8 12.027a.5.5 0 0 1 .232.056l3.686 1.894-.694-3.957a.565.565 0 0 1 .162-.505l2.907-2.77-4.052-.576a.525.525 0 0 1-.393-.288L8.001 2.223 8 2.226v9.8z"/>
                  </svg>
                  Unfav
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

    <Modal bind:showModal>
      <h2 slot="header">
        {artistaModal.name}
        <small><em>id: {artistaModal.id}</em></small>
      </h2>
      <div class="d-flex justify-content-center">
        <img src="{artistaModal.image}" alt="{artistaModal.name}">
      </div>
      <ul class="definition-list">
        <li>Biography: {artistaModal.biography}</li>
        <li>Birthday: {artistaModal.birthday}</li>
        <li>Popularity: {artistaModal.popularity}</li>
      </ul>
    </Modal>