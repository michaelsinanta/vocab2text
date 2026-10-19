"""15-word few-shot examples for minangkabau.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "ambo | noun | I | ambo pai ka sikola",
                "mambali | verb | to buy | adiak pai mambali rokok",
                "baju | noun | shirt | manjaik baju",
                "baru | adjective | New | rumah baru badiri",
                "untuak | particle | for | untuak ambo",
                "abak | noun | father | itu abak den",
                "jo | adverb | and | letaknyo antaro bumi jo langik",
                "amak | noun | Mother | N/A",
                "di | particle | at / in | pitihnyo ilang di rumah",
                "pasa | noun | market | amak pai ka pasa",
                "ateh | preposition | up | baju di ateh lemari",
                "untuak | preposition | for | N/A",
                "persiapan | noun | preparation | N/A",
                "hari | noun | day | hari ko hari rayo",
                "rayo | noun | celebration | hari rayo",
            ]
        ),
        "output": "Ambo mambali baju baru untuak abak jo amak di pasa ateh untuak persiapan hari rayo.",
        "translation": "I bought new clothes for my father and mother at the Upper Market for the Eid celebration.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kawan | noun | friend | kawan den pai ka Kanada",
                "dakek | adjective | close | jarak kota Bukik jo Agam tu dakek",
                "ambo | noun | I | ambo pai ka sikola",
                "sakeluarga | adverb | along with family | inyo sakeluarga pai ka pasa",
                "jo | adverb | and | latakanya bak bumi jo langik",
                "anak-anaknyo | noun | his family | anak-anaknyo alah gadang",
                "pai | verb | go | inyo pai ka pasa",
                "ka | N/A | to | inyo pai ka pasa",
                "lua nagari | noun | overseas | N/A",
                "manampuah | verb | pursue | N/A",
                "pendidikan | noun | education | N/A",
                "S3 | noun | PhD | N/A",
                "di | preposition | in | N/A",
                "australia | noun | Australia | N/A",
            ]
        ),
        "output": "Kawan dakek ambo sakeluarga jo anak-anaknyo pai ka lua nagari manampuah pendidikan S3 di Australia.",
        "translation": "My close friend, along with his family and kids, moved overseas to pursue a PhD in Australia.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pas | conjunction | when | N/A",
                "mananam | verb | plant | N/A",
                "padi | noun | rice | N/A",
                "Dona | proper noun | Dona (person name) | N/A",
                "maliek | verb | see | N/A",
                "banyak | adjective | many | N/A",
                "taranak | noun | cattle | N/A",
                "lalu lalang | verb | going back and forth | N/A",
                "di pinggia | preposition | beside | N/A",
                "sawah | noun | rice field | N/A",
                "punyo | verb | possession | N/A",
                "mamak | noun | uncle from mother's family | N/A",
                "nyo | pronoun | her | N/A",
            ]
        ),
        "output": "Pas mananam padi, Dona maliek banyak taranak lalu lalang di pinggia sawah punyo mamak nyo.",
        "translation": "While planting rice, Dona saw many cattle beside his uncle’s rice field.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pak | noun | Sir | N/A",
                "Muncak | proper noun | Muncak (person name) | N/A",
                "mambawok | verb | drive | N/A",
                "oto | noun | car | N/A",
                "dari | preposition | from | N/A",
                "Padang | proper noun | Padang as the location | N/A",
                "ka | preposition | to | N/A",
                "Jakarta | proper noun | Jakarta as the location | N/A",
                "duo | numeral | two | N/A",
                "hari | noun | days | N/A",
                "tanpa | preposition | without | N/A",
                "baranti | verb | stop | N/A",
                "jo | preposition | with | N/A",
                "kawan | noun | friend | N/A",
                "baliau | pronoun | his | N/A",
            ]
        ),
        "output": "Pak Muncak mambawok oto dari Padang ka Jakarta duo hari tanpa baranti jo kawan baliau.",
        "translation": "Mr. Muncak drove a car from Padang to Jakarta for two days without stopping with his friend.",
    },
    {
        "word_candidates": "\n".join(
            [
                'si | article | No meaning, it\'s like "the" | N/A',
                "Feri | proper noun | Feri (person name) | N/A",
                "ko | determiner | this | N/A",
                "urang | noun | person | N/A",
                "nyo | pronoun | he | N/A",
                "pamaleh | adjective | lazy | N/A",
                "bana | adverb | very | N/A",
                "kalau | conjunction | if | N/A",
                "disuruah | verb | asked | N/A",
                "mangarajoan | verb | doing | N/A",
                "sesuatu | pronoun | something | N/A",
                "ado | pronoun | there (is) | N/A",
                "se | adverb | any | N/A",
                "alasan | noun | reason | N/A",
                "nyo | pronoun | his | N/A",
            ]
        ),
        "output": "Si Feri ko urang nyo pamaleh bana, kalau disuruah mangarajoan sesuatu ado se alasan nyo.",
        "translation": "Feri is a very lazy person, if he is asked to do something he always has an excuse.",
    },
    {
        "word_candidates": "\n".join(
            [
                "amak | noun | mother | N/A",
                "samo | conjunction | and | N/A",
                "apak | noun | father | N/A",
                "alah | adverb | have | N/A",
                "banyak | adjective | many | N/A",
                "berkorban | verb | sacrificed | N/A",
                "manggadaian | verb | selling | N/A",
                "sawah | noun | rice field | N/A",
                "jo | conjunction | and | N/A",
                "tanah | noun | land | N/A",
                "untuak | preposition | for | N/A",
                "mambiayai | verb | pay | N/A",
                "pitih | noun | fee | N/A",
                "kuliah | noun | college | N/A",
                "awak | pronoun | my | N/A",
            ]
        ),
        "output": "Amak samo apak alah banyak berkorban manggadaian sawah jo tanah untuak mambiayai pitih kuliah awak.",
        "translation": "My mother and father have sacrificed a lot by selling their rice fields and land to pay for my college fees.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pak | noun | Sir | N/A",
                "bupati | noun | regent | N/A",
                "manjalehan | verb | explain | N/A",
                "kalau | conjunction | that | N/A",
                "dalam | preposition | in | N/A",
                "duo | numeral | two | N/A",
                "tahun | noun | year | N/A",
                "ko | determiner | this | N/A",
                "akan | adverb | will | N/A",
                "ado | pronoun | there (is) | N/A",
                "pembangunan | noun | construction | N/A",
                "musajik | noun | mosque | N/A",
                "baru | adjective | new | N/A",
                "di | preposition | in | N/A",
                "kampuang | noun | village | N/A",
            ]
        ),
        "output": "Pak Bupati manjalehan kalau dalam duo tahun ko akan ado pembangunan musajik baru di kampuang.",
        "translation": "The Regent explained that in the next two years there will be construction of a new mosque in the village.",
    },
    {
        "word_candidates": "\n".join(
            [
                "politik | noun | politics | N/A",
                "negara | noun | country | N/A",
                "awak | pronoun | my | N/A",
                "ko | determiner | this | N/A",
                "alah | adverb | have | N/A",
                "kacau | adjective | chaos | N/A",
                "dek | preposition | because | N/A",
                "terlalu | adverb | too | N/A",
                "banyak | adjective | many | N/A",
                "bana | adverb | very | N/A",
                "urang | noun | people | N/A",
                "nan | pronoun | that | N/A",
                "korupsi | adjective | corrupt | N/A",
                "di | preposition | in | N/A",
                "pemerintahan | noun | government | N/A",
            ]
        ),
        "output": "Politik negara awak ko alah kacau dek terlalu banyak bana urang nan korupsi di pemerintahan.",
        "translation": "Our country's politics is in chaos because there are too many corrupt people in the government.",
    },
    {
        "word_candidates": "\n".join(
            [
                "indak | adverb | none | N/A",
                "sado | determiner | all | N/A",
                "urang | noun | people | N/A",
                "bisa | auxiliary verb | can | N/A",
                "sakolah | verb | go to school | N/A",
                "tinggi | adjective | high | N/A",
                "sarjana | noun | bachelor degree | N/A",
                "master | noun | master degree | N/A",
                "sampai | preposition | until | N/A",
                "doktor | noun | PhD | N/A",
                "jadi | conjunction | so | N/A",
                "harus | auxiliary verb | must | N/A",
                "bisa | auxiliary verb | can | N/A",
                "banyak | adverb | very | N/A",
                "bersyukur | adjective | grateful | N/A",
            ]
        ),
        "output": "Indak sado urang bisa sakolah tinggi, sarjana, master sampai doktor, jadi harus bisa banyak bersyukur.",
        "translation": "Not everyone can go to college, get a bachelor's degree, master's degree or doctorate, so we have to be very grateful.",
    },
    {
        "word_candidates": "\n".join(
            [
                "dek | preposition | because | N/A",
                "ulah | noun | actions | N/A",
                "Pratono | proper noun | Pratono (person name) | N/A",
                "Indonesia | proper noun | Indonesia | N/A",
                "lah | adverb | have | N/A",
                "ampia | adverb | almost | N/A",
                "bangkrut | adjective | bankrupt | N/A",
                "dan | conjunction | and | N/A",
                "banyak | adjective | many | N/A",
                "urang-urang | noun | people | N/A",
                "santiang | adjective | smart | N/A",
                "lari | verb | run | N/A",
                "ka | preposition | to | N/A",
                "lua nagari | noun | overseas | N/A",
            ]
        ),
        "output": "Dek ulah Pratono, Indonesia lah ampia bangkrut dan banyak urang-urang santiang lari ka lua nagari.",
        "translation": "Because of Pratono's actions, Indonesia is almost bankrupt and many smart people have fled abroad.",
    },
]
