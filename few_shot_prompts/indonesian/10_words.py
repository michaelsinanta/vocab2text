"""10-word few-shot examples for indonesian.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "saya | pronoun | one who speaks or writes (in the formal or casual variety); I | N/A",
                "dan | particle | conjunctions of language units (words, phrases, clauses and sentences) that are equivalent, belong to the same type and have no different functions | ayah dan ibu, bibi dan paman, serta para anak, cucu, dan kemenakan bersama-sama merayakan 50 tahun perkawinan nenek mereka",
                "keluarga | noun | mothers and fathers and their children; the whole house | seluruh keluarganya pindah ke Bandung",
                "berencana | verb | with a plan; design; there's a plan | N/A",
                "pergi | verb | leave | setelah mengunci pintu rumah, dia pergi ke tempat kerjanya; pukul lima pagi ia pergi ke stasiun",
                "berlibur | verb | go (have fun, relax, etc.) spend time off; vaccinate | mereka merencanakan berlibur ke Pulau Dewata",
                "ke | particle | preposition to mark a direction or destination | ibu sedang pergi ke pasar; rumahnya menghadap ke utara",
                "pantai | noun | seaside; coast | N/A",
                "akhir | noun | denouement; the end | pada akhir tahun ini",
                "pekan | noun | week (7 days) | harapanku dia datang pekan ini",
            ]
        ),
        "output": "Saya dan keluarga berencana pergi berlibur ke pantai akhir pekan.",
        "translation": "My family and I plan to go on a beach vacation this weekend.",
    },
    {
        "word_candidates": "\n".join(
            [
                "mereka | pronoun | third person plural (him with others); the people being talked about | Toto bertemu dengan Amir di jalan, lalu mereka pergi bersama-sama ke sekolah",
                "memutuskan | verb | set; determine | ia memutuskan siapa-siapa yang akan melaksanakan rencananya",
                "untuk | particle | aim or purpose; for | lemari untuk (menyimpan) pakaian; pakaian untuk segala usia",
                "tidak | adverb | particles to express denial, rejection, denial, and so on; nothing | tempat kerjanya tidak jauh dari rumahnya; apa yang dikatakannya itu tidak benar...",
                "menghadiri | verb | attend (lecture, ceremony) | ia akan menghadiri upacara wisuda anaknya",
                "acara | noun | activities performed, broadcast, or contested; programming (television, radio, etc.) | acara televisi dan radio setiap hari dimuat dalam media daring",
                "pernikahan | noun | wedding ceremony | dia akan menghadiri pernikahan saudaranya",
                "teman | noun | friend; friend | hanya teman dekat yang akan kuundang",
                "mereka | pronoun | third person plural (him with others); the people being talked about | Toto bertemu dengan Amir di jalan, lalu mereka pergi bersama-sama ke sekolah",
                "besok | noun | the day after today; tomorrow | hari ini hari Kamis, besok hari Jumat",
            ]
        ),
        "output": "Mereka memutuskan untuk tidak menghadiri acara pernikahan teman mereka besok.",
        "translation": "They decided not to attend their friend's wedding ceremony tomorrow.",
    },
    {
        "word_candidates": "\n".join(
            [
                "apakah | pronoun | Question words to express choices and emphasize the information you want to know | apakah suratku sudah sampai?",
                "kamu | pronoun | who is spoken to; who is addressed (in a friendly or rude way) | N/A",
                "sudah | adverb | has (states an action that has occurred) | ia sudah pandai membaca",
                "menyelesaikan | verb | completing (preparing) work and so on; perfect (sentences and so on) | ia menyelesaikan kalimat itu dengan cepat",
                "tugas | noun | which must be done or which is determined to be done; work that is a person's responsibility; assigned work | pegawai hendaklah menjalankan tugas masing-masing dengan baik; kerjakan tugas Saudara baik-baik",
                "matematika | noun | the science of numbers, relationships between numbers, and operational procedures used in solving problems regarding numbers | N/A",
                "di | particle | preposition to mark time | di hari itu ia tidak datang",
                "sesi | noun | half; stage | para peserta upacara tekun mengikuti sesi demi sesi acara yang telah dijadwalkan panitia",
                "kelas | noun | study room at school | gedung sekolah itu terdiri atas enam kelas",
                "kemarin | noun | the day before today | sekarang hari Jumat, kemarin hari Kamis",
            ]
        ),
        "output": "Apakah kamu sudah menyelesaikan tugas matematika di sesi kelas kemarin?",
        "translation": "Have you completed the mathematics assignment from yesterday's class session?",
    },
    {
        "word_candidates": "\n".join(
            [
                "mengapa | pronoun | interrogative words to ask for causes, reasons, or actions | mengapa kawanmu tidak datang?; sedang mengapa adikmu itu?",
                "pria | noun | adult male | kaum pria",
                "tua | adjective | have lived a long time; elderly (not young anymore) | ia lebih tua dua tahun daripada saya; neneknya sudah tua; pada hari (masa) tuanya pada masa (ketika) tua",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "terus | adverb | non-stop | ia berjalan terus siang malam",
                "menangis | verb | giving birth to feelings of sadness (disappointment, regret, etc.) by shedding tears and making sounds (sobbing, screaming) | ibu itu menangis terharu; anak itu menangis kesakitan",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "dalam | particle | preposition to mark a place that contains content | dalam rumah itu tidak ada mebel",
                "kereta | noun | train | N/A",
                "api | noun | heat and light that comes from something burning; flame | di dekat api itu tampak beberapa orang berdiang",
            ]
        ),
        "output": "Mengapa pria tua itu terus menangis di dalam kereta api?",
        "translation": "Why does that old man keep crying on the train?",
    },
    {
        "word_candidates": "\n".join(
            [
                "mari | particle | interjection to express an invitation; Come on | N/A",
                "kita | pronoun | plural first person pronouns, which speak together with other people, including those being spoken to | N/A",
                "membersihkan | verb | make it clean (by washing, sweeping, scrubbing, etc.) | N/A",
                "seluruh | numeral | all; all; throughout (indicates a whole) | seluruh dunia; seluruh tubuh",
                "ruangan | noun | a spacious place; room (large); room (inside the house); class (place of study)... | N/A",
                "tamu | noun | people who come to visit (visit, etc.) to other people's places or to banquets | N/A",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "sebelum | particle | when it hasn't happened yet; prior to (a job, situation, etc.); before | sebelum tidur periksalah pintu dan jendela...",
                "tamu | noun | people who come to visit (visit, etc.) to other people's places or to banquets |  *(Catatan: disesuaikan dari pengulangan frasa tamu undangan)*",
                "undangan | noun | invited person | undangan sudah memenuhi tempat yang disediakan",
                "datang | verb | arrived at the destination | ia datang pukul 08.00",
            ]
        ),
        "output": "Mari kita membersihkan seluruh ruangan tamu ini sebelum tamu undangan datang!",
        "translation": "Let’s clean the entire living room before the invited guests arrive!",
    },
    {
        "word_candidates": "\n".join(
            [
                "jangan | adverb | the word prohibiting means not allowed; it shouldn't be necessary | jangan bohong",
                "pernah | adverb | have experienced (experienced and so on) | ia sendiri pernah dihukum; belum (tidak) pernah belum sekali pun mengalami dan sebagainya",
                "mencoba | verb | trying to do (do) something | dua orang tahanan mencoba melarikan diri",
                "membuka | verb | making it uncovered or uncovered (such as removing the cover, hood, fence) | setiap pukul 05.00 pagi ia sudah membuka jendela; jika membuka lemari jangan lupa menutupnya kembali",
                "pintu | noun | (boards and so on) cover (door) | Ibu membukakan pintu untuk tamunya",
                "rahasia | noun | something hidden | pintu rahasia",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "tanpa | adverb | not with ...; don't... | menghilang tanpa bekas",
                "izin | noun | statement granting (not prohibiting, etc.); consent permits | ia telah mendapat izin untuk mendirikan perusahaan mebel",
                "saya | pronoun | one who speaks or writes (in the formal or casual variety); I | N/A",
            ]
        ),
        "output": "Jangan pernah mencoba membuka pintu rahasia itu tanpa izin saya!",
        "translation": "Never try to open that secret door without my permission!",
    },
    {
        "word_candidates": "\n".join(
            [
                "betapa | particle | interjections indicating feelings of wonder, admiration, sadness, and so on; how; Really | betapa sedihnya orang yang kematian ibu",
                "indah | adjective | in a condition pleasing to the eye; Beautiful; beautiful | N/A",
                "pemandangan | noun | beautiful natural conditions to look at | di Pantai Senggigi, Lombok, banyak pemandangan yang indah",
                "matahari | noun | (the first letter is usually written in capitals) the star which is the center of the solar system, emits heat and light to the Earth and other planets that orbit it, most of its content is in the form of hydrogen and helium | N/A",
                "terbenam | verb | sinking (about the sun) | matahari terbenam pukul enam sore",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "atas | noun | higher part (place). | dari atas bukit kita dapat menikmati pemandangan yang indah; bagian atas dan bagian bawah",
                "pegunungan | noun | mountains | N/A",
                "sore | noun | evening | aku pulang ke Solo sore ini; sorenya pada petang harinya",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
            ]
        ),
        "output": "Betapa indah pemandangan matahari terbenam di atas pegunungan sore ini!",
        "translation": "How beautiful the sunset view over the mountains is this evening!",
    },
    {
        "word_candidates": "\n".join(
            [
                "perusahaan | noun | a legal entity organization that carries out transactions or business | N/A",
                "konstruksi | noun | the arrangement (model, layout) of a building (bridge, house, etc.) | rumah itu kokoh karena konstruksinya beton bertulang",
                "dari | particle | a word that states the origin of the arrival | ia datang dari Medan; menerima surat dari ayahnya",
                "jepang | noun | A country located in East Asia, whose capital is Tokyo | N/A",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "membangun | verb | erect (construct buildings and so on) | mereka sedang membangun benteng di tempat itu",
                "gedung | noun | large walled buildings and so on as places for activities such as offices, meetings, commerce, performances or sports | N/A",
                "bertingkat | verb | wearing level; moaning | gedung bertingkat; di tanah yang sempit sebaiknya didirikan bangunan yang bertingkat",
                "sepuluh | numeral | numbers symbolized by the number 10 (Arabic) or X (Roman) | N/A",
            ]
        ),
        "output": "Perusahaan konstruksi dari Jepang itu membangun gedung bertingkat sepuluh.",
        "translation": "That Japanese construction company built a ten-story building.",
    },
    {
        "word_candidates": "\n".join(
            [
                "jika | particle | conjunctions to mark conditions (promises); if | jika hari tidak hujan, saya akan datang; intan itu jika terbenam di pelimbahan sekalipun tiada akan hilang cahayanya",
                "hujan | noun | water droplets falling from the air due to the cooling process | N/A",
                "turun | verb | fall (about rain, snow, and so on); come upon (about plagues, torment, etc.) | N/A",
                "dengan | particle | connecting words to explain the method (how it happens or takes effect); while; while | ia menjawab dengan tersenyum; harus datang sendiri dengan membawa ijazah *(Catatan: berfungsi memperjelas keadaan kata keterangan)*",
                "sangat | adverb | especially (things, circumstances, etc.); very; too | rumahnya sangat jauh dari sini",
                "deras | adjective | heavy (about rain) | hujan deras seperti dicurahkan dari langit",
                "kami | pronoun | who speaks together with others (excluding those spoken to); who writes on behalf of a group, does not include readers | N/A",
                "pasti | adjective | is fixed; must not; Of course; must | dia sudah berjanji besok pasti datang; jika diberkahi Tuhan, usaha kita pasti berhasil",
                "membatalkan | verb | undo | mereka sepakat membatalkan keberangkatannya karena cuaca buruk",
                "pertandingan | noun | a competition in sports that pits two players (or teams) against each other | pertandingan sepak bola",
            ]
        ),
        "output": "Jika hujan turun dengan sangat deras kami pasti membatalkan pertandingan.",
        "translation": "If it rains very heavily, we will definitely cancel the match.",
    },
    {
        "word_candidates": "\n".join(
            [
                "harga | noun | the value of goods determined or expressed in money | mobil ini sangat mahal harganya",
                "komputer | noun | an automatic electronic device that can calculate or process data carefully according to instructions... | N/A",
                "baru | adjective | recently purchased (owned); never used | pagi tadi ia memakai baju baru; kemarin ia mengendarai sepeda baru hadiah dari orang tuanya",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "ternyata | verb | it's real; there is proof; proven | ternyata ia memiliki kemampuan memimpin",
                "jauh | adjective | many; very; very (about differences, discrepancies or shortcomings) | anak itu jauh lebih besar daripada kakaknya",
                "lebih | adverb | increase; increasingly | kesehatannya sudah lebih baik; harganya menjadi lebih mahal",
                "mahal | adjective | high price | karena senangnya pada barang itu, biarpun mahal dibelinya juga",
                "daripada | particle | preposition to mark a comparison | buku ini lebih bagus daripada buku itu",
                "perkiraan | noun | estimated; guessing results; consideration; calculation | N/A",
                "anda | pronoun | words of greeting to the person you are talking to or communicating with (does not differentiate between level, position and age) | N/A",
            ]
        ),
        "output": "Harga komputer baru ini ternyata jauh lebih mahal daripada perkiraan anda.",
        "translation": "The price of this new computer turns out to be much higher than your estimate.",
    },
]
