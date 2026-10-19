"""15-word few-shot examples for javanese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "para | determiner | the (plural marker for people) | Para tamu sampun sami rawuh ing adicara punika.",
                "warga | noun | citizen / member | Saben warga kudu njaga karesikan lingkungan.",
                "padha | adjective | same, equal, or plural marker | Bocah-bocah kuwi padha dolanan ing lapangan.",
                "kerja | verb | work | Bapak nembe kerja wonten kantor.",
                "bakti | noun | devotion | Bocah kuwi pancen duwe bakti marang wong tuwane.",
                "ngresiki | verb | to clean | Bapak nembe ngresiki latar wingking.",
                "dalan | noun | road | Dalan iki rame banget amarga akeh kendaraan.",
                "désa | noun | village | Aku manggon ing désa sing asri.",
                "supaya | conjunction | so that | Sinaua sing sregep supaya pinter.",
                "lingkungan | noun | bend | Omahku ana ing sandhinge lingkungan dalan kuwi.",
                "resik | adjective | clean | Omah iki katon resik amarga saben dina disapu.",
                "lan | conjunction | and | Bapak lan Ibu tindak dhateng peken.",
                "nyaman | adjective | comfortable | Kursi iki rasane nyaman banget kanggo lungguh.",
                "saben | determiner | every | Saben esuk aku sarapan sega goreng.",
                "dina | multiword term | holiday | Umat Islam padha silaturahmi menyang omahe tangga teparo nalika dina gedhé Idul Fitri.",
            ]
        ),
        "output": "Saben dina, para warga padha kerja bakti ngresiki dalan désa supaya lingkungan resik lan nyaman.",
        "translation": "The citizens do community service cleaning the village road so the environment is clean and comfortable every day.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "sinau | verb | to study | Aku lagi sinau basa Jawa supaya bisa lancar guneman karo simbah.",
                "aksara | noun | script | Bocah-bocah lagi sinau nulis aksara Jawa.",
                "jawa | noun | Javanese heartland or culture; specifically referring to lands under the Javanese monarchs or traditional Javanese customs | Wong iku isih ngugemi adat kejawèn sing wis dadi warisane para leluhur.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "sekolah | noun | schoolchild | Bocah sekolahan jaman saiki wis pinter nggunakake internet.",
                "karo | preposition | with | Simbah dhahar bubur karo santen.",
                "bapak | noun | father | Bapak tindak dhateng kantor.",
                "guru | verb | to study under a teacher; to seek knowledge from a master | Yen kowe pengin pinter nembang, kowe kudu maguru marang empune.",
                "sing | pronoun | which, who, that | Iki buku sing daktuku wingi.",
                "sabar | multiword term | extremely patient | Wong tuwa iku pancen sabar drana senajan putune kerep nggawe jengkel.",
                "lan | conjunction | and | Bapak lan Ibu tindak dhateng peken.",
                "pinter | adjective | smart | Bocah kuwi pancen pinter banget ing sekolah.",
                "terang | verb | to explain | Bapak guru lagi nerangaké babagan sejarah Majapahit.",
                "pelajaran | noun | lesson | Bocah-bocah nggatekake pelajaran saka Bapak Guru.",
            ]
        ),
        "output": "Aku sinau aksara Jawa ing sekolah karo bapak guru sing sabar lan pinter nerangake pelajaran.",
        "translation": "I learn Javanese script at school with a teacher who is patient and smart at explaining lessons.",
    },
    {
        "word_candidates": "\n".join(
            [
                "adhi | noun | younger sibling | Adhiku lagi sinau ing kamar.",
                "seneng | adjective | happy; to like | Aku seneng banget mangan sega goreng.",
                "nggambar | verb | to draw | Adhik lagi nggambar pemandangan ing buku gambar.",
                "sawangan | noun | view | Sawangan ing pinggir segara iki pancen endah banget.",
                "gunung | multiword term | a long mountain range | Ing sisih lor kutha iki ana gunung kendheng sing katon ijo royo-royo.",
                "apik | adjective | good | Klambine apik banget.",
                "nganggo | verb | to use | Bapak tindak kantor nganggo mobil.",
                "potlot | noun | pencil | Aku tuku potlot anyar ing toko buku.",
                "warna | noun | color | Kembang mawar iku duwe warna abang sing apik banget.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "buku | noun | book | Aku tuku buku anyar ing toko.",
                "gambar | noun | picture | Bocah kuwi lagi nggawe gambar gunung.",
                "sing | pronoun | which, who, that | Iki buku sing daktuku wingi.",
                "anyar | adjective | new | Aku tuku klambi anyar.",
                "iki | pronoun | this | Buku iki duweke adhiku.",
            ]
        ),
        "output": "Adhi seneng nggambar sawangan gunung sing apik, nganggo potlot warna ing buku gambar anyar iki.",
        "translation": "Younger sibling likes to draw beautiful mountain views using colored pencils in this new sketchbook.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bapak | noun | father | Bapak tindak dhateng kantor.",
                "nggawa | verb | bring | Aku nggawa buku menyang sekolah.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "asil | noun | result | Asil panene taun iki apik banget.",
                "panèn | multiword term | harvesting crops during the rainy season | Para tani ing desa lagi sibuk panèn rendhengan amarga wis mlebu mangsa udan.",
                "saka | preposition | from | Bapak nembe kondur saka kantor.",
                "sawah | noun | a portion of a rice field allocated for sugarcane cultivation | Sawah sing ditanduri tebu kuwi wis wayahe panen.",
                "banjur | conjunction | then | Dheweke adus, banjur mangkat sekolah.",
                "simpen | verb | to store, to save, or to hide | Bapak nyimpen dhuwit ana ing njero celengan.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "jero | adjective | deep | Sumur iki banyune isih jero banget.",
                "gudhang | noun | warehouse | Bapak lagi ngeterake barang menyang gudhang.",
                "omah | noun | house | Omahku ana ing pinggir dalan gedhe.",
                "ageng | adjective | big | Dalemipun Pak Lurah punika ageng sanget.",
                "iki | pronoun | this | Buku iki duweke adhiku.",
            ]
        ),
        "output": "Bapak nggawa kathah asil panèn sawah, banjur disimpen ing jero gudhang omah sing ageng iki.",
        "translation": "Father brings many harvest results from the field and then stores them inside the warehouse of this big house.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ibu | noun | mother | Ibu tindak dhateng peken mundhut rasukan.",
                "becik | adjective | good | Bocah kuwi pancen becik bebudene.",
                "paring | verb | to give | Bapak paring arta kagem simbah.",
                "pitutur | noun | wise advice | Wong tuwa kudu menehi pitutur sing becik marang anak-anake.",
                "marang | preposition | to | Kula badhe matur marang Bapak.",
                "anak | multiword term | adopted child | Bocah kuwi dadi anak angkat ing kulawarga sugih.",
                "supaya | conjunction | so that | Sinaua sing sregep supaya pinter.",
                "tansah | adverb | always | Mugi-mugi panjenengan tansah pinaringan kasarasan.",
                "jujur | adjective | honest | Dadi wong iku kudu jujur supaya dipercaya liyan.",
                "nalika | conjunction | when | Nalika aku isih cilik, aku seneng dolanan layangan.",
                "ngomong | verb | to speak | Kowe mau ngomong apa karo bapak?",
                "karo | preposition | with | Simbah dhahar bubur karo santen.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "wong | noun | person | Wong iku mau nggawa kranjang isi woh-wohan.",
                "liya | adjective | other | Aku arep tuku buku sing liya.",
            ]
        ),
        "output": "Ibu maringi pitutur marang anak supaya tansah jujur nalika ngomong karo wong liya.",
        "translation": "Mother kindly gives advice to her child to always be honest when speaking with many other people.",
    },
    {
        "word_candidates": "\n".join(
            [
                "wong | noun | person | Wong iku mau nggawa kranjang isi woh-wohan.",
                "lanang | adjective | male | Bocah lanang iku lagi dolanan bal-balan ing lapangan.",
                "iku | determiner | that | Buku iku duweke adhiku.",
                "mlaku | verb | walk | Aku mlaku menyang pasar saben esuk.",
                "alon | adverb | slow | Mlakune alon banget amarga dalane lunyu.",
                "banget | adverb | very | Panganan iki enak banget.",
                "amarga | conjunction | because | Aku ora mangkat sekolah amarga udan deres.",
                "sikil | noun | leg or foot | Sikilku lara amarga kakehan mlaku.",
                "isih | adverb | still | Aku isih mangan sega goreng.",
                "lara | adjective | sick | Adhik ora mlebu sekolah amarga lara untu.",
                "wus | adverb | already | Srengengene wus mlethek saka wetan.",
                "tiba | verb | fall | Adhik nangis amarga tiba saka pit.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "dalan | noun | road | Dalan iki rame banget amarga akeh kendaraan.",
                "wingi | adverb | yesterday | Aku wingi tuku buku anyar ing pasar.",
            ]
        ),
        "output": "Wong lanang iku mlaku alon banget amarga sikile isih lara tiba ing dalan wingi.",
        "translation": "That man walks very slowly because his leg is still hurting from falling on the road yesterday.",
    },
    {
        "word_candidates": "\n".join(
            [
                "aku | pronoun | I | Aku arep lunga menyang pasar.",
                "lan | conjunction | and | Bapak lan Ibu tindak dhateng peken.",
                "kanca | noun | friend | Budi iku kanca sekolahku wiwit SD.",
                "padha | adjective | same, equal, or plural marker | Bocah-bocah kuwi padha dolanan ing lapangan.",
                "seneng | adjective | happy; to like | Aku seneng banget mangan sega goreng.",
                "dolan | verb | to play or hang out | Aku arep dolan menyang omahe kancaku.",
                "dhateng | verb | to come / to | Bapak nembe kemawon dhateng saking kitha.",
                "kali | noun | river | Banyu kali iki katon bening banget.",
                "ageng | adjective | big | Dalemipun Pak Lurah punika ageng sanget.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "ndeleng | verb | to see | Aku lagi ndeleng TV ing ruang tamu.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "iwak | noun | freshwater fish | Ing rawa iki isih akeh iwak loh sing bisa dipancing.",
                "apik | adjective | good | Klambine apik banget.",
                "cilik | adjective | small | Omahku cilik nanging resik.",
            ]
        ),
        "output": "Aku lan kanca padha seneng dolan dhateng kali ageng kanggo ndeleng iwak cilik apik.",
        "translation": "My friend and I like to hang out at the big river to see many small beautiful fish.",
    },
    {
        "word_candidates": "\n".join(
            [
                "simbah | noun | grandparent | Simbah nembe sare wonten kamar.",
                "kerep | adverb | often | Dheweke kerep dolan mrene.",
                "crita | noun | story | Bapak lagi maca crita wayang.",
                "babagan | preposition | about | Dheweke crito babagan pengalamane ing kutha.",
                "jaman | noun | era | Jaman saiki kabeh wis sarwa nganggo teknologi.",
                "kuna | adjective | ancient; from time immemorial | Candi iki wis ana wiwit jaman kuna makuna.",
                "nalika | conjunction | when | Nalika aku isih cilik, aku seneng dolanan layangan.",
                "wong | noun | person | Wong iku mau nggawa kranjang isi woh-wohan.",
                "isih | adverb | still | Aku isih mangan sega goreng.",
                "padha | adjective | same, equal, or plural marker | Bocah-bocah kuwi padha dolanan ing lapangan.",
                "manggon | verb | to reside | Dheweke manggon ing kutha Solo.",
                "seneng | adjective | happy; to like | Aku seneng banget mangan sega goreng.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "désa | noun | village | Aku manggon ing désa sing asri.",
                "ageng | adjective | big | Dalemipun Pak Lurah punika ageng sanget.",
            ]
        ),
        "output": "Simbah kerep crita babagan jaman kuna nalika wong isih padha manggon seneng ing désa.",
        "translation": "Grandparent often tells stories about ancient times when people still lived happily in a big village.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bocah | noun | child | Bocah kuwi sregep banget sinau.",
                "pinter | adjective | smart | Bocah kuwi pancen pinter banget ing sekolah.",
                "kuwi | determiner | that | Buku kuwi duweke adhiku.",
                "seneng | adjective | happy; to like | Aku seneng banget mangan sega goreng.",
                "maca | verb | to read | Bapak lagi maca koran ing teras.",
                "buku | noun | book | Aku tuku buku anyar ing toko.",
                "babad | noun | chronicle | Babad Tanah Jawi iku salah siji sumber sejarah Jawa sing penting.",
                "amarga | conjunction | because | Aku ora mangkat sekolah amarga udan deres.",
                "crita | noun | story | Bapak lagi maca crita wayang.",
                "apik | adjective | good | Klambine apik banget.",
                "banget | adverb | very | Panganan iki enak banget.",
                "lan | conjunction | and | Bapak lan Ibu tindak dhateng peken.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "piwulang | noun | teaching | Bocah kuwi tansah eling marang piwulang wong tuwane.",
                "penting | adjective | important | Sinau kuwi penting banget kanggo masa depan.",
            ]
        ),
        "output": "Bocah pinter kuwi seneng maca buku babad amarga critane apik banget lan kathah piwulang penting.",
        "translation": "That smart child likes to read chronicles because the stories are very good and contain many important teachings.",
    },
    {
        "word_candidates": "\n".join(
            [
                "para | determiner | the (plural marker for people) | Para tamu sampun sami rawuh ing adicara punika.",
                "tamu | noun | guest | Bapak nembe nemoni tamu wonten ing ruang tamu.",
                "kathah | adjective | many | Tiyang ingkang rawuh wonten ing adicara punika kathah sanget.",
                "padha | adjective | same, equal, or plural marker | Bocah-bocah kuwi padha dolanan ing lapangan.",
                "rawuh | verb | to arrive | Bapak nembe kemawon rawuh saking kantor.",
                "ing | preposition | in | Aku tuku buku ing pasar.",
                "omah | noun | house | Omahku ana ing pinggir dalan gedhe.",
                "ageng | adjective | big | Dalemipun Pak Lurah punika ageng sanget.",
                "iki | pronoun | this | Buku iki duweke adhiku.",
                "kanggo | preposition | for | Buku iki kanggo kowe.",
                "ngadhepi | verb | to face | Kita kudu wani ngadhepi tantangan urip.",
                "acara | noun | event | Dina iki ana acara perpisahan ing sekolah.",
                "sing | pronoun | which, who, that | Iki buku sing daktuku wingi.",
                "penting | adjective | important | Sinau kuwi penting banget kanggo masa depan.",
                "banget | adverb | very | Panganan iki enak banget.",
                "ngadiri | verb | to attend | Ibu ngadiri acara.",
            ]
        ),
        "output": "Para tamu padha rawuh ing omah ageng iki ngadiri acara sing penting banget.",
        "translation": "Many guests arrived at this big house to attend a very important event.",
    },
]
