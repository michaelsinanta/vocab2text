"""10-word few-shot examples for hitu.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "yau | pronoun | my | N/A",
                "waliu | noun | younger sibling | N/A",
                "ene | adverb | currently | N/A",
                "pahai | verb | to play | N/A",
                "ball | noun | ball | N/A",
                "le | preposition | at | N/A",
                "lalestalai | noun | beside the house | N/A",
                "kula | preposition | with | N/A",
                "ile | pronoun | his / her | N/A",
                "lahan | noun | friend | N/A",
            ]
        ),
        "output": "Yau waliu ene pahai ball le lalestalai kula ile lahan.",
        "translation": "My younger sibling is currently playing ball beside the house with their friend.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mansia | noun | people | N/A",
                "le | preposition | at | N/A",
                "lumalale | noun | inside the house | N/A",
                "pasike | adjective | noisy | N/A",
                "nela | adverb | very | N/A",
                "nala | conjunction | so that | N/A",
                "yau | pronoun | I | N/A",
                "te | adverb | not | N/A",
                "bisa | verb | can | N/A",
                "kele | verb | to sleep | N/A",
            ]
        ),
        "output": "Mansia le lumalale pasike nela, nala yau te bisa kele.",
        "translation": "The people inside the house are very noisy, so I cannot sleep.",
    },
    {
        "word_candidates": "\n".join(
            [
                "patahia | verb | to tell / say | N/A",
                "wa | preposition | to / for | N/A",
                "ale | pronoun | your | N/A",
                "lahan | noun | friend | N/A",
                "ma | determiner | that | N/A",
                "kika | adverb | tomorrow | N/A",
                "alamasa | noun | afternoon | N/A",
                "oros | noun | o'clock | N/A",
                "hata | numeral | four | N/A",
                "ite | pronoun | we | N/A",
                "laka | verb | to depart | N/A",
            ]
        ),
        "output": "Patahia wa ale lahan ma, kika alamasa oros hata ite laka.",
        "translation": "Tell your friend that tomorrow afternoon at four o'clock we will leave.",
    },
    {
        "word_candidates": "\n".join(
            [
                "yau | pronoun | I | N/A",
                "te | adverb | not | N/A",
                "hala | verb | to bring | N/A",
                "pisi | noun | money | N/A",
                "wa | conjunction | to / for | N/A",
                "pasanahi | verb | to shop | N/A",
                "amanan | noun | food | N/A",
                "le | preposition | at | N/A",
                "skolah | noun | school | N/A",
            ]
        ),
        "output": "Yau te hala pisi wa pasanahi amanan le skolah.",
        "translation": "I do not bring money to buy food at school.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kolo | verb | to sit | N/A",
                "kula | preposition | with | N/A",
                "lahan-lahan | noun | friends | N/A",
                "le | preposition | at | N/A",
                "nanuli | noun | beach | N/A",
                "nala | conjunction | while | N/A",
                "apapei | verb | to wait | N/A",
                "lamatai | noun | sun | N/A",
                "kulu | verb | to set (of the sun) | N/A",
            ]
        ),
        "output": "Kolo kula lahan-lahan le nanuli nala apapei lamatai kulu.",
        "translation": "Sit with friends at the beach while waiting for the sun to set.",
    },
    {
        "word_candidates": "\n".join(
            [
                "yau | pronoun | I | N/A",
                "iya | verb | want to | N/A",
                "panene | verb | to ask / request | N/A",
                "maaf | noun | forgiveness / apology | N/A",
                "ena | preposition | about | N/A",
                "ite | pronoun | our | N/A",
                "pau'e | noun | commotion | N/A",
                "hanamasa | adverb | yesterday | N/A",
                "le | preposition | at | N/A",
                "iskola | noun | school | N/A",
            ]
        ),
        "output": "Yau iya panene maaf ena ite pau'e hanamasa le iskola.",
        "translation": "I want to apologize about the disturbance we caused yesterday at school.",
    },
    {
        "word_candidates": "\n".join(
            [
                "paiya | verb | to clean | N/A",
                "ale | pronoun | your | N/A",
                "halale | noun | room | N/A",
                "wusi | conjunction | after | N/A",
                "me | pronoun | that | N/A",
                "baru | adverb | only then | N/A",
                "ale | pronoun | you | N/A",
                "pahai | verb | to play | N/A",
                "kui | preposition | join / together with | N/A",
                "ale | pronoun | your | N/A",
                "lahan | noun | friend | N/A",
            ]
        ),
        "output": "Paiya ale halale wusi me baru ale pahai kui ale lahan.",
        "translation": "Clean your room first, then you can play with your friend.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tiyaka | noun | stomach | N/A",
                "nyela | adjective | full | N/A",
                "ing puna | verb | to make / cause | N/A",
                "yau | pronoun | my | N/A",
                "kele | noun | sleep | N/A",
                "naika | adverb | feels more | N/A",
                "iya | adjective | good | N/A",
            ]
        ),
        "output": "Tiyaka nyela ing puna ya kele naika iya.",
        "translation": "A full stomach makes my sleep feel better.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pake | verb | to wear | N/A",
                "lapun | noun | clothes | N/A",
                "mete | adjective | black | N/A",
                "wa | preposition | during | N/A",
                "lamata | noun | daytime | N/A",
                "ketu | noun | day | N/A",
                "ing puna | verb | to make / cause | N/A",
                "nanau | noun | body | N/A",
                "tambah | adverb | more | N/A",
                "rasa | verb | to feel | N/A",
                "loto | adjective | hot | N/A",
            ]
        ),
        "output": "Pake lapun mete wa lamata ketu ing puna nanau tambah rasa loto.",
        "translation": "Wearing black clothes during the daytime makes the body feel hotter.",
    },
    {
        "word_candidates": "\n".join(
            [
                "hekakau | noun | morning | N/A",
                "saat | adverb | earlier / just now | N/A",
                "ma | determiner | that | N/A",
                "ulan | noun | rain | N/A",
                "nala | conjunction | so | N/A",
                "yau | pronoun | I | N/A",
                "antar | verb | to take / accompany | N/A",
                "ena waliu | noun | my younger sibling | N/A",
                "lete | preposition | to | N/A",
                "skolah | noun | school | N/A",
                "ka'a | verb | to ride | N/A",
                "becak | noun | pedicab | N/A",
            ]
        ),
        "output": "Hekakau saat ma ulan, nala yau antar ena waliu lete skolah ka'a becak.",
        "translation": "It rained this morning, so I took my younger sibling to school by pedicab.",
    },
]
