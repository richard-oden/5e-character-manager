<script>
    const mapObject = (obj, callbackFn) => Object.fromEntries(
        Object.entries(obj).map(callbackFn));

    export let abilityScores;
    export let proficiencyBonus;
    export let proficientSaves;

    $: abilityScoreBonuses = mapObject(abilityScores, ([k, v]) => [k, (v - 10) / 2]);
    $: savingThrows = mapObject(abilityScoreBonuses, ([k, v]) => [k, proficientSaves.includes(k) ? v + proficiencyBonus : v]);

</script>

<section class="row justify-between border-bottom">
    {#each Object.entries(abilityScores) as [name, score]}
        <div class="col align-center justify-between border-right flex-grow">
            <span class="font-sm">{name}</span>
            <div class="font-m">
                <span>{abilityScoreBonuses[name]}</span>/
                <span class={proficientSaves.includes(name) ? 'prof' : ''}>{savingThrows[name]}</span>
            </div>
            <span class="font-sm">{score}</span>
        </div>
    {/each}
</section>