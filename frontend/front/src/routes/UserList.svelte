<script>
      let promise = getUsers();
      async function getUsers() {
      // faz um request GET para endpoint /filmes
          const res = await fetch(`http://localhost:8000/users/`);
          const text = await res.json();
          if (res.ok) { return text; } 
      else { throw new Error(text);}
      }

      async function soft_delete_user(userId) {
        console.log('Excluindo usuário:', userId);
        const res = await fetch(`http://localhost:8000/users/${userId}`, {
          method: "PUT", // Usamos o método PUT para atualizar o usuário
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ is_active: false }), // Defina is_active como false
        });

        if (res.ok) {
          promise = getUsers();
        } else {
          throw new Error("Failed to soft delete user.");
        }
      }


  </script>
  
  
  {#await promise}
      <p>...loading</p>
  {:then users}
    <h2>Lista de Usuários</h2>
      <div class="border rounded-2 p-3">
        <table class="table table-striped table-hover">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
            {#each users.filter(user => user.is_active) as user}
              <tr>
                <th scope="row">{user.id}</th>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                    <button on:click={()=>soft_delete_user(user.id)} type="button" class="btn btn-outline-danger">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                            <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                          </svg>
                        Remove
                    </button>
                </td>
              </tr>
            {/each}
            </tbody>
          </table>
        </div>
          
  
  {:catch error}
      <p style="color: red">{error.message}</p>
  {/await}