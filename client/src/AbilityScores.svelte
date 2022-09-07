<script>
    const mapObject = (obj, callbackFn) => Object.fromEntries(
        Object.entries(obj).map(callbackFn));

    export let abilityScores;
    export let proficiencyBonus;
    export let savingThrows;

    $: abilityScoreBonuses = mapObject(abilityScores, ([k, v]) => [k, (v - 10) / 2]);
    $: savingThrowBonuses = mapObject(abilityScoreBonuses, ([k, v]) => {
        const savingThrow = savingThrows.find(savingThrow => savingThrow.ability === k);

        if (savingThrow?.proficiency === 1)
            return [k, v + proficiencyBonus];

        if (savingThrow?.proficiency === 2)
            return [k, v + (proficiencyBonus * 2)];

        return [k, v];
    });

</script>

<section class="row justify-between border-bottom">
    {#each Object.entries(abilityScores) as [name, score]}
        <div class="col align-center justify-between border-right flex-grow">
            <span class="font-sm">{name}</span>
            <div class="font-m">
                <span>{abilityScoreBonuses[name]}</span>/
                <span>{savingThrowBonuses[name]}</span>
            </div>
            <span class="font-sm">{score}</span>
        </div>
    {/each}
</section>