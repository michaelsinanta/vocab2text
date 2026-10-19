"""5-word few-shot examples for acehnese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "neuk | N/A | to want to | lon neuk pajoh bu",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "keudè | noun | shop | Keudè nyan raya",
            ]
        ),
        "output": "Lôn neuk jak u keudè.",
        "translation": "I wanna go to the shop",
    },
    {
        "word_candidates": "\n".join(
            [
                "uroe | noun | day | sigo jumat na tujoh uroe",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "seuuem | adjective | hot | ie ju nyan seuuem that",
                "that | adverb | very | rayek that",
            ]
        ),
        "output": "Uroe nyoe seuuem that.",
        "translation": "Today is very hot",
    },
    {
        "word_candidates": "\n".join(
            [
                "rumoh | noun | house | N/A",
                "beulau | adjective | blue | rumoh beulau nyan lagak",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "lagak | adjective | beautiful | lagak that bajèe droen",
                "that | adverb | very | rayek that",
            ]
        ),
        "output": "Rumoh beulau nyoe lagak that.",
        "translation": "This blue house is very beautiful",
    },
    {
        "word_candidates": "\n".join(
            [
                "peuë | interrogative pronoun | what | peuë nan?",
                "kah | pronoun | you | N/A",
                "kalheueh | abbreviation | already | N/A",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "bu | noun | cooked rice | jih h'an ek jipajohbu",
            ]
        ),
        "output": "Peuë kah kalheueh pajôh bu?",
        "translation": "Have you eaten?",
    },
    {
        "word_candidates": "\n".join(
            [
                "Manok | noun | chicken | manok nyan rayeuk",
                "crôh | verb | fry | manok crôh",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "that | adverb | very | rayek that",
                "mangat | adjective | delicious | mangat that boh panah nyoe",
            ]
        ),
        "output": "Manok crôh nyoe that mangat.",
        "translation": "This fried chicken is delectable",
    },
    {
        "word_candidates": "\n".join(
            [
                "adoe | noun | younger sibling | N/A",
                "teungoh | adverb | in the middle of | Lon teungoh meurunoe",
                "meurunoe | verb | to study | N/A",
                "teumuleh | verb | writing | aneuk miet teumuleh bak bintéh",
            ]
        ),
        "output": "Adoe teungoh meurunoe teumuleh.",
        "translation": "My younger sibling is learning to write.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mie | noun | cat | mie nyan warna itam",
                "nyan | demonstrative pronoun | that | Rumoh nyan lagak",
                "éh | verb | to sleep | satpam hana éh malam",
                "bak | particle | with, at | suratjih na bak lôn",
                "sofa | noun | sofa | sofa nyan lagak",
            ]
        ),
        "output": "Mie nyan jiéh bak sofa.",
        "translation": "The cat is sleeping on the sofa.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kamoe | pronoun | we/us | Kamoe jak u meunasah",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "bu | noun | cooked rice | jih h'an ek jipajohbu",
                "ngen | particle | with | N/A",
                "keluarga | noun | family | keluarga lon na peut ureueng",
            ]
        ),
        "output": "Kamoe pajoh bu ngen keluarga.",
        "translation": "We eat rice with the family.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bungong | noun | flower | bungong mirah ka lon tanom",
                "bak | particle | with, at | suratjih na bak lôn",
                "lampôih | noun | garden | N/A",
                "cukôp | adjective | enough / sufficient | kama nyoe sép keu duwa droe manteng",
                "lagak | adjective | beautiful | lagak that bajèe droen",
            ]
        ),
        "output": "Bungong bak lampôih cukôp lagak.",
        "translation": "The flowers in the garden are very beautiful.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mamplam | noun | mango | N/A",
                "lon | noun | myself | N/A",
                "manéh | adjective | sweet | N/A",
                "that | adverb | very | rayek that",
            ]
        ),
        "output": "Mamplam lon manéh that.",
        "translation": "My mango is very sweet.",
    },
]
