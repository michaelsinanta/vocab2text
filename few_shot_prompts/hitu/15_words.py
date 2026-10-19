"""15-word few-shot examples for hitu.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "patahia | verb | to tell | N/A",
                "wa | preposition | to | N/A",
                "ina | noun | mother | N/A",
                "kula | preposition | with / in a manner of | N/A",
                "iya iya | adverb | nicely / gently | N/A",
                "ena | conjunction | that | N/A",
                "wali'u | noun | younger sibling | N/A",
                "rasa | verb | to feel | N/A",
                "malalekeng | adjective | sad | N/A",
                "kalu | conjunction | if | N/A",
                "ena | verb | gets / can | N/A",
                "tanarat | verb | to be scolded | N/A",
                "isan-isane | adverb | too often | N/A",
            ]
        ),
        "output": "Patahia wa ina kula iya iya ena wali'u rasa malalekeng kalu ena tanarat isan-isane.",
        "translation": "Tell mother gently that the younger sibling feels sad when scolded too often.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pahnene | verb | to listen | N/A",
                "yau | pronoun | my | N/A",
                "lepa | noun | explanation | N/A",
                "me | adverb | first | N/A",
                "lawa | verb | to run away | N/A",
                "he'i | preposition | from | N/A",
                "yau | pronoun | me | N/A",
                "ehe'e | adverb | don't | N/A",
                "inta | conjunction | as if | N/A",
                "yau | pronoun | I | N/A",
                "le | determiner | this | N/A",
                "mansia | noun | person | N/A",
                "sahane | adjective | other | N/A",
            ]
        ),
        "output": "Pahnene yau lepa me, lawa he'i yau ehe'e inta yau le mansia sahane.",
        "translation": "Please listen to my explanation first; do not run away from me as if I were a stranger.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tolong | interjection | please | N/A",
                "panara | verb | to be angry | N/A",
                "yau | pronoun | I | N/A",
                "ehe | adverb | don't | N/A",
                "me | adverb | first | N/A",
                "yau | pronoun | I | N/A",
                "kewa | verb | to know | N/A",
                "yau | pronoun | I | N/A",
                "pasala | adjective | wrong | N/A",
                "sale | pronoun | all | N/A",
                "le | determiner | this | N/A",
                "ite | pronoun | we | N/A",
                "bisa | verb | can | N/A",
                "lepan | verb | to discuss | N/A",
                "iya iya | adverb | nicely | N/A",
            ]
        ),
        "output": "Tolong panara yau ehe me yau kewa yau pasala sale le ite bisa lepan iya iya.",
        "translation": "Please do not be angry with me yet; I know I was wrong, and we can discuss all of this calmly.",
    },
    {
        "word_candidates": "\n".join(
            [
                "meme | noun | uncle | N/A",
                "ti'i | verb | to pick | N/A",
                "ambalang | noun | mango | N/A",
                "huai | noun | fruit | N/A",
                "masusu | adjective | sweet | N/A",
                "le | preposition | at | N/A",
                "luma | noun | house | N/A",
                "mulingi | noun | back / behind | N/A",
                "si | verb | (does it) | N/A",
                "kana | verb | to take / grab | N/A",
                "kula | preposition | with | N/A",
                "akukut | noun | pole | N/A",
                "ata'li | adjective | long | N/A",
                "yang | pronoun | which | N/A",
                "una | verb | made | N/A",
                "he | preposition | from | N/A",
                "ute'e | noun | bamboo | N/A",
            ]
        ),
        "output": "Meme si ti'i ambalang huai masusu le luma mulingi, si kana kula akukut ata'li yang una he ute'e.",
        "translation": "Uncle picks sweet mango fruit behind the house using a long pole made of bamboo.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ena'i | conjunction | when | N/A",
                "kele hetu | verb | to wake up | N/A",
                "wa | preposition | at | N/A",
                "oros | noun | o'clock | N/A",
                "lima | numeral | five | N/A",
                "hekakau | noun | morning | N/A",
                "ma | determiner | that | N/A",
                "Andi | proper noun | Andi (person name) | N/A",
                "pa'iya | verb | to tidy up | N/A",
                "nawanga | noun | bed | N/A",
                "inu | verb | to drink | N/A",
                "wail | noun | water | N/A",
                "loto pariki | adjective | warm | N/A",
                "galas tai | noun | a glass of | N/A",
                "wusi | conjunction | then | N/A",
                "oi | verb | to go | N/A",
                "olahraga | noun | exercise | N/A",
            ]
        ),
        "output": "Ena'i kele hetu wa oros lima hekakau ma, Andi pai'ya nawanga, inu wailoto pariki'i galas tai wusi oi olahraga.",
        "translation": "When Andi woke up at five o'clock this morning, he tidied the bed, drank a glass of warm water, then went exercising.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mahina | noun | woman | N/A",
                "yang | pronoun | who | N/A",
                "ene | adverb | currently | N/A",
                "kolo | verb | sitting | N/A",
                "kula | preposition | while | N/A",
                "pake | verb | wearing | N/A",
                "lapun | noun | clothes | N/A",
                "kau | adjective | red | N/A",
                "ma | determiner | that | N/A",
                "nalang | verb | named | N/A",
                "Fatimah | proper noun | Fatimah (person name) | N/A",
                "ile | pronoun | she | N/A",
                "ma | verb | is | N/A",
                "yau | pronoun | my | N/A",
                "weteng | noun | niece / nephew | N/A",
            ]
        ),
        "output": "Mahina yang ene kolo kula pake lapun kau ma nalang Fatimah, ile ma yau weteng.",
        "translation": "The woman who is sitting while wearing a red shirt is named Fatimah; she is my niece.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ehe | negation | don't | N/A",
                "lepa | verb | to speak | N/A",
                "takaruang | adverb | carelessly | N/A",
                "me | adverb | first | N/A",
                "kalu | conjunction | if | N/A",
                "te | adverb | not | N/A",
                "kewa | verb | to know | N/A",
                "ing nyanesa | noun | the truth | N/A",
                "ma | pronoun | it | N/A",
                "hao | adverb | how | N/A",
                "biar | conjunction | so that | N/A",
                "te | adverb | not | N/A",
                "puna | verb | to become | N/A",
                "ena | conjunction | into | N/A",
                "fitnah | noun | slander | N/A",
            ]
        ),
        "output": "Ehe lepa takaruang me kalu te kewa ing nyanesa ma hao biar te puna ena fitnah.",
        "translation": "Do not speak carelessly if you do not yet know the truth, so that it does not become slander.",
    },
    {
        "word_candidates": "\n".join(
            [
                "karna | conjunction | because | N/A",
                "te | adverb | not | N/A",
                "kele | verb | to sleep | N/A",
                "lamata ketu | noun | daytime | N/A",
                "atolo | noun | night | N/A",
                "ing puna | verb | makes / causes | N/A",
                "yau | pronoun | I | N/A",
                "sosu | adjective | sleepy | N/A",
                "malali | adverb | quickly | N/A",
            ]
        ),
        "output": "Karna te kele nai lamata ketu, atolo ing puna yau sosu malali.",
        "translation": "Because I did not sleep during the day, I feel sleepy quickly at night.",
    },
    {
        "word_candidates": "\n".join(
            [
                "he | preposition | since | N/A",
                "koi koi | adjective | small (childhood) | N/A",
                "sala | adverb | repeatedly | N/A",
                "baba | noun | father | N/A",
                "panau | verb | to teach | N/A",
                "yami | pronoun | us | N/A",
                "wa | conjunction | that | N/A",
                "te | adverb | not | N/A",
                "boleh | verb | allowed | N/A",
                "pasosala | verb | to lie | N/A",
                "ena | preposition | to | N/A",
                "mansia | noun | people | N/A",
            ]
        ),
        "output": "He koi koi sala baba panau yami wa te boleh pasosala ena mansia.",
        "translation": "Since childhood, our father taught us that we must not lie to people.",
    },
    {
        "word_candidates": "\n".join(
            [
                "baba | noun | father | N/A",
                "kai | verb | to work | N/A",
                "leu | verb | to go home | N/A",
                "he | preposition | from | N/A",
                "kantor | noun | office | N/A",
                "sahi | verb | to buy | N/A",
                "ambalang | noun | mango | N/A",
                "huai | noun | fruit | N/A",
                "le | preposition | at | N/A",
                "toko | noun | shop | N/A",
                "ahasa | adjective | near | N/A",
                "lalan | noun | road | N/A",
                "ela | adjective | big / main | N/A",
                "wusi | conjunction | after | N/A",
                "taka | preposition | at | N/A",
                "alamasa | noun | afternoon | N/A",
            ]
        ),
        "output": "Baba kai leu he kantor sahi ambalang huai le toko ahasa lalan ela, kai leu he kantor wusi taka alamasa.",
        "translation": "Father works and goes home from the office, buys mangoes at a shop near the main road, then goes home from the office in the afternoon.",
    },
]
