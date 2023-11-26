<script>
  let promise = getArtistas();
  let artistas = [];
  let searchTerm = "";
  let forceUpdate = {};
  let artistaModal = {}; 

  let artista;

  import Modal from './Modal.svelte';

	let showModal = false;

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

  async function getArtistas() {
    try {
      const res = await fetch(`http://localhost:8000/artistas/`);
      const text = await res.json();
      if (res.ok) {
        artistas = text;
      } else {
        throw new Error(text);
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao carregar artistas.');
    }
  }

  async function favoritarArtista(artistId) {
    try {
      const res = await fetch(`http://localhost:8000/favorite_artist/1`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          artist_id: artistId,
        }),
      });

      if (res.ok) {
        alert('Artista favoritado com sucesso!');
      } else {
        const text = await res.json();
        throw new Error(text);
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao favoritar artista.');
    }
  }


  async function handleSubmit(event) {
    event.preventDefault();

    if (searchTerm.trim() !== "") {
      try {
        const res = await fetch(`http://localhost:8000/artista/${encodeURIComponent(searchTerm)}`);
        const artistasEncontrados = await res.json();
        
        // Atualiza a lista de artista com os  encontrados
        artistas = artistasEncontrados;
        forceUpdate = {}; // Força a atualização do estado
      } catch (error) {
        console.error(error);
        alert('Erro ao buscar artista.');
      }
    }
  }

  
</script>

<div class="container text-center">
  <h1>Lista de artistas</h1>
  <form class="d-flex" role="search" on:submit="{handleSubmit}">
    <input bind:value="{searchTerm}" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-warning" type="submit" id="busca">Search</button>
  </form>

  {#await promise}
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  {:then}
    <!-- Se precisar exibir algo enquanto aguarda o carregamento -->
  {:catch error}
    <p style="color: red">{error.message}</p>
  {/await}

  <div class="row">
    {#each artistas as artista (artista.id)}
      <div class="col-3 border m-2 rounded-2 p-2">
        <h4>{artista.name}</h4>
        <img src="{artista.image}" alt="{artista.title}">
        <button on:click={() => abrirModal(artista.id)} type="button" class="btn btn-outline-primary mt-2" data-toggle="modal" data-target="#exampleModalLong">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
</svg>
          Details
        </button>
        <button on:click={() => favoritarArtista(artista.id)} type="button" class="btn btn-outline-warning mt-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
            <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
          </svg>
          Favorite
        </button>
      </div>
    {/each}
  </div>
</div>

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
