"""10-word few-shot examples for javanese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "bapak | noun | father | Bapak tindak dhateng kantor.",
                "buru | verb | hunt | Bapak tindak alas badhe buru kidang.",
                "kidang | noun | barking deer | Kidang kencana mlayu mlebu ing tengah alas.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "alas | noun | forest | Kewan-kewan galak manggon ana ing tengah alas.",
                "nalika | conjunction | when | Nalika aku isih cilik, aku seneng dolanan layangan.",
                "esuk | noun | morning | Saben esuk bapak ngunjuk kopi.",
                "karo | conjunction | with | Bapak tindak dhateng peken karo Ibu.",
                "kanca | noun | friend | Budi iku kanca sekolahku wiwit SD.",
                "piyambak | adjective | alone | Bapak tindak dhateng Semarang piyambak.",
            ]
        ),
        "output": "Bapak berburu kidang ing alas nalika esuk karo kanca piyambak.",
        "translation": "Father hunts for barking deer in the forest in the morning with a friend alone.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "mung | adverb | only | Aku mung tuku buku siji.",
                "gadhah | verb | to have | Kula gadhah buku.",
                "dhuwit | noun | money | Dhuwit iki kanggo tuku jajan.",
                "sithik | numeral | a little | Aku mung njaluk sega sithik wae amarga isih wareg.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "tuku | verb | buy | Aku arep tuku buku anyar ing toko.",
                "klambi | noun | clothes | Bapak nembe mundhut klambi anyar ing pasar.",
                "anyar | adjective | new | Aku tuku klambi anyar.",
            ]
        ),
        "output": "Aku mung gadhah dhuwit sithik kanggo tuku klambi anyar.",
        "translation": "I only have a little money to buy new clothes.",
    },
    {
        "word_candidates": "\n".join(
            [
                "jobin | noun | floor | Simbah lagi ngepel jobin supaya resik.",
                "gelish | adjective | worried | Simbah ngeres amarga akeh bledug.",
                "amarga | conjunction | because | Aku ora mangkat sekolah amarga udan deres.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "bledug | noun | dust | Mejane kebak bledug amarga wis suwe ora diresiki.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "jero | adjective | deep | Sumur iki banyune isih jero banget.",
                "omah | noun | house | Omahku ana ing pinggir dalan gedhe.",
                "iki | pronoun | this | Buku iki duweke adhiku.",
            ]
        ),
        "output": "Jobin gelisah amarga kathah bledug ing jero omah iki.",
        "translation": "The floor is dirty because there is a lot of dust inside this house.",
    },
    {
        "word_candidates": "\n".join(
            [
                "klambi | noun | clothes | Bapak nembe mundhut klambi anyar ing pasar.",
                "gedhobroh | adjective | oversized | Klambine gedhobroh amarga kegedhen.",
                "amarga | conjunction | because | Aku ora mangkat sekolah amarga udan deres.",
                "ukuran | noun | measurement | Ukuran klambi iki kegedhen kanggo aku.",
                "ageng | adjective | big | Dalemipun Pak Lurah punika ageng sanget.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "awak | adjective | clear | Cahyane srengenge esuk iki katon awak banget.",
                "cilik | adjective | small | Omahku cilik nanging resik.",
            ]
        ),
        "output": "Klambi gedhobroh amarga ukuran ageng kanggo awak cilik.",
        "translation": "The clothes are oversized because the size is too big for a small body.",
    },
    {
        "word_candidates": "\n".join(
            [
                "adhi | noun | younger sibling | Adhiku lagi sinau ing kamar.",
                "sinau | verb | study | Aku lagi sinau basa Jawa supaya bisa lancar.",
                "sregep | adjective | diligent | Bocah kuwi sregep banget sinau supaya juara.",
                "supaya | conjunction | so that | Sinaua sing sregep supaya pinter.",
                "dadi | verb | become | Bocah kuwi saiki wis dadi guru.",
                "bocah | noun | child | Bocah kuwi sregep banget sinau.",
                "sing | pronoun | which/that | Iki buku sing daktuku wingi.",
                "pinter | adjective | smart | Bocah kuwi pancen pinter banget.",
                "banget | adverb | very | Panganan iki enak banget.",
            ]
        ),
        "output": "Adhi sregep sinau supaya dadi bocah sing pinter banget.",
        "translation": "Younger sibling studies diligently to become a very smart child.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ibu | noun | mother | Ibu tindak dhateng peken mundhut rasukan.",
                "kongkon | verb | to order | Bapak kongkon aku tuku rokok ing warung.",
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "mangan | verb | eat | Aku lagi mangan sega goreng.",
                "dhisik | adverb | first | Aku arep mangan dhisik.",
                "durung | adverb | not yet | Aku durung mangan awit mau esuk.",
                "lunga | verb | go | Aku arep lunga menyang pasar.",
                "dhateng | preposition | to | Kula ngaturaken dhateng panjenengan.",
                "sekolah | noun | school | Adhik mangkat sekolah numpak sepeda.",
            ]
        ),
        "output": "Ibu kongkon aku mangan dhisik sakdurunge lunga dhateng sekolah.",
        "translation": "Mother ordered me to eat first before going to school.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bocah | noun | child | Bocah kuwi sregep banget sinau.",
                "dolanan | noun | toy | Adhik tuku dolanan anyar ing pasar.",
                "layangan | noun | kite | Bocah-bocah dolanan layangan ing lapangan.",
                "nalika | conjunction | when | Nalika aku isih cilik, aku dolanan.",
                "dikongkon | verb | ordered | Bocah kuwi dikongkon ibune tuku uyah.",
                "sinau | verb | study | Aku lagi sinau basa Jawa.",
                "karo | conjunction | with | Bapak tindak dhateng peken karo Ibu.",
                "bapak | noun | father | Bapak tindak dhateng kantor.",
            ]
        ),
        "output": "Bocah dolanan layangan nalika dikongkon sinau karo bapak.",
        "translation": "The child plays with a kite when ordered to study by father.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "temu | verb | meet | Aku wingi temu kanca lawas.",
                "kanca | noun | friend | Budi iku kanca sekolahku.",
                "lawas | adjective | old | Omah lawas iku isih kokoh.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "pasar | noun | market | Ibu tindak dhateng pasar.",
                "nalika | conjunction | when | Nalika aku isih cilik...",
                "tuku | verb | buy | Aku arep tuku buku anyar.",
                "panganan | noun | food | Ibu mundhut panganan ing pasar.",
            ]
        ),
        "output": "Aku ketemu kanca lawas ing pasar nalika tuku panganan.",
        "translation": "I met an old friend at the market while buying food.",
    },
    {
        "word_candidates": "\n".join(
            [
                "petani | noun | farmer | Pak Sardi dadi tani.",
                "nggawa | verb | bring | Aku nggawa buku menyang sekolah.",
                "kayu | noun | wood | Bapak ngethok kayu nganggo kampak.",
                "saka | preposition | from | Bapak kondur saka kantor.",
                "alas | noun | forest | Simbah golek kayu bakar ing alas.",
                "nganggo | verb | use | Aku mangkat sekolah nganggo sepatu anyar.",
                "cikar | noun | cart | Sapi narik cikar isi panen.",
                "cilik | adjective | small | Omahku cilik nanging resik.",
            ]
        ),
        "output": "Petani nggawa kayu saka alas nganggo cikar cilik.",
        "translation": "The farmer brings wood from the forest using a small cart.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bocah | noun | child | Bocah kuwi sregep sinau.",
                "iku | determiner | that | Buku iku duweke adhiku.",
                "seneng | adjective | like/happy | Aku seneng mangan sega goreng.",
                "maca | verb | read | Bapak lagi maca koran.",
                "buku | noun | book | Aku tuku buku anyar.",
                "crita | noun | story | Bapak maca crita wayang.",
                "saben | determiner | every | Saben esuk aku sarapan.",
                "wengi | noun | night | Aku ora bisa turu yen wis wengi.",
            ]
        ),
        "output": "Bocah iku seneng maca buku crita saben wengi.",
        "translation": "That child likes to read storybooks every night.",
    },
]
