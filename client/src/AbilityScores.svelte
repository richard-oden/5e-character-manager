<script>
    export let abilities;
    export let proficiencyBonus;
    export let savingThrows;

    const mapObject = (obj, callbackFn) => Object.fromEntries(
        Object.entries(obj).map(callbackFn));

    $: abilityScoreBonuses = Object.fromEntries(abilities.map(_ => [_.name, (_.score - 10) / 2]));
    $: savingThrowBonuses = mapObject(abilityScoreBonuses, ([k, v]) => {
        const savingThrow = savingThrows.find(savingThrow => savingThrow.ability === k);

        if (savingThrow?.proficiency === 1)
            return [k, {value: v + proficiencyBonus, class: 'prof'}];

        if (savingThrow?.proficiency === 2)
            return [k, {value: v + (proficiencyBonus * 2), class: 'exp'}];

        return [k, {value: v, class: ''}];
    });

</script>

<section class="row justify-between border-bottom">
    {#each abilities as ability}
        <div class="col align-center justify-between border-right flex-grow">
            <span class="font-sm">{ability.name}</span>
            <div class="font-m">
                <span>{abilityScoreBonuses[ability.name]}</span>/
                <span class="{savingThrowBonuses[ability.name].class}">
                    {savingThrowBonuses[ability.name].value}
                </span>
            </div>
            <span class="font-sm">{ability.score}</span>
        </div>
    {/each}
</section>