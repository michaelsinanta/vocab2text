"""10-word few-shot examples for acehnese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "aneuk miet | noun | child aged 3 to 12 years old | N/A",
                "meu'en | verb | to play | aneuk miet teungoh jimeu'en di lheun",
                "bak | particle | with, at | suratjih na bak lôn",
                "lampôih | noun | garden | N/A",
                "sira | particle | while | jih jipeugah sira jibri paket nyan",
                "jep | verb | to drink | jep ie mameh tiep uroe hana get",
                "ie | noun | water | alue nyoe ubiet that ie",
                "u | noun | coconut | N/A",
            ]
        ),
        "output": "Aneuk miet jimeu'en bak lampôih sira jijep ie u.",
        "translation": "Children play in the garden while drinking coconut water.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mak | noun | mother | N/A",
                "taguen | verb | to cook, to process | N/A",
                "kuah | noun | soup | ayah peugot kuah sie",
                "eungkôt | noun | fish | N/A",
                "keu | particle | for | N/A",
                "bandum | adverb | all together | N/A",
                "ureueng | noun | person | N/A",
                "bak | particle | with, at | suratjih na bak lôn",
                "rumoh | noun | house | N/A",
                "kamoe | pronoun | we/us | Kamoe jak u meunasah",
            ]
        ),
        "output": "Mak taguen kuah eungkôt keu bandum ureung bak rumoh kamoe.",
        "translation": "Mother cooks fish soup for everyone at our house.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bék | particle | do not | bek meunan tapubuet!",
                "uroe | noun | day | sigo jumat na tujoh uroe",
                "nyoe | particle | this | N/A",
                "lon | noun | myself | N/A",
                "neuk | N/A | to want to | lon neuk pajoh bu",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | Lon jak u keudè",
                "peukan | noun | market | uroe nyoe, peukan rame that",
                "mita | verb | to search, to look for | N/A",
                "eungkôt | noun | fish | N/A",
                "masen | adjective | salty | boh manok masen",
            ]
        ),
        "output": "Bék uroe nyoe lon neuk jak u peukan mita eungkôt masen.",
        "translation": "not today, i want to go the festival to look for salted fish",
    },
    {
        "word_candidates": "\n".join(
            [
                "lon | noun | myself | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "sikula | noun | school | Lon jak sikula",
                "poh | adverb | o'clock | nyoe ka poh siploh",
                "tujoh | noun | seven | umu jih tujoh buleuen",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "dan | preposition | and | adoe dan aduen",
                "di | preposition | at; in | na bu di sikula",
                "intat | N/A | to deliver | adék jijak intat bu u blang",
                "lé | particle | by | rumoh nyoe geubloh lé yahjih buleuen nyang kalheueth",
                "ayah | noun | father | N/A",
            ]
        ),
        "output": "Lon jak sikula poh tujoh beungoh dan di intat lé ayah.",
        "translation": "I go to school at 7 and dropped off by father",
    },
    {
        "word_candidates": "\n".join(
            [
                "tiep | particle | every | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "ayah | noun | father | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | Lon jak u keudè",
                "blang | noun | field | N/A",
                "keu | particle | for | N/A",
                "meugoë | verb | farming | nek lon meugoe bak blang",
                "padé | noun | rice plant | N/A",
            ]
        ),
        "output": "Tiep beungoh ayah jak u blang keu meugoë padé.",
        "translation": "Every morning, father goes to the rice field to tend the crops.",
    },
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "bu | noun | cooked rice | jih h'an ek jipajohbu",
                "ngen | particle | with | N/A",
                "eungkôt | noun | fish | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "sabab | noun | because of | N/A",
                "deuek | adjective | hungry | pruet lôn deuek, bu hana le",
                "that | adverb | very | rayek that",
            ]
        ),
        "output": "Lôn pajoh bu ngen eungkôt beungoh nyoe sabab lôn deuek that.",
        "translation": "I eat rice and fish this morning because i am very hungry",
    },
    {
        "word_candidates": "\n".join(
            [
                "ma | noun | mother | N/A",
                "lôn | pronoun | I | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "keudè | noun | shop | Keudè nyan raya",
                "keu | particle | for | N/A",
                "bloe | verb | to buy | ibu jak u peukan geuneuk bloe manok",
                "bu | noun | cooked rice | jih h'an ek jipajohbu",
                "ngen | particle | with | N/A",
                "ie | noun | water | alue nyoe ubiet that ie",
            ]
        ),
        "output": "Ma lôn jak u keudé keu bloe bu ngen ie.",
        "translation": "My mother goes to the shop to buy rice and water",
    },
    {
        "word_candidates": "\n".join(
            [
                "aduen | noun | elder sibling | N/A",
                "lôn | pronoun | I | N/A",
                "ngen | particle | with | N/A",
                "adoe | noun | younger sibling | N/A",
                "maté | verb | turn off | yah lon neupeumaté apui",
                "panyöt | noun | lamp | Panyöt nyan trang",
                "lam | particle | in | N/A",
                "bilék | noun | room | Bilék lon baro",
                "ayah | noun | father | N/A",
            ]
        ),
        "output": "Aduen lôn ngen adoe lôn neupeumaté panyöt lam bilék ayah.",
        "translation": "My older sister and my younger sister turn off the lights in my father's room",
    },
    {
        "word_candidates": "\n".join(
            [
                "buët | noun | work | buët nyan brat",
                "rumoh | noun | house | N/A",
                "sikula | noun | school | lôn jak sikula",
                "lôn | pronoun | I | N/A",
                "abéh | verb | finished | bék talakèe lé, ka habéh",
                "bak | particle | with, at | suratjih na bak lôn",
                "poh | noun | at (time marker) | poh lapan malam",
                "lapan | numeral | eight | lapan boh manok",
                "malam | noun | night | N/A",
                "nyoe | pronoun | this | nyoe rumoh lon",
            ]
        ),
        "output": "Buët rumoh sikula lôn abeh bak poh lapan malam nyoe.",
        "translation": "My school work is finished at eight o'clock tonight",
    },
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "ngen | particle | with | N/A",
                "rakan | noun | friend | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "gunong | noun | mountain | N/A",
                "watѐe | noun | time | watѐe nyan ka",
                "singoh | adverb | tomorrow | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
            ]
        ),
        "output": "Lôn ngen rakan lôn jak u gunong watèe singoh beungoh.",
        "translation": "My friend and I go to the mountain tomorrow morning.",
    },
]
