<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<script>
    export let menu;
</script>


<nav class="navbar navbar-expand-lg" style="background-color: #9400d3;">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">
      <img src="https://filmeseseries.org/wp-content/uploads/2022/01/logotipo-filmes-e-series.png" alt="Bootstrap" width="150" height="auto">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link link-light" aria-current="page" href="/" on:click|preventDefault={() => (menu = 1)}>Movies</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/" on:click|preventDefault={() => (menu = 2)}>Artist</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/" on:click|preventDefault={() => (menu = 3)}>Create User</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/" on:click|preventDefault={() => (menu = 4)}>Favorite Movies</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/" on:click|preventDefault={() => (menu = 5)}>Favorite Artists</a>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="/" on:click|preventDefault={() => (menu = 6)}>Users</a>
        </li>
      </ul>
      
    </div>
  </div>
</nav>
