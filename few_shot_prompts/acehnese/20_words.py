"""20-word few-shot examples for acehnese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "sikula | noun | school | Lon jak sikula",
                "di | preposition | at; in | na bu di sikula",
                "gampông | noun | village | N/A",
                "peureulèe | noun | need | adoe peureulèe buku",
                "leubèh | adverb | more | leubèh get meja nyoe",
                "le | adjective | many | le ureueng bak kanto nyan",
                "gurèe | noun | teacher | N/A",
                "ngen | particle | with | N/A",
                "buku | noun | book | puduek buku bak ateuh meja",
                "mangat | conjunction | so that | lon peugleh naleung mangat get ta kalon",
                "aneuk | noun | child | ka na aneuk",
                "jeut | verb | able to | lon jeut jak",
                "meurunoe | verb | to study | N/A",
                "ngen | particle | with | N/A",
                "get | adjective | proper | N/A",
            ]
        ),
        "output": "Sikula-sikula di gampông peureulee leubèh le gurèe ngen buku mangat aneuk-aneuk jeut meurunoe ngen get.",
        "translation": "Schools in the village need more teachers and books so children can learn well.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ureueng | noun | person | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | Lon jak u keudè",
                "laôt | noun | sea | laôt nyan le eungkôt",
                "yôh | particle | when | yôh droen trok, lôn teungoh manoe",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "suboh | noun | dawn | N/A",
                "dan | preposition | and | adoe dan aduen",
                "wôe | verb | return | lon jak wôe gampông",
                "watèe | noun | time | hana sidroe pih nyang teupeu, peu nyang akan terjadi bak watèe ukeu",
                "seupot | noun | afternoon | ka seupot ka jeut wo",
                "ba | verb | to bring | gobnyan geuba kamuih basa Aceh u kantou",
                "eungkôt | noun | fish | N/A",
                "keu | particle | for | N/A",
                "meukat | verb | to trade | ma geumeukat di peukan",
                "bak | particle | with, at | suratjih na bak lôn",
                "peukan | noun | market | uroe nyoe, peukan rame that",
                "singoh | adverb | tomorrow | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
            ]
        ),
        "output": "Ureueng jak u laôt yôh beungoh subôh dan wôe watèe seupot ba eungkot keu geumeukat bak peukan singoh beungoh.",
        "translation": "People who go to sea during early hours of dawn and return in the afternoon bring fish to sell at the market the next day.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aneuk miet | noun | child aged 3 to 12 years old | N/A",
                "nyan | demonstrative pronoun | that | Rumoh nyan lagak",
                "ka | abbreviation | already | uroe ka seupôt",
                "teuduek | verb | to sink down into a sitting position | jih ka teuduek lam sagoe",
                "bak | particle | with, at | suratjih na bak lôn",
                "binèh | noun | edge | ka puduek bak binèh manteng",
                "lampôih | noun | garden | N/A",
                "reuoh | noun | sweat | lon le that teubiet reuoh",
                "ka | abbreviation | already | uroe ka seupôt",
                "basah | adjective | wet | bék meu'en ujeuen euntreuk basah",
                "bak | particle | with, at | suratjih na bak lôn",
                "saboh | numeral | a piece of | N/A",
                "badan | noun | body | N/A",
                "ayah | noun | father | N/A",
                "lon | noun | myself | N/A",
                "teuseunyôm | verb | to smile | N/A",
                "kalôn | verb | to see | N/A",
                "nyan | demonstrative pronoun | that | Rumoh nyan lagak",
            ]
        ),
        "output": "Aneuk miet nyan ka teuduek bak binèh lampôih. Reuoh ka basah bak saboh badan. Ayah lon teuseunyôm kalôn aneuk miet nyan.",
        "translation": "The children were already sitting at the edge of the garden. Sweat drenched their entire bodies. My father smiled as he looked at the children.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aneuk muda | noun | youth | N/A",
                "di | preposition | at; in | na bu di sikula",
                "gampông | noun | village | N/A",
                "nyan | demonstrative pronoun | that | Rumoh nyan lagak",
                "meurunoe | verb | to study | N/A",
                "meugoë | verb | farming | nek lon meugoë bak blang",
                "nibak | particle | from | N/A",
                "ureueng chik | noun | parents | N/A",
                "awaknyan | noun | they | awaknyan aneuk muda mandum",
                "mangat | conjunction | so that | lon peugleh naleung mangat get ta kalon",
                "tradisi | noun | tradition | tradisi jameun dilee",
                "hana | adverb | not | han turi makajih hana sayang",
                "gadoh | verb | to disappear | ureueng nyan ka padum uroe gadoh?",
            ]
        ),
        "output": "Aneuk muda di gampông nyan meurunoe meugoë nibak ureueng chik awaknyan mangat tradisi meugoë hana gadoh.",
        "translation": "Young people in that village learn to farm from their parents so that the farming tradition won't be lost.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tiep | particle | every | N/A",
                "na | verb | exist | N/A",
                "khanduri | noun | feast | singoh na khanduri blang",
                "adat | noun | custom | adat bak po teumeureuhom",
                "bandum | adverb | all together | N/A",
                "rakyat | noun | people | rakyat Pakistan",
                "gampông | noun | village | N/A",
                "sapat | verb | assemble | jeut ta jak meunyoe mandum ka meusapat",
                "keu | particle | for | N/A",
                "bantu | noun | assistance | jih jitrimong geunaséh keu ureueng siblah rumohjih sabab ka geubantu jih",
                "po | noun | owner | ho po rumoh nyoe?",
                "mangat | conjunction | so that | lon peugleh naleung mangat get ta kalon",
                "bagah | adjective | fast | jak bagah",
                "lheuh | verb | finish | lon ka lheuh jak kanto",
                "dan | preposition | and | adoe dan aduen",
                "jeut | verb | able to | lon jeut jak",
                "meurayakan | verb | to celebrate | meurayakan uroe asyura",
                "rame | adverb | together | kueh nyan ta peugot rame-rame",
            ]
        ),
        "output": "Tiep na khanduri adat, bandum rakyat gampông meusapat keu bantu po khanduri mangat bagah lheuh dan jeut meurayakan rame-rame.",
        "translation": "Whenever there's a custom ceremony, all the villagers gather to help the host so it can be finished quickly and celebrated together.",
    },
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "pajoh | verb | to eat | jih jipajoh bu siuroe lhee go",
                "gulèe | noun | curry | gulèe nyan mangat",
                "eungkôt nila | noun | tilapia | lôn pajôh eungkôt nila",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "nyoe | particle | this | N/A",
                "sabab | noun | because of | N/A",
                "deuek | adjective | hungry | pruet lôn deuek, bu hana le",
                "that | adverb | very | rayek that",
                "adoe | noun | younger sibling | N/A",
                "hana | adverb | not | han turi makajih hana sayang",
                "ka | abbreviation | already | uroe ka seupôt",
                "bloe | verb | to buy | ibu jak u peukan geuneuk bloe manok",
                "kuéh seupet | noun | egg roll | kuéh seupet nyan mangat",
            ]
        ),
        "output": "Lôn pajoh gulèe eungkot nila beungoh nyoe sabab lôn deuek that, adoe lôn hana pajoh sabab ka geubloe kuéh seupet.",
        "translation": "I ate the tilapia curry because I was really hungry, but my younger sibling didn't eat because she had already bought egg roll",
    },
    {
        "word_candidates": "\n".join(
            [
                "uroe | noun | day | sigo jumat na tujoh uroe",
                "nyoe | particle | this | N/A",
                "ujeuen | noun | rain | ujeuen raya that",
                "raya | adjective | big | N/A",
                "that | adverb | very | rayek that",
                "lôn | pronoun | I | N/A",
                "hana | adverb | not | han turi makajih hana sayang",
                "jeut | verb | able to | lôn jeut jak",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "sikula | noun | school | lôn jak sikula",
                "sabab | noun | because of | N/A",
                "jalan | noun | road | hana jalan",
                "ngob | adjective | flooded | N/A",
                "ngen | particle | with | N/A",
                "ie | noun | water | alue nyoe ubiet that ie",
                "nyang | particle | which | N/A",
                "manteung | adverb | still | gobnyan manteung lam rumoh",
            ]
        ),
        "output": "Uroe nyoe ujeuen raya that, lôn hana jeut jak u sikula sabab jalan ngob ngen ie ujeuen nyang manteung raya.",
        "translation": "Today it is raining very heavily, so I cannot go to the school because the road is still flooded by heavy rainwater.",
    },
    {
        "word_candidates": "\n".join(
            [
                "lôn | pronoun | I | N/A",
                "ngen | particle | with | N/A",
                "rakan | noun | friend | N/A",
                "meurunoe | verb | to study | N/A",
                "basa aceh | noun | acehnese | gobnyan galak basa aceh",
                "bak | particle | with, at | suratjih na bak lôn",
                "pustaka | noun | library | pustaka bak sikula",
                "kamoe | pronoun | we, us | kamoe jak u meunasah",
                "hana | adverb | not | han turi makajih hana sayang",
                "jeut | verb | become, be | jeut keu guru",
                "lalè | adjective | neglectful | N/A",
                "sabab | noun | because of | N/A",
                "ujian | noun | exam / test | singoh na ujian matematik",
                "akhé | noun | end | N/A",
                "semester | noun | term | N/A",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "ka | abbreviation | already | uroe ka seupôt",
                "toe | preposition | close | rumoh lôn toe pasai",
            ]
        ),
        "output": "Lôn ngen rakan lôn meurunoe basa aceh bak pustaka, kamoe hana jeut lalè sabab ujian akhé semester nyoe ka to.",
        "translation": "Me and my friends study Acehnese at the library, we can't be careless because the final exam is approaching.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ayah | noun | father | N/A",
                "lôn | pronoun | I | N/A",
                "jak | verb | to go to | kamoe meujak u rumoh kepala sikula",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "lampôh | noun | garden | N/A",
                "beungoh | noun | morning | jih jibeudoh poh 05.00 beungoh",
                "nyoe | pronoun | this | nyoe rumoh lon",
                "keu | particle | for | N/A",
                "kalon | verb | to look closely at | N/A",
                "bak | noun | tree | bak mamplam",
                "kayèe | noun | timber | kayèe nyan manyang",
                "geutah | noun | sap, latex, gum | N/A",
                "adoe | noun | younger sibling | N/A",
                "tulong | noun | assistance | jih jitrimong geunaséh keu ureueng siblah rumohjih sabab ka geubantu jih",
                "peugot | verb | to do / to perform | jih jipeugot buet jih ngen get;",
                "buët | noun | work | buët nyan brat",
                "sampoe | particle | until | N/A",
                "abéh | verb | finished | bék talakèe lé, ka habéh",
                "meugréb | noun | sunset prayer time | jih trok u Jakarta kurap meugréb",
            ]
        ),
        "output": "Ayah lôn geujak u lampôh beungoh nyoe keu neukalon bak kayèe geutah, adoe lôn geutulong peugot buët sampoe abéh meugréb.",
        "translation": "My father went to the plantation this morning to look after the rubber trees, my younger brother helped with the work until dawn.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tu | noun | grandfather | tu lôn geuturi haba.",
                "lôn | pronoun | I | N/A",
                "ba | verb | to bring | tulong ba tah nyoe!",
                "u | preposition | to | kamoe meujak u rumoh sikula",
                "rumoh sakét | noun | hospital | gobnyan geuba u rumoh sakét",
                "sabab | noun | because of | N/A",
                "gula darah | noun | blood sugar | gula darah ma lôn",
                "that | adverb | very | rayek that",
                "brat | adjective | severe | saket nyan brat",
                "ék | verb | to rise | produksi breueh jiék",
                "jinoe | adverb | now | jinoe lon sibuk",
                "gobnyan | pronoun | he, she, it | pakon jih (gobnyan, droeneuhnyan) beungéh",
                "ka | abbreviation | already | uroe ka seupôt",
                "lam | particle | in | N/A",
                "kama | noun | room | gobnyan lam kama",
                "operasi | noun | surgery; operation | peunyakét ginjal nyang gohlom parah jeut jipeupuléh hana payah operasi",
            ]
        ),
        "output": "Tu lôn jiba u rumoh saket sabab gula darah gobnyan that brat jiék, jinoe gobnyan ka lam kama operasi.",
        "translation": "My grandfather was taken to the hospital due to high blood sugar level, now he's in the operation room.",
    },
]
