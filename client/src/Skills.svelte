<script>
    const Proficiency = Object.freeze({
		NONE: 0,
		PROFICIENT: 1,
		EXPERT: 2
	});

    const getProficiencyClass = proficiency => {
        if (proficiency === Proficiency.EXPERT)
            return 'exp';
        
        if (proficiency === Proficiency.PROFICIENT)
            return 'prof';

        return '';
    };

    export let abilities;
    export let proficiencyBonus;
    export let skills;

    $: abilityScoreBonuses = Object.fromEntries(abilities.map(_ => [_.name, (_.score - 10) / 2]));
    $: skillBonuses = Object.fromEntries(skills.map(skill => {
        let bonus = abilityScoreBonuses[skill.ability];

        if (skill.proficiency === Proficiency.PROFICIENT)
            return [skill.name, bonus + proficiencyBonus];
        
        if (skill.proficiency === Proficiency.EXPERT)
            return [skill.name, bonus + (proficiencyBonus * 2)];

        return [skill.name, bonus];
    }));
</script>

<section class="col bordered margin-bottom-2">
    <input id="skills-collapsible" class="collapsible-toggle" type="checkbox">
    <label for="skills-collapsible" class="collapsible-label">Skills</label>
    <div class="collapsible-content col">
        <div class="col font-sm">
            {#each skills as skill}
                <div class="row border-bottom-sm justify-between {getProficiencyClass(skill.proficiency)}">
                    <span>{skill.name} ({skill.ability})</span>
                    <span>{skillBonuses[skill.name]}</span>
                </div>
            {/each}
        </div>
    </div>
</section>