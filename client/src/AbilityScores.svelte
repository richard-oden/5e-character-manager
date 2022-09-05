<script>
    Object.prototype.mapObject = callbackFunction => Object.fromEntries(
        Object.entries(this).map(callbackFunction));

    const abilityScores = {
        STR: 10,
        DEX: 16,
        CON: 18,
        INT: 22,
        WIS: 12,
        CHA: 8
    };
    const proficiencyBonus = 5;
    const proficientSaves = ['CON', 'INT', 'WIS'];

    $: abilityScoreBonuses = abilityScores.mapObject(([k, v]) => [k, (v - 10) / 2]);
    $: savingThrows = abilityScoreBonuses.mapObject(([k, v]) => [k, proficientSaves.includes(k) ? v + proficiencyBonus : v]);

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