"""15-word few-shot examples for indonesian.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "ayah | noun | male biological parents; father | N/A",
                "dan | particle | conjunctions of language units (words, phrases, clauses and sentences) that are equivalent, belong to the same type and have no different functions | ayah dan ibu, bibi dan paman, serta para anak, cucu, dan kemenakan bersama-sama merayakan 50 tahun perkawinan nenek mereka",
                "ibu | noun | female parents | N/A",
                "berencana | verb | with a plan; design; there's a plan | N/A",
                "membeli | verb | obtain something by exchanging (payment) for money | ibu pergi ke pasar untuk membeli beras dan sayur",
                "rumah | noun | building for residence | N/A",
                "baru | adjective | recently finished (made, given) | ia membeli rumah baru di kompleks perumahan itu",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "kawasan | noun | certain areas that have certain characteristics, such as residences, shops, industry, and so on | Pulo Gadung merupakan kawasan industri",
                "perumahan | noun | a collection of several houses; residential houses | pemerintah sedang mendirikan perumahan untuk golongan menengah",
                "elit |  | → elite | N/A",
                "yang | particle | a word that states that the next part of the sentence explains the word in front | dijumpainya seorang pengemis yang sedang berteduh di bawah pohon asam itu",
                "berada | verb | It is in) | ketika itu ia berada di luar negeri",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "pusat | noun | a place located in the middle | Istana Merdeka letaknya di pusat kota Jakarta",
                "kota | noun | a population concentration area with high density and modern facilities and most of the population works outside agriculture | N/A",
            ]
        ),
        "output": "Ayah dan ibu berencana membeli rumah baru di kawasan perumahan elit yang berada di pusat kota.",
        "translation": "My father and mother plan to buy a new house in an elite residential area in the city center.",
    },
    {
        "word_candidates": "\n".join(
            [
                "kami | pronoun | who speaks together with others (excluding those spoken to); who writes on behalf of a group, does not include readers | N/A",
                "semua | numeral | all; all | semua orang menangisi kepergiannya; karena kelalaiannya semua penghuni asrama itu kena marah",
                "sepakat | adjective | agree; consensus; agree | Malaysia dan Singapura sepakat untuk mengadakan perundingan dengan Indonesia",
                "untuk | particle | aim or purpose; for | lemari untuk (menyimpan) pakaian; pakaian untuk segala usia",
                "tidak | adverb | particles to express denial, rejection, denial, and so on; nothing | tempat kerjanya tidak jauh dari rumahnya; apa yang dikatakannya itu tidak benar...",
                "membicarakan | verb | converse; say; negotiate | kita sudah membicarakan perkara itu selama dua hari",
                "masalah | noun | something that must be completed (solved); question; problem | masalah keluarga hendaknya diselesaikan oleh keluarga itu sendiri; rapat itu harus memecahkan masalah yang paling rumit",
                "pekerjaan | noun | livelihood; which is used as a staple of livelihood; something done to earn a living | ia sedang berusaha mencari pekerjaan",
                "selama | noun | all the time; during | selama aku berada di luar negeri, ia rajin mengirim kabar kepadaku; selama hayat dikandung badan budi baiknya tidak akan terlupakan",
                "menikmati | verb | taste; experience (something pleasant or satisfying) | menikmati hasil kemerdekaan",
                "liburan | noun | holiday period; vacancy | N/A",
                "keluarga | noun | mothers and fathers and their children; the whole house | seluruh keluarganya pindah ke Bandung",
                "bersama | adverb | together; simultaneously | kami berangkat bersama ke sekolah",
                "minggu | noun | a period of seven days; week | setiap tahun kami mendapat cuti dua minggu",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
            ]
        ),
        "output": "Kami semua sepakat untuk tidak membicarakan masalah pekerjaan selama menikmati liburan keluarga bersama minggu ini.",
        "translation": "We all agreed not to talk about work during this family holiday this week.",
    },
    {
        "word_candidates": "\n".join(
            [
                "apakah | pronoun | Question words to express choices and emphasize the information you want to know | apakah suratku sudah sampai?",
                "kamu | pronoun | who is spoken to; who is addressed (in a friendly or rude way) | N/A",
                "sangat | adverb | especially (things, circumstances, etc.); very; too | rumahnya sangat jauh dari sini",
                "yakin | adjective | believe (know, understand) truly; (feel) certain (certain, unmistakable) | hakim yakin akan kesalahan terdakwa itu; ia berkata dengan yakinnya berkata dengan pasti...",
                "bahwa | particle | connecting words to state the content or description of the part of the sentence in front | ia mengira bahwa hari ini libur",
                "keputusan | noun | decree; final attitude (step that must be carried out) | ia tidak berani segera mengambil keputusan",
                "untuk | particle | aim or purpose; for | lemari untuk (menyimpan) pakaian; pakaian untuk segala usia",
                "pindah | verb | switch or swap places | N/A",
                "ke | particle | preposition to mark a direction or destination | ibu sedang pergi ke pasar; rumahnya menghadap ke utara",
                "luar | noun | areas, places, and so on that are not part of something itself | ia berdiri di luar gedung; lima tahun ia tinggal di luar negeri",
                "negeri | noun | country; government (opposite private) | karena ia bersekolah di SMA negeri, biayanya pun tidak begitu besar",
                "adalah | verb | identical to | Pancasila adalah falsafah bangsa Indonesia",
                "pilihan | noun | paths, efforts and so on that can be done | tidak ada lagi pilihan lain, kita harus pergi sekarang",
                "paling | adverb | ter-; very | anaknya yang paling besar duduk di kelas 3 SMU",
                "tepat | adjective | correct or suitable (about guesses, predictions, etc.) | perhitungannya kurang tepat; alasan itu mungkin tepat juga",
                "sekarang | noun | this time (time, moment); now | lain dulu lain sekarang",
            ]
        ),
        "output": "Apakah kamu sangat yakin bahwa keputusan untuk pindah ke luar negeri adalah pilihan paling tepat sekarang?",
        "translation": "Are you very sure that the decision to move abroad is the most correct choice right now?",
    },
    {
        "word_candidates": "\n".join(
            [
                "bagaimana | pronoun | question words to ask for methods, actions (usually followed by the word method) | bagaimana caranya membeli buku dari luar negeri?",
                "cara | noun | way (rule, system) of doing (doing and so on) something | begitulah cara orang membuat tapai; bagaimana cara menulis huruf ini?",
                "yang | particle | a word to state that the next word or sentence takes precedence or is differentiated from the others | orang yang baik hati",
                "paling | adverb | ter-; very | anaknya yang paling besar duduk di kelas 3 SMU",
                "efektif | adjective | can bring results; effective (about effort, action); mangkus | N/A",
                "untuk | particle | aim or purpose; for | lemari untuk (menyimpan) pakaian; pakaian untuk segala usia",
                "mengatasi | verb | cope | kapal-kapal perang kita turut mengatasi penyelundupan",
                "masalah | noun | something that must be completed (solved); question; problem | masalah keluarga hendaknya diselesaikan oleh keluarga itu sendiri...",
                "kemacetan | noun | thing (state) stuck | pawai itu mengakibatkan kemacetan lalu lintas",
                "lalu | verb | walk past | dilarang lalu di jalan ini",
                "lintas | noun | route | lintas Jakarta–Bandung",
                "parah | adjective | difficult to overcome | masalah kenakalan remaja akhir-akhir ini makin parah",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "ibu | noun | the main one among several other things; The most important | ibu negeri; ibu kota",
                "kota | noun | a population concentration area with high density and modern facilities and most of the population works outside agriculture | N/A",
                "kita | pronoun | plural first person pronouns, which speak together with other people, including those being spoken to | N/A",
            ]
        ),
        "output": "Bagaimana cara yang paling efektif untuk mengatasi masalah kemacetan lalu lintas parah di ibu kota kita?",
        "translation": "What is the most effective way to deal with severe traffic congestion in our capital city?",
    },
    {
        "word_candidates": "\n".join(
            [
                "tolong | verb | help | minta tolong minta bantuan",
                "bantu | verb | Help | bantulah orang miskin dan melarat",
                "saya | pronoun | one who speaks or writes (in the formal or casual variety); I | N/A",
                "memindahkan | verb | put to another place; carry (move); order (move, etc.) to move to another place | ia disuruh ibunya memindahkan lemari itu ke kamar belakang",
                "semua | numeral | all; all | semua orang menangisi kepergiannya...",
                "barang | noun | general objects (everything that is tangible or tangible) | barang cair; barang keras",
                "berat | adjective | great pressure (scale) | peti berat itu tidak dapat diangkat oleh tiga orang",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "ke | particle | preposition to mark a direction or destination | ibu sedang pergi ke pasar; rumahnya menghadap ke utara",
                "dalam | noun | the inside, not the outside | ketika rumah itu terbakar, anak-anaknya masih ada di dalam",
                "gudang | noun | a house or ward where things are kept | N/A",
                "besar | adjective | more than medium size; small opponent | batang kayu ini sangat besar sehingga tidak sanggup tanganku memeluknya",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "belakang | noun | (behind | anak-anak berlindung di belakang pohon",
                "rumah | noun | building for residence | N/A",
                "sekarang | noun | this time (time, moment); now | lain dulu lain sekarang",
            ]
        ),
        "output": "Tolong bantu saya memindahkan semua barang berat ini ke dalam gudang besar di belakang rumah sekarang!",
        "translation": "Please help me move all these heavy items into the large warehouse behind the house now!",
    },
    {
        "word_candidates": "\n".join(
            [
                "tolong | verb | help | minta tolong minta bantuan",
                "jangan | adverb | the word prohibiting means not allowed; it shouldn't be necessary | jangan bohong",
                "mengizinkan | verb | give permission; grant; allow; not prohibited | orang tuanya telah mengizinkannya untuk segera menikah",
                "anak | noun | small humans | anak itu baru berumur enam tahun",
                "kecil | adjective | young | anak itu lebih kecil daripada adikku",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "bermain | verb | do something for fun | adiknya sedang bermain di taman",
                "sendirian | adverb | alone; Alone | semua orang sudah pulang, tetapi ia tinggal sendirian menjaga anak yang sakit itu",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "dekat | adjective | short, not far (distance or between) | tinggalnya dekat dari sini",
                "tepi | noun | a place by the sea (river and so on) | tepi pantai pesisir; tepi sungai; tepi laut",
                "sungai | noun | large streams of water (usually natural-made); time | sungai itu dapat dilayari sampai ke pedalaman",
                "yang | particle | a word that states that the next part of the sentence explains the word in front | dijumpainya seorang pengemis yang sedang berteduh di bawah pohon asam itu",
                "sangat | adverb | especially (things, circumstances, etc.); very; too | rumahnya sangat jauh dari sini",
                "dalam | adjective | far down (from the surface); deep into the center (from the edge) | lukanya cukup dalam",
                "tadi | noun | just a moment ago | sejak tadi ia sudah kuperingatkan; dari tadi ia belum duduk",
            ]
        ),
        "output": "Tolong jangan mengizinkan anak kecil itu bermain sendirian di dekat tepi sungai yang sangat dalam tadi!",
        "translation": "Please do not let that small child play alone near the very deep riverbank!",
    },
    {
        "word_candidates": "\n".join(
            [
                "sungguh | adverb | very; very | buku itu sungguh mahal",
                "luar | noun | not from the environment (family, country, region, etc.) itself; foreign | meskipun ia orang luar, tetapi sudah seperti keluarga sendiri *(Catatan: bagian dari idiom luar biasa)*",
                "biasa | adjective | common; general | bagi masyarakat sekarang memakai sepatu sudah biasa",
                "penampilan | noun | process, method, act of displaying | acara itu diisi dengan penampilan pakaian adat; penampilan mereka sangat mengesankan",
                "tarian | noun | type of dance; dance style | N/A",
                "tradisional | adjective | according to tradition (custom) | upacara tradisional upacara menurut adat",
                "yang | particle | a word that states that the next part of the sentence explains the word in front | dijumpainya seorang pengemis yang sedang berteduh di bawah pohon asam itu",
                "para | particle | accompanying words that express reference to a group | para tamu mulai berdatangan",
                "siswa | noun | students (especially at primary and secondary school levels); student | siswa SMU",
                "sekolah | noun | buildings or institutions for learning and teaching as well as places for receiving and giving lessons... | keluar sekolah sudah tidak belajar di sekolah lagi...",
                "dasar | noun | base; foundation | gotong-royong adalah dasar masyarakat Indonesia",
                "main | verb | acting as an actor in a play (film, music, etc.) | dia sering ikut main dalam pementasan drama di sekolah",
                "pada | particle | preposition used to indicate position above or in relation to or in relation to, meaning in (used in front of nouns, personal pronouns, adverbs of time) or to | pada dasarnya; ada padanya (-ku, -mu); pada keesokan harinya",
                "pagi | noun | early part of the day | ia bangun pukul 05.00 pagi",
                "hari | noun | conditions (air, nature, etc.) that occur within 24 hours | kalau hari mendung, saya tidak datang; hari baru pukul enam petang",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
            ]
        ),
        "output": "Sungguh luar biasa penampilan tarian tradisional yang para siswa sekolah dasar main pada pagi hari ini!",
        "translation": "The traditional dance performance by the elementary school students this morning is amazing!",
    },
    {
        "word_candidates": "\n".join(
            [
                'sebuah | noun | a fruit | ia menciptakan sebuah lagu *(Catatan: entri kamus menyatakan "sebuah" namun maknanya untuk benda)*',
                "jembatan | noun | roads (of bamboo, wood, concrete, etc.) stretched over rivers (ravines, base edges, etc.); big footbridge | N/A",
                "panjang | adjective | long distance (from end to end) | jalan yang panjang itu akan ditempuhnya dalam 30 menit",
                "yang | particle | a word that states that the next part of the sentence explains the word in front | dijumpainya seorang pengemis yang sedang berteduh di bawah pohon asam itu",
                "menghubungkan | verb | make connected (continuous); connect | garis itu menghubungkan titik A dengan titik B",
                "dua | numeral | numbers symbolized by the numbers 2 (Arabic) or II (Roman) | N/A",
                "desa | noun | a territorial unit inhabited by a number of families who have their own system of government (headed by a village head) | N/A",
                "terpencil | verb | separately; isolated; far from others | beliau lahir di sebuah kampung terpencil",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "akhirnya | adverb | the end | akhirnya kita juga yang harus menderita rugi",
                "selesai | verb | ready-made (about something made); done | mudah-mudahan pembuatan jembatan itu dapat selesai akhir tahun ini",
                "pengerjaan | noun | process, method, act of doing something; processing | N/A",
                "pemerintah | noun | a system of exercising authority and power that regulates the social, economic and political life of a country or its parts | N/A",
                "daerah | noun | government environment; region | N/A",
                "setempat | noun | (in) the place (country, city, etc.) itself | para calon imam dan khatib dididik sesuai dengan kebutuhan masjid setempat",
            ]
        ),
        "output": "Sebuah jembatan panjang yang menghubungkan dua desa terpencil itu akhirnya selesai pengerjaan pemerintah daerah setempat.",
        "translation": "A long bridge connecting two remote villages has finally been completed by the local government.",
    },
    {
        "word_candidates": "\n".join(
            [
                "apabila | particle | If; if | apabila keadaan mengizinkan, tahun depan saya akan meneruskan kuliah",
                "kamu | pronoun | who is spoken to; who is addressed (in a friendly or rude way) | N/A",
                "rajin | adjective | likes to work (studying and so on); diligent; really work; always try hard | rajin lah belajar supaya naik kelas",
                "belajar | verb | trying to gain intelligence or knowledge | adik belajar membaca",
                "setiap | numeral | each | N/A",
                "hari | noun | time from morning to morning (i.e. one rotation of the earth on its axis, 24 hours) | seminggu ada tujuh hari",
                "maka | particle | conjunctions to express relationships, consequences, implications | saya tidak dapat mengetik dengan baik, maka surat undangan itu saya tulis saja",
                "kamu | pronoun | who is spoken to; who is addressed (in a friendly or rude way) | N/A",
                "pasti | adjective | is fixed; must not; Of course; must | dia sudah berjanji besok pasti datang; jika diberkahi Tuhan, usaha kita pasti berhasil",
                "akan | adverb | (to express something that is about to happen, means) will | disangkanya hari akan hujan",
                "mendapatkan | verb | get; obtain | Indonesia telah mendapatkan pasaran minyak di Asia",
                "nilai | noun | intelligence number; seeds; ponten | rata-rata nilai mata pelajarannya adalah sembilan...",
                "sangat | adverb | especially (things, circumstances, etc.); very; too | rumahnya sangat jauh dari sini",
                "memuaskan | verb | adequate (hopes, desires, etc.); pleasant | hasil ujiannya tahun ini sangat memuaskan",
                "nanti | noun | a time not long from now; later time; later | hal itu akan kita bicarakan nanti; nanti saya akan menelepon Anda lagi; sampai bertemu lagi nanti",
            ]
        ),
        "output": "Apabila kamu rajin belajar setiap hari maka kamu pasti akan mendapatkan nilai sangat memuaskan nanti.",
        "translation": "If you study diligently every day, you will definitely get very satisfying grades later.",
    },
    {
        "word_candidates": "\n".join(
            [
                "pemandangan | noun | beautiful natural conditions to look at | di Pantai Senggigi, Lombok, banyak pemandangan yang indah",
                "alam | noun | everything in the heavens and on the earth (such as the earth, stars, powers) | alam sekeliling",
                "di | particle | preposition to mark a place | semalam ia tidur di rumah temannya",
                "desa | noun | a group of houses outside the city that form a unit | di desa itu belum ada listrik",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "jauh | adjective | many; very; very (about differences, discrepancies or shortcomings) | anak itu jauh lebih besar daripada kakaknya",
                "lebih | adverb | increase; increasingly | kesehatannya sudah lebih baik; harganya menjadi lebih mahal",
                "indah | adjective | in a condition pleasing to the eye; Beautiful; beautiful | N/A",
                "daripada | particle | preposition to mark a comparison | buku ini lebih bagus daripada buku itu",
                "tempat | noun | space (field, house, and so on) available to do something | tempat belajar; tempat duduk",
                "wisata | noun | activities to have fun, expand knowledge, etc., carried out by traveling to a certain place, usually together; tourist | N/A",
                "yang | particle | a word that states that the next part of the sentence explains the word in front | dijumpainya seorang pengemis yang sedang berteduh di bawah pohon asam itu",
                "pernah | adverb | have experienced (experienced and so on) | ia sendiri pernah dihukum; belum (tidak) pernah belum sekali pun mengalami dan sebagainya",
                "kita | pronoun | plural first person pronouns, which speak together with other people, including those being spoken to | N/A",
                "tuju | verb | going to | N/A",
                "bersama | adverb | together; simultaneously | kami berangkat bersama ke sekolah",
            ]
        ),
        "output": "Pemandangan alam di desa ini jauh lebih indah daripada tempat wisata yang pernah kita tuju bersama.",
        "translation": "The natural scenery in this village is far more beautiful than the tourist spot we have visited together.",
    },
]
