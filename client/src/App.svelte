<script>
	export let character;
	import AbilityScores from './AbilityScores.svelte';
</script>

<main>
	<AbilityScores {...character}/>
</main>