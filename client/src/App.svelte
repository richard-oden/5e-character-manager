<script>
	import AbilityScores from './AbilityScores.svelte';

	const character = {
		abilityScores: {
			STR: 10,
			DEX: 16,
			CON: 18,
			INT: 22,
			WIS: 12,
			CHA: 8
		},
		proficiencyBonus: 5,
		proficientSaves: ['CON', 'INT', 'WIS']
	};
</script>

<main>
	<section class="row justify-between border-bottom">
		<AbilityScores abilityScores={character.abilityScores} proficiencyBonus={character.proficiencyBonus} proficientSaves={character.proficientSaves}/>
	</section>
</main>