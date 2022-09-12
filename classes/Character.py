import uuid

from classes.ExpendableResource import ExpendableResource

class Character():
    def __init__(
        name: str, 
        race_id: str, 
        classes: dict[str, int],
        abilities: dict[str, int],
        background_id: str,
        feat_ids: list[str],
        proficient_skills: list[str],
        expert_skills: list[str],
        hp_max: int,
        hp_current: int,
        hp_total: int,
        hp_temp: int,
        hit_dice_current: dict[str, int],
        death_saves: int,
        inspiration: int,
        item_ids: list[str],
        known_spell_ids: list[str],
        prepared_spell_ids: list[str],
        expended_spell_slots: dict[int, int],
        additional_resources: dict[str, ExpendableResource],
        notes: dict[str, str]):

        id = str(uuid.uuid4())
        name = name
        race_id = race_id
        classes = classes
        level = level
        abilities = abilities
        background_id = background_id
        feat_ids = feat_ids
        proficient_skills = proficient_skills
        expert_skills = expert_skills
        hp_max = hp_max
        hp_current = hp_current
        hp_total = hp_total
        hp_temp = hp_temp
        hit_dice_current = hit_dice_current
        death_saves = death_saves
        inspiration = inspiration
        item_ids = item_ids
        known_spell_ids = known_spell_ids
        prepared_spell_ids = prepared_spell_ids
        expended_spell_slots = expended_spell_slots
        additional_resources = additional_resources
        notes = notes
