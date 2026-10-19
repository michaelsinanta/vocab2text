"""15-word few-shot examples for acehnese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "tiep | particle | every | N/A",
                "uroe | noun | day | sigo jumat na tujoh uroe",
                "aleuhat | noun | Sunday | uroe aleuhat",
                "kamoe | pronoun | we/us | Kamoe jak u meunasah",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | Lon jak u keudè",
                "peukan | noun | market | uroe nyoe, peukan rame that",
                "ngen | particle | with, same, together | aneuk nyan jijak ngen yahjih u lampoh",
                "ayah | noun | father | N/A",
                "keu | particle | for | N/A",
                "bloe | verb | to buy | ibu jak u peukan geuneuk bloe manok",
                "eungkôt | noun | fish | N/A",
                "ngen | particle | with | N/A",
                "gulé | noun | curry | N/A",
            ]
        ),
        "output": "Tiep uroe aleuhat, kamoe jak u peukan ngen ayah keu bloe eungkot ngen gule.",
        "translation": "Every Sunday, we go to the market with father to buy fish with curry.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kupi | noun | coffee | kupi nyoe phet that",
                "itam | adjective | black | guda bulèe itam",
                "mangat | adjective | delicious | mangat that boh panah nyoe",
                "that | adverb | very | rayek that",
                "meunyoe | particle | if | N/A",
                "ta | pronoun | we/us | ta duek meusigoe",
                "Jép | verb | to drink | jep ie mameh tiep uroe hana get",
                "di | preposition | at; in | na bu di sikula",
                "seupot | noun | afternoon | ka seupot ka jeut wo",
                "uroe | noun | time / daytime | uroe trang buleuen",
                "sira | particle | while | jih jipeugah sira jibri paket nyan",
                "deungo | verb | hear | lon deungo ureueng tuha awak nyan ka meucrèe",
                "haba | noun | talk | habajih hanjeut tapatéh",
                "rakan | noun | friend | N/A",
            ]
        ),
        "output": "Kupi itam mangat that meunyoe ta jép di seupot uroe sira ta deungo haba rakan.",
        "translation": "Black coffee is so delicious if we drink it in the afternoon while listening to friends talking.",
    },
    {
        "word_candidates": "\n".join(
            [
                "meunyoe | particle | if | N/A",
                "Ujeuen | noun | rain | Ujeuen raya that",
                "brat | adjective | severe | Saket nyan brat",
                "teuka | verb | to come | N/A",
                "seupot | noun | afternoon | ka seupot ka jeut wo",
                "nyoe | particle | this | N/A",
                "geutanyoe | pronoun | we | geutanyoe inong, peubuet bak teumpat agam",
                "piyoh | verb | to stop | ka dua buluen lon piyoh bak keurija",
                "manteng | adverb | only | lôn tanyong manteng",
                "bak | particle | with, at | suratjih na bak lôn",
                "rumoh | noun | house | N/A",
                "bék | particle | do not | bek meunan tapubuet!",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "ho | adverb | where | ho ka jak?",
            ]
        ),
        "output": "Meunyo ujeuen brat teuka seupot nyoe, geutanyoe piyoh manteng bak rumoh bék jak ho-ho.",
        "translation": "If heavy rain comes this afternoon, let's just stop at home, don't go anywhere.",
    },
    {
        "word_candidates": "\n".join(
            [
                "abusyik | noun | grandfather | abusyik ka tuha",
                "nyang | particle | who | ureueng nyang get até",
                "jaga | verb | to watch over | lon jaga blang jih nyang na di gampong nyoe",
                "kalôn | verb | to see | N/A",
                "peureuno | verb | to teach | N/A",
                "ngen | verb | along with | neuk jipubloe saboh rumoh ngen lampoh-lampohjih",
                "ato | verb | arrange | awaknyoe ato kueh",
                "bandum | adverb | all together | N/A",
                "hai | noun | thing | hai-hai nyang harus ta pahami",
                "meulaot | verb | go to sea | ayah geu jak meulaot",
                "bak | particle | with, at | suratjih na bak lôn",
                "daerah | noun | area | daerah nyoe makmu",
                "nyoe | particle | this | N/A",
            ]
        ),
        "output": "Abusyik nyang jaga, nyang kalôn, nyang peureuno, ngen ato bandum hai meulaot bak daerah nyoe.",
        "translation": "It is Grandpa who guards, supervises, teaches, and manages everything related to marine activities in this area.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aneuk muda | noun | youth | N/A",
                "jameun jinoe | noun | modern era | N/A",
                "galak | verb | like/love | Lon galak pajôh kuéh.",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "bak | particle | with, at | suratjih na bak lôn",
                "keudé kupi | noun | cafe | N/A",
                "keu | particle | for | N/A",
                "Jép | verb | to drink | jep ie mameh tiep uroe hana get",
                "kupi | noun | coffee | kupi nyoe phet that",
                "susu | noun | milk | susu jampu kupi",
                "ngen | particle | with, same, together | aneuk nyan jijak ngen yahjih u lampoh",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "Kuéh | noun | cookies | Kuéh nyan manéh.",
            ]
        ),
        "output": "Aneuk muda jameun jinoe galak jak bak keudé kupi keu jep kupi susu ngen pajoh kuéh.",
        "translation": "Young people nowadays like to go to coffee shops to drink milk coffee and eat cakes.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ma | noun | mother | N/A",
                "ngen | particle | with | N/A",
                "ayah | noun | father | N/A",
                "lôn | pronoun | I | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "lampôh | noun | garden | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "keu | particle | for | N/A",
                "kalon | verb | to look closely at | N/A",
                "cicém | noun | bird | cicém nyan lagak",
                "nyang | particle | which | N/A",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "jagông | noun | corn | N/A",
            ]
        ),
        "output": "Ma ngen ayah lôn jak u lampôh beungoh nyoe keu neukalon cicém nyang pajoh jagông.",
        "translation": "My mother and father go to the plantation this morning to inspect for birds feeding on the corn",
    },
    {
        "word_candidates": "\n".join(
            [
                "aduen | noun | elder sibling | N/A",
                "lôn | pronoun | I | N/A",
                "ngen | particle | with | N/A",
                "adoe | noun | younger sibling | N/A",
                "duek | verb | stay | duek bak rumoh",
                "lam | particle | in | N/A",
                "rumoh | noun | house | N/A",
                "watѐe | noun | time | watѐe nyan ka",
                "malam | noun | night | N/A",
                "sabab | noun | because of | N/A",
                "tuboh | noun | body | N/A",
                "droeneuh | pronoun | they | N/A",
                "hék | adjective | tired | lôn hék that, ban lônwoe dari peukan",
                "that | adverb | very | rayek that",
            ]
        ),
        "output": "Aduen lôn ngen adoe lôn duek lam rumoh watèe malam sabab tuboh droeneuh hék that.",
        "translation": "My older sister and my younger sister stay at home during the night because their bodies are exhausted",
    },
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "teungoh | adverb | in the middle of | lôn teungoh meurunoe",
                "peugot | verb | to do / to perform | jih jipeugot buet jih ngen get;",
                "penelitian | noun | research | penelitian lôn",
                "gurèe | noun | teacher | N/A",
                "nyang | particle | which | N/A",
                "na | verb | exist/be | na ie lam glah",
                "hubungan | noun | connection | na hubungan ngon diabetes",
                "ngen | particle | with | N/A",
                "panyaket | noun | disease | panyaket kurap",
                "diabetes | noun | diabetes | panyaket diabetes",
                "bak | particle | with, at | suratjih na bak lôn",
                "rumoh saket | noun | hospital | Gobnyan geuba u rumoh sakét",
            ]
        ),
        "output": "Lôn teungoh peugöt penelitian gurèe lôn nyang na hubungan ngen panyaket diabetes bak rumoh saket.",
        "translation": "I am doing my lecturer's research that is related to diabetes in the hospital",
    },
    {
        "word_candidates": "\n".join(
            [
                "ayah | noun | father | N/A",
                "lôn | pronoun | I | N/A",
                "galak | verb | like/love | lôn galak pajôh kuéh",
                "that | adverb | very | rayek that",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "pasi | noun | shore | kamoe jak u pasi",
                "ngen | particle | with | N/A",
                "rakan | noun | friend | N/A",
                "gobnyan | pronoun | he, she, it | pakon jih (gobnyan, droeneuhnyan) beungéh",
                "tip | adjective | every | tip uroe awak nyan jimeukat bak peukan",
                "uroe | noun | day | sigo jumat na tujoh uroe",
                "aleuhat | noun | Sunday | uroe aleuhat",
                "kawé | verb | fish | neukawé bing",
                'eungkôt | noun | fish | N/A"',
            ]
        ),
        "output": "Ayah lôn galak that jak u pasi ngen rakan gobnyan tip uroe aleuhat neukawé eungkôt.",
        "translation": "My father loves to go the to shore with his friends every sunday to go fishing",
    },
    {
        "word_candidates": "\n".join(
            [
                "ma | noun | mother | N/A",
                "lôn | pronoun | I | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "pasai | noun | market | mak jak u pasai",
                "ngen | particle | with | N/A",
                "adék | noun | younger sibling | N/A",
                "neuk | N/A | to want to | lon neuk pajoh bu",
                "bloe | verb | to buy | ibu jak u peukan geuneuk bloe manok",
                "ie | noun | water | alue nyoe ubiet that ie",
                "u | noun | coconut | N/A",
                "keu | particle | for | N/A",
                "buka puasa | verb | break the fast | kamoe buka puasa",
            ]
        ),
        "output": "Ma lôn jak u pasai ngen adék lôn neuk bloe ie u keu buka puasa.",
        "translation": "My mother goes to the market with my younger brother to buy coconut water for breaking the fast",
    },
]
