<script> 
    let menu = 1;
    import Artist from "./Artist.svelte";
    import Movie from "./Movie.svelte"
    import Nav from "./Nav.svelte"
	import User from "./user.svelte";
	import UserList from "./UserList.svelte";
	import FavoriteMovies from "./FavoriteMovies.svelte";
	import FavoriteArtist from "./FavoriteArtist.svelte";
</script>

<Nav bind:menu/>

<div class="container col-6 mt-3">
	{#if menu === 1}
		<Movie/>
	{:else if menu === 2}
		<Artist/>
	{:else if menu === 3}
		<User/>
	{:else if menu === 4}
		<FavoriteMovies/>
	{:else if menu === 5}
	    <FavoriteArtist/>
	{:else}
		<UserList/>
	{/if}
</div>
