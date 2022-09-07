from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    character = {
        'id': '0',
        'name': 'Theodas Aldevyr',
        'class': 'Wizard',
        'subClass': 'School of Evocation',
        'race': 'High Elf',
        'alignment': 'Lawful Good',
        'level': 16,
        'abilityScores': {
            'STR': 10,
            'DEX': 16,
			'CON': 18,
			'INT': 22,
			'WIS': 12,
			'CHA': 8
        },
        'proficiencyBonus': 5,
        'savingThrows': [
            {
                'ability': 'CON',
                'proficiency': 1
            },
            {
                'ability': 'INT',
                'proficiency': 1
            },
            {
                'ability': 'WIS',
                'proficiency': 1
            }
        ],
        'hitPoints': {
            'total': 134,
            'maximum': None,
            'current': 74,
            'temporary': 0
        },
        'hitDice': {
            'total': 16,
            'current': 6,
            'size': 6
        },
        'armorClass': 15,
        'initiative': 3,
        'speed': 30,
        'deathSaves': 0,
        'inspiration': 0,
        'miscProficiencies': {
            'languages': ['Common', 'Elvish', 'Sylvan', 'Draconic', 'Celestial', 'Infernal'],
            'tools': ['Tinkerer\'s Tools'],
            'weapons': ['longswords', 'shortswords', 'shortbows', 'longbows', 'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbows']
        },
        'vision': {
            'type': 'Darkvision',
            'range': 60
        },
        'wealth': {
            'copper': 0,
            'silver': 0,
            'electrum': 0,
            'gold': 800,
            'platinum': 0
        },
        'feats': [
            {
                'name': 'War Caster',
                'description': '''You have practiced casting spells in the midst of combat, learning techniques that grant you the following benefits:
You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.
You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.
When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature.'''
            },
            {
                'name': 'Resilient',
                'description': '''Choose one ability score. You gain the following benefits:
Increase the chosen ability score by 1, to a maximum of 20.
You gain proficiency in saving throws using the chosen ability.'''
            },
            {
                'name': 'Artificer Initiate',
                'description': '''You've learned some of an artificer's inventiveness:
You learn one cantrip of your choice from the artificer spell list, and you learn one 1st-level spell of your choice from that list. Intelligence is your spellcasting ability for these spells.
You can cast this feat's 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have.
You gain proficiency with one type of artisan's tools of your choice, and you can use that type of tool as a spellcasting focus for any spell you cast that uses Intelligence as its spellcasting ability.'''
            }
        ],
        'actions': [

        ],
        'spells': [

        ],
        'items': [

        ],
        'notes': [
            
        ]
    }
    return send_from_directory('client/public', 'index.html', character)

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


if __name__ == "__main__":
    app.run(debug=True)