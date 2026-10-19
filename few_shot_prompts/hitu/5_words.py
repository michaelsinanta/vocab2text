"""5-word few-shot examples for hitu.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "yau | pronoun | I | N/A",
                "a | verb | to eat | N/A",
                "ala | noun | rice | N/A",
                "kula | preposition | with | N/A",
                "iyan | noun | fish | N/A",
            ]
        ),
        "output": "Yau a ala kula iyan.",
        "translation": "I eat rice with fish.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ana | noun | child | N/A",
                "le | determiner | this | N/A",
                "te | adverb | not | N/A",
                "pahnene sow | verb | obedient / listens | N/A",
            ]
        ),
        "output": "Ana le te pahnene sow.",
        "translation": "This child does not listen.",
    },
    {
        "word_candidates": "\n".join(
            [
                "yau | pronoun | my | N/A",
                "waliu | noun | younger sibling | N/A",
                "ene | adverb | currently (progressive marker) | N/A",
                "pahai | verb | to play | N/A",
                "kanikir | noun | marbles | N/A",
            ]
        ),
        "output": "Yau waliu ene pahai kanikir.",
        "translation": "My younger sibling is currently playing marbles.",
    },
    {
        "word_candidates": "\n".join(
            [
                "inu | verb | to drink | N/A",
                "meung | noun | medicine | N/A",
                "wa | conjunction | so that | N/A",
                "iya | verb | to recover / heal | N/A",
                "malali | adverb | quickly | N/A",
            ]
        ),
        "output": "Inu meung wa iya malali.",
        "translation": "Drink medicine so that you recover quickly.",
    },
    {
        "word_candidates": "\n".join(
            [
                "amanan | noun | food | N/A",
                "le | determiner | this | N/A",
                "te | adverb | not yet | N/A",
                "pasaloton | verb | heated (passive) | N/A",
                "sala | adverb | not yet | N/A",
            ]
        ),
        "output": "Amanan le te pasaloton sala.",
        "translation": "This food has not yet been heated.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ana | noun | child | N/A",
                "le | determiner | this | N/A",
                "pahoi | verb | to bathe | N/A",
                "tawali | adjective | long (duration) | N/A",
                "sehwa | adverb | very / extremely | N/A",
            ]
        ),
        "output": "Ana le pahoi tawali sehwa.",
        "translation": "This child bathes for a very long time.",
    },
    {
        "word_candidates": "\n".join(
            [
                "lapun | noun | clothes | N/A",
                "ma | determiner | that | N/A",
                "ing | adverb | already | N/A",
                "koi | adjective | small | N/A",
                "nela | adverb | very | N/A",
            ]
        ),
        "output": "Lapun ma ing koi nela.",
        "translation": "Those clothes are already very small.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ite | pronoun | we | N/A",
                "lua | adverb | both / together | N/A",
                "oi | verb | to go | N/A",
                "le | preposition | to | N/A",
                "asal | noun | market | N/A",
            ]
        ),
        "output": "Ite lua oi le asal.",
        "translation": "The two of us go to the market.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kika | adverb | tomorrow | N/A",
                "yau | pronoun | I | N/A",
                "oi | verb | to go | N/A",
                "le | preposition | to | N/A",
                "koto | noun | Ambon | N/A",
            ]
        ),
        "output": "Kika yau oi le koto.",
        "translation": "Tomorrow I am going to Ambon.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ile | pronoun | he / she | N/A",
                "te | adverb | not | N/A",
                "pahnene | verb | to hear | N/A",
                "ale | pronoun | you | N/A",
                "lepa | verb | to speak | N/A",
            ]
        ),
        "output": "Ile te pahnene ale lepa.",
        "translation": "He/she does not hear you speaking.",
    },
]
