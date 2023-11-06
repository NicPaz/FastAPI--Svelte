<script>
    let resposta = "";
    async function sendForm(e){
        // envia o formulario no formato json
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());
        const res = await fetch('http://localhost:8000/users',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const json = await res.json();
        resposta = JSON.stringify(json);
    }
    </script>
    

    
    <p>{resposta}</p>
    <h2>Cadastrar Usuário</h2>
        <div class="border rounded-2 p-3">
            <form class="crud" on:submit|preventDefault={sendForm}>
                <div class="mb-3">
                    <label for="InputName" class="form-label">User Name</label>
                    <input type="text" class="form-control" id="InputName" name="name" placeholder="User name" required autocomplete="off">
                </div>
                <div class="mb-3">
                    <label for="InputEmail" class="form-label">Email</label>
                    <input type="text" class="form-control" id="InputEmail" name="email" placeholder="Email" required autocomplete="off">
                </div>
                <div class="mb-3">
                    <label for="InputPassword" class="form-label">Email</label>
                    <input type="password" class="form-control" id ="InputPassword" name="password" placeholder="password" required autocomplete="off">
                </div>
                <input class="btn btn-primary" type="submit" value="Submit">
            </form>
        </div>
    
    <style>

    </style>
     