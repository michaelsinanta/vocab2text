"""5-word few-shot examples for javanese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "tuku | verb | buy | Aku arep tuku buku anyar ing toko.",
                "woh | noun | fruit | Wit pelem iki wis wiwit metu wohe.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "pasar | noun | market | Ibu tindak dhateng pasar mundhut sayuran.",
            ]
        ),
        "output": "Aku tuku woh ing pasar.",
        "translation": "I buy fruit at the market.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ibu | noun | mother | Ibu tindak dhateng peken mundhut rasukan.",
                "masak | verb | to cook | Ibu lagi masak sega goreng ing pawon.",
                "sega | noun | cooked rice | Saben esuk aku sarapan sega pecel.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "tamu | noun | guest | Bapak nemoni tamu wonten ing ruang tamu.",
            ]
        ),
        "output": "Ibu masak sega kanggo tamu.",
        "translation": "Mother cooks rice for the guests.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bocah | noun | child | Bocah kuwi sregep banget sinau.",
                "lagi | adverb | currently | Bapak lagi dhahar wonten pawon.",
                "dolanan | noun | toy | Adhik tuku dolanan anyar ing pasar.",
                "bal | noun | ball | Bocah-bocah padha dolanan bal ing lapangan.",
            ]
        ),
        "output": "Bocah bocah lagi dolanan bal.",
        "translation": "The children are currently playing ball.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bapak | noun | father | Bapak tindak dhateng kantor.",
                "maca | verb | to read | Bapak lagi maca koran ing teras.",
                "koran | noun | newspaper | Bapak nembe maos koran wonten ing teras.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "teras | noun | terrace | Bapak lungguh ing teras omah.",
            ]
        ),
        "output": "Bapak maca koran ing teras.",
        "translation": "Father reads the newspaper on the terrace.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kucing | noun | cat | Kucing kuwi lagi turu ing dhuwur kursi.",
                "ireng | adjective | black | Kucing sing wernane ireng kuwi jenenge Si Manis.",
                "turu | verb | sleep | Adhik lagi turu ing kamar.",
                "cedhak | adjective | near | Omahku cedhak karo pasar.",
                "lawang | noun | door | Tulung tutupna lawang kuwi amarga udan.",
            ]
        ),
        "output": "Kucing ireng turu cedhak lawang.",
        "translation": "The black cat sleeps near the door.",
    },
    {
        "word_candidates": "\n".join(
            [
                "wong | noun | person | Wong iku lagi mlaku menyang pasar.",
                "nggawa | verb | bring | Aku nggawa buku menyang sekolah.",
                "kayu | noun | wood | Bapak lagi ngethok kayu nganggo kampak.",
                "saka | preposition | from | Bapak nembe kondur saka kantor.",
                "alas | noun | forest | Simbah golek kayu bakar ana ing alas.",
            ]
        ),
        "output": "Wong nggawa kayu saka alas.",
        "translation": "A person brings wood from the forest.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "mangan | verb | eat | Aku lagi mangan sega goreng.",
                "sega | noun | cooked rice | Aku lagi mangan sega goreng ing pawon.",
                "anget | adjective | warm | Aku seneng teh anget nalika hawa adhem.",
                "saiki | adverb | now | Saiki aku lagi mangan sega goreng.",
            ]
        ),
        "output": "Aku mangan sega anget saiki.",
        "translation": "I am eating warm rice now.",
    },
    {
        "word_candidates": "\n".join(
            [
                "simbah | noun | grandparent | Simbah nembe sare wonten kamar.",
                "lungguh | verb | sit | Bapak nembe lungguh wonten kursi ngajeng.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "kursi | noun | chair | Bapak lenggah wonten kursi kayu.",
                "kayu | noun | wood | Bapak lagi ngethok kayu nganggo kampak.",
            ]
        ),
        "output": "Simbah lungguh ing kursi kayu.",
        "translation": "Grandparent sits on a wooden chair.",
    },
    {
        "word_candidates": "\n".join(
            [
                "wong | noun | person | Wong iku lagi mlaku menyang pasar.",
                "iku | determiner | that | Buku iku duweke adhiku.",
                "mlaku | verb | walk | Aku mlaku menyang pasar saben esuk.",
                "nang | particle | how come | Kowe ka ora mangkat sekolah?",
                "kali | noun | river | Banyu kali iki katon bening banget.",
            ]
        ),
        "output": "Wong iku mlaku nang kali.",
        "translation": "That person is walking to the river.",
    },
    {
        "word_candidates": "\n".join(
            [
                "adhi | noun | younger sibling | Adhiku lagi sinau ing kamar.",
                "nulis | verb | write | Bapak nulis layang kanggo simbah.",
                "surat | noun | letter | Bapak nembe maos surat saking Pak Lurah.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "ibu | noun | mother | Ibu tindak dhateng peken mundhut rasukan.",
            ]
        ),
        "output": "Adhi nulis surat kanggo ibu.",
        "translation": "Younger sibling writes a letter for mother.",
    },
]
