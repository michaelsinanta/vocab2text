"""5-word few-shot examples for minangkabau.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "ambo | pronoun | I | pai ka sikola ambo",
                "sadang | adverb | currently | inyo sadang makan",
                "makan | verb | eat | makan ubi",
                "ikan | noun | fish | N/A",
                "goreng | adjective | fried | N/A",
            ]
        ),
        "output": "Ambo sadang makan ikan goreng.",
        "translation": "I am currently eating fried fish.",
    },
    {
        "word_candidates": "\n".join(
            [
                "inyo | pronoun | he | N/A",
                "pai | verb | go | N/A",
                "mambali | verb | buy | adiak pai mambali rokok",
                "baju | noun | dress | manjaik baju",
                "baru | adjective | new | rumah baru badiri",
            ]
        ),
        "output": "Inyo pai mambali baju baru.",
        "translation": "He is going to buy new clothes.",
    },
    {
        "word_candidates": "\n".join(
            [
                "awak | pronoun | 1 i; 2 us; 3 us | N/A",
                "suko | verb | like | N/A",
                "baraja | verb | study | N/A",
                "bahasa | noun | language | bahasa Minangkabau",
                "minang | noun | Minang | N/A",
            ]
        ),
        "output": "Awak suko baraja bahasa Minang.",
        "translation": "We like studying the Minang language.",
    },
    {
        "word_candidates": "\n".join(
            [
                "inyo | pronoun | we | daerah kito",
                "jalan | verb | walk | N/A",
                "ka | preposition | to | malam tu kami pai ka pasa",
                "labuah | noun | highway | labuah panjang",
                "gadang | adjective | big | N/A",
            ]
        ),
        "output": "Inyo jalan ka labuah gadang.",
        "translation": "He is walking to the main road.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tamu | noun | visitor | tamu tu alah pai",
                "hidang | verb | served | N/A",
                "minum | verb | drink | minum aia",
                "kopi | noun | coffee | untuak pambali kopi sajo",
                "angek | adjective | hot | N/A",
            ]
        ),
        "output": "Tamu dihidangan minum kopi angek.",
        "translation": "The guest is served hot coffee to drink.",
    },
    {
        "word_candidates": "\n".join(
            [
                "adiak | noun | brother | N/A",
                "duduak | verb | sit down | duduak elok-elok",
                "di | preposition | in | pitihnyo ilang di rumah",
                "muko | noun | front | N/A",
                "rumah | noun | house | N/A",
            ]
        ),
        "output": "Adiak duduak-duduak di muko rumah.",
        "translation": "Younger sibling is sitting around in front of the house.",
    },
    {
        "word_candidates": "\n".join(
            [
                "urang | noun | person | urang Padang",
                "sadang | adverb | currently | N/A",
                "makan | verb | eat | makan ubi",
                "nasi | noun | rice | N/A",
                "bungkuih | noun | wrap | N/A",
            ]
        ),
        "output": "Urang sadang makan nasi bungkuih.",
        "translation": "People are currently eating wrapped rice.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kaki | noun | feet (part of the body) | bola tu disipaknyo jo kaki",
                "wak | pronoun | my | N/A",
                "takilik | adjective | sprained | N/A",
                "pas | conjunction | when | N/A",
                "main | verb | play | N/A",
                "bola | noun | ball | N/A",
            ]
        ),
        "output": "Kaki wak takilik pas main bola.",
        "translation": "My leg got sprained while playing ball.",
    },
    {
        "word_candidates": "\n".join(
            [
                'katak | noun | "frog, toad, koncek, bell" | N/A',
                "ijau | adjective | green | N/A",
                "maloncek | verb | jump | N/A",
                "di | preposition | in | N/A",
                "halaman | noun | yard | N/A",
            ]
        ),
        "output": "Katak ijau maloncek di halaman.",
        "translation": "The green frog is jumping in the yard.",
    },
    {
        "word_candidates": "\n".join(
            [
                "si | article | the for person | N/A",
                "Mita | proper noun | Mita (person name) | N/A",
                "pai | verb | go | N/A",
                "mambali | verb | buy | N/A",
                "bareh | noun | rice | N/A",
            ]
        ),
        "output": "Si Mita pai mambali bareh.",
        "translation": "Mita is going to buy rice.",
    },
]
