"""10-word few-shot examples for minangkabau.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "ambo | pronoun | I | ambo pai ka sikola",
                "sakeluarga | adverb | with all family | N/A",
                "sadang | adverb | currently | inyo sadang makan",
                "makan | verb | eat | makan ubi",
                "nasi | noun | rice | N/A",
                "jo | preposition | with | N/A",
                "randang | noun | beef with coconut seasons | N/A",
                "dan | conjunction | and | N/A",
                "baluik | noun | eel | N/A",
                "goreng | adjective | fried | N/A",
            ]
        ),
        "output": "Ambo sakeluarga sadang makan nasi jo randang dan baluik goreng.",
        "translation": "I and my whole family are currently eating rice with rendang and fried eel.",
    },
    {
        "word_candidates": "\n".join(
            [
                "inyo | pronoun | he | N/A",
                "mambali | verb | buy | adiak pai mambali rokok",
                "baju | noun | dress | manjaik baju",
                "baru | adjective | new | rumah baru badiri",
                "bawarna | adjective | coloured | N/A",
                "sirah | adjective | red | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "toko | noun | shop | toko batingkek",
                "kawan | noun | friend | N/A",
                "awak | pronoun | our | daerah kito",
            ]
        ),
        "output": "Inyo mambali baju baru bawarna sirah di toko kawan awak.",
        "translation": "He bought a new red shirt at our friend's shop.",
    },
    {
        "word_candidates": "\n".join(
            [
                "awak | pronoun | 1 i; 2 us; 3 us | N/A",
                "baraja | verb | study | N/A",
                "bahasa | noun | language | bahasa Minangkabau",
                "korea | noun | Korea | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "tampek | noun | place | N/A",
                "kursus | noun | course | N/A",
                "nan | pronoun | that is | N/A",
                "baru | adverb | recent | N/A",
                "tagak | adjective | built | N/A",
            ]
        ),
        "output": "Awak baraja bahasa korea di tampek kursus nan baru tagak.",
        "translation": "We study Korean at the newly established course place.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pas | conjunction | when | N/A",
                "awak | pronoun | we | N/A",
                "tagak | verb | stand | N/A",
                "di | preposition | in | N/A",
                "labuah | noun | highway | labuah panjang",
                "banyak | adjective | lots | datanglah urang banyak",
                "urang | noun | people | N/A",
                "nan | pronoun | who is | N/A",
                "manggaleh | verb | sell | N/A",
                "durian | noun | durian | N/A",
            ]
        ),
        "output": "Pas awak tagak di labuah banyak urang nan manggaleh durian.",
        "translation": "When we stand on the highway, many people are selling durian.",
    },
    {
        "word_candidates": "\n".join(
            [
                "apak | noun | dad | N/A",
                "suko | verb | like | N/A",
                "bana | adverb | very much | N/A",
                "minum | verb | drink | minum aia",
                "kopi | noun | coffee | untuak pambali kopi sajo",
                "manih | adjective | sweet | N/A",
                "angek | adjective | hot | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "pagi | noun | morning | N/A",
                "hari | noun | day | N/A",
            ]
        ),
        "output": "Apak suko bana minum kopi manih angek di pagi hari.",
        "translation": "Father really likes drinking hot sweet coffee in the morning.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ayam | noun | chicken | N/A",
                "nan | pronoun | that is | N/A",
                "dilapehan | verb | released | N/A",
                "tadi | adverb | earlier / just now | N/A",
                "pagi | noun | morning | N/A",
                "banyak | adjective | many | N/A",
                "bakumpua | verb | gather | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "muko | noun | front | N/A",
                "rumah | noun | house | N/A",
            ]
        ),
        "output": "Ayam nan dilapehan tadi pagi banyak bakumpua di muko rumah.",
        "translation": "The chickens released this morning are gathering in front of the house.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kadai | noun | shop | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "muko | noun | front | N/A",
                "rumah | noun | house | N/A",
                "pak | noun | Sir | N/A",
                "datuak | noun | well-respected man / traditional chief | N/A",
                "kini | adverb | now | N/A",
                "alah | adverb | already / has been | N/A",
                "tutuik | adjective | closed | N/A",
                "permanen | adjective | permanent | N/A",
            ]
        ),
        "output": "Kadai di muko rumah Pak Datuak kini alah tutuik permanen.",
        "translation": "The shop in front of Pak Datuak's house is now permanently closed.",
    },
    {
        "word_candidates": "\n".join(
            [
                "nan | pronoun | the one which / that | N/A",
                "tarakhir | adjective | last | N/A",
                "dikarajoan | verb | done | N/A",
                "dalam | preposition | in | N/A",
                "bawuduak | verb | perform ablution | N/A",
                "adolah | verb | is | N/A",
                "mambasuah | verb | wash | mambasuah piriang",
                "kaki | noun | feet (part of the body) | bola tu disipaknyo jo kaki",
                "dan | conjunction | and | N/A",
                "badoa | verb | pray | N/A",
            ]
        ),
        "output": "Nan tarakhir dikarajoan dalam bawuduak adolah mambasuah kaki dan badoa.",
        "translation": "The last thing done in ablution is washing the feet and praying.",
    },
    {
        "word_candidates": "\n".join(
            [
                "koncek | noun | frog / toad | N/A",
                "baranang | verb | swim | N/A",
                "di | preposition | in | pitihnyo ilang di rumah",
                "kolam | noun | pool | N/A",
                "samantaro | conjunction | while | N/A",
                "ayam | noun | chicken | ayam batalua di padi mati kalaparan ki",
                "mamatuak | verb | peck | N/A",
                "makanan | noun | food | N/A",
                "dari | preposition | from | N/A",
                "tanah | noun | ground / soil | N/A",
            ]
        ),
        "output": "Koncek baranang di kolam samantaro ayam mamatuak makanan dari tanah.",
        "translation": "A frog is swimming in the pond while chickens peck food from the ground.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bini | noun | wife | N/A",
                "awak | pronoun | my | N/A",
                "sadang | adverb | currently / in the process of | N/A",
                "manganduang | verb | pregnant / carrying a child | N/A",
                "sambilan | numeral | nine | N/A",
                "bulan | noun | month | N/A",
                "dan | conjunction | and | N/A",
                "inyo | pronoun | she | N/A",
                "acok | adverb | frequently | N/A",
                "muntah-muntah | verb | vomiting | N/A",
            ]
        ),
        "output": "Bini awak sadang manganduang sambilan bulan dan inyo acok muntah-muntah.",
        "translation": "My wife is seven months pregnant and she often vomits.",
    },
]
