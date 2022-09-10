<script>
	export let character;
	import AbilityScores from './AbilityScores.svelte';
	import Skills from './Skills.svelte';
</script>

<main>
	<AbilityScores {...character}/>
	<Skills {...character}/>
</main>