<script>
      let promise = getArtista();
      async function getArtista() {
          const res = await fetch(`http://localhost:8000/artistas/`);
          const text = await res.json();
          if (res.ok) { return text; } 
      else { throw new Error(text);}
      }
      function handleClick() {
          promise = getArtista();
      }
  </script>
  
  <button on:click={handleClick}> Artistas</button>
  
  {#await promise}
    <div class="d-flex justify-content-center">
        <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
        </div>
    </div>
  {:then artista}
    <h1>{artista.name}</h1>
        <h2>Biography:</h2>
        <p>{artista.biography}</p>
        <img src="{artista.image}" alt ="">
  
  {:catch error}
      <p style="color: red">{error.message}</p>
  {/await}