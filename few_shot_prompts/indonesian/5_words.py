"""5-word few-shot examples for indonesian.

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
                "sedang | adverb | still (in doing something); Again; only just) | ia sedang belajar mengetik",
                "minum | verb | put water (or a liquid object) in the mouth and gulp it down | hampir setiap pagi ayahku minum susu",
                "kopi | noun | drinks made from coffee powder | N/A",
                "panas | adjective | feels like burning or feels close to fire; relatively high temperature | hari ini udara panas",
            ]
        ),
        "output": "Saya sedang minum kopi panas.",
        "translation": "I am drinking hot coffee.",
    },
    {
        "word_candidates": "\n".join(
            [
                "dia | pronoun | the single persona being discussed, outside the speaker and interlocutor; He | N/A",
                "tidak | adverb | particles to express denial, rejection, denial, and so on; nothing | tempat kerjanya tidak jauh dari rumahnya; apa yang dikatakannya itu tidak benar; baik tidaknya baik atau tidak baik; dapat tidaknya dapat atau tidak; jangan tidak [1] harus [2] tidak boleh tidak; kenal (tahu, melihat) pun tidak sama sekali tidak kenal (tahu, melihat); seorang (suatu, sesen) pun tidak tiada seorang (suatu, sesen) jua pun; yang tidak diadakan yang tidak ada diadakan (diharapkan)",
                "suka | verb | like; like | neneknya suka benar makan sirih; memang banyak orang suka menonton bioskop; ada yang suka daging dan ada juga yang suka ikan laut",
                "makan | verb | put something in the mouth, then chew and swallow it | ia sedang makan pisang",
                "pedas | adjective | tastes like chili or pepper | N/A",
            ]
        ),
        "output": "Dia tidak suka makan pedas.",
        "translation": "He does not like eating spicy food.",
    },
    {
        "word_candidates": "\n".join(
            [
                "apakah | pronoun | Question words to express choices and emphasize the information you want to know | apakah suratku sudah sampai?",
                "kamu | pronoun | who is spoken to; who is addressed (in a friendly or rude way) | N/A",
                "sudah | adverb | has (states an action that has occurred) | ia sudah pandai membaca",
                "mandi | verb | clean the body with water and soap (by splashing, immersing yourself in water, etc.) | hari libur banyak orang mandi di laut",
                "pagi | noun | time after sunrise until midday | ia bekerja keras dari pagi hingga petang",
            ]
        ),
        "output": "Apakah kamu sudah mandi pagi?",
        "translation": "Have you taken a morning shower?",
    },
    {
        "word_candidates": "\n".join(
            [
                "kapan | pronoun | interrogative words to ask for the time | kapan dia akan pergi?",
                "mereka | pronoun | third person plural (him with others); the people being talked about | Toto bertemu dengan Amir di jalan, lalu mereka pergi bersama-sama ke sekolah",
                "akan | adverb | (to express something that is about to happen, means) will | disangkanya hari akan hujan",
                "pulang | verb | go home or to one's native place; back to); back (to) | kapan engkau pulang ke Semarang?; sudah tengah malam ia belum juga pulang; pulang kepada istri pertama rujuk dengan istrinya yang pertama",
                "kampung | noun | village; hamlet | N/A",
            ]
        ),
        "output": "Kapan mereka akan pulang kampung?",
        "translation": "When will they return to their hometown?",
    },
    {
        "word_candidates": "\n".join(
            [
                "tolong | verb | help | minta tolong minta bantuan",
                "bawa | verb | take it somewhere else | N/A",
                "buku | noun | bound sheets of paper, containing writing or blank; book | N/A",
                "merah | adjective | containing or showing a color similar to red | mukanya merah tersipu-sipu",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
            ]
        ),
        "output": "Tolong bawa buku merah itu!",
        "translation": "Please bring that red book!",
    },
    {
        "word_candidates": "\n".join(
            [
                "jangan | adverb | the word prohibiting means not allowed; it shouldn't be necessary | jangan bohong",
                "buang | verb | throw; release; take it out | N/A",
                "sampah | noun | goods or objects that are thrown away because they are no longer used and so on; dirt such as leaves, paper | jangan membuang sampah sembarangan",
                "sembarangan | adjective | not selectively; not with a glance; just... just | menuduh dengan sembarangan saja asal menuduh saja (tidak dengan alasan yang layak); kawin dengan orang sembarangan dengan orang yang tidak terpilih (tidak berasal dan sebagainya); buku itu diletakkan sembarangan saja tidak memilih tempat atau tidak dengan aturan",
                "lagi | adverb | return (act and so on) to the way it was before; repeat as before; also | kemarin sudah menonton, sekarang hendak menonton lagi",
            ]
        ),
        "output": "Jangan buang sampah sembarangan lagi!",
        "translation": "Do not litter again!",
    },
    {
        "word_candidates": "\n".join(
            [
                "wah | particle | interjections to express admiration, surprise, surprise, disappointment | wah, bukan main ramainya Jakarta!",
                "pemandangan | noun | beautiful natural conditions to look at | di Pantai Senggigi, Lombok, banyak pemandangan yang indah",
                "gunung | noun | a very large and high hill (usually more than 600 m high) | N/A",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "indah | adjective | in a condition pleasing to the eye; Beautiful; beautiful | N/A",
            ]
        ),
        "output": "Wah, pemandangan gunung ini indah!",
        "translation": "Wow, this mountain view is beautiful!",
    },
    {
        "word_candidates": "\n".join(
            [
                "kue | noun | snacks made from various ingredients, can be made in various shapes, some are steamed, fried, baked | N/A",
                "itu | pronoun | demonstrative words for objects (time, things) that are far from the speaker | letusan Gunung Krakatau itu sangat dahsyat",
                "dimakan | verb | destroyed; damaged; spent | rumahnya habis dimakan api; pagar besinya keropos dimakan karat",
                "oleh | particle | connecting words to mark the perpetrator | rumah ini dibeli oleh ayahnya bulan lalu; tidak teringat oleh ibuku bahwa hari ini hari ulang tahun anaknya",
                "adik | noun | younger sibling (boy or girl) | adik kandung",
            ]
        ),
        "output": "Kue itu dimakan oleh adik.",
        "translation": "The cake was eaten by my younger sibling.",
    },
    {
        "word_candidates": "\n".join(
            [
                "jika | particle | conjunctions to mark conditions (promises); if | jika hari tidak hujan, saya akan datang; intan itu jika terbenam di pelimbahan sekalipun tiada akan hilang cahayanya",
                "hujan | noun | water droplets falling from the air due to the cooling process | N/A",
                "kami | pronoun | who speaks together with others (excluding those spoken to); who writes on behalf of a group, does not include readers | N/A",
                "tidak | adverb | particles to express denial, rejection, denial, and so on; nothing | tempat kerjanya tidak jauh dari rumahnya; apa yang dikatakannya itu tidak benar; baik tidaknya baik atau tidak baik; dapat tidaknya dapat atau tidak; jangan tidak [1] harus [2] tidak boleh tidak; kenal (tahu, melihat) pun tidak sama sekali tidak kenal (tahu, melihat); seorang (suatu, sesen) pun tidak tiada seorang (suatu, sesen) jua pun; yang tidak diadakan yang tidak ada diadakan (diharapkan)",
                "pergi | verb | leave | setelah mengunci pintu rumah, dia pergi ke tempat kerjanya; pukul lima pagi ia pergi ke stasiun",
            ]
        ),
        "output": "Jika hujan, kami tidak pergi.",
        "translation": "If it rains, we will not go.",
    },
    {
        "word_candidates": "\n".join(
            [
                "gerakan | noun | the act or state of moving (water, sea, machine) | N/A",
                "mobil | noun | land vehicles driven by engine power, with four or more wheels (always even), usually using fuel oil to start the engine; auto; automobile | N/A",
                "ini | pronoun | a word indicating something that is not far from the speaker | buku ini bagus",
                "lebih | adverb | increase; increasingly | kesehatannya sudah lebih baik; harganya menjadi lebih mahal",
                "cepat | adjective | in a short time can cover quite long distances (travel, movement, events, etc.); rate; torrential | ia berlari cepat; kejadian berlalu dengan cepat",
            ]
        ),
        "output": "Gerakan mobil ini lebih cepat.",
        "translation": "This car moves faster.",
    },
]
