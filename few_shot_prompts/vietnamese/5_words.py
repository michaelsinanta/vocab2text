"""5-word few-shot examples for vietnamese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "đang | adverb | A particle indicating that an action or state is currently in progress and has not yet finished at the reference point in time (usually the moment of speaking); equivalent to the progressive aspect (-ing). | trời đang mưa to * đang mải suy nghĩ * đang học đại học",
                "uống | verb | to drink; to take liquid into the mouth and swallow it | uống thuốc * uống rượu",
                "cà phê | noun | A medium-sized shrub with opposite leaves, white flowers, and small red berries when ripe, whose seeds are roasted and ground to make a beverage; coffee. | cây cà phê * nhấm nháp li cà phê",
                "nóng | adjective | having a temperature higher than human body temperature, or higher than what is considered average | nước nóng * xấu hổ, mặt nóng bừng * trời nóng kéo dài",
            ]
        ),
        "output": "Tôi đang uống cà phê nóng.",
        "translation": "I am drinking hot coffee.",
    },
    {
        "word_candidates": "\n".join(
            [
                'ngày ngày | adverb | (colloquial) day after day, day in and day out, every single day (referring to an action repeated over time) | ngày ngày cắp sách đến trường * "Song hồ nửa khép cánh mây, Tường đông ghé mắt, ngày ngày hằng trông." (TKiều)',
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "đi | verb | To go or move to another place to perform a certain activity or task | đi ngủ * đi chợ * đi bộ đội * làm đơn đi kiện * chuyến đi biển dài ngày",
                "học | verb | To acquire knowledge or practice skills passed down by others; to learn or study. | học nghề * học đàn * đi một ngày đàng học một sàng khôn (tng)",
            ]
        ),
        "output": "Ngày ngày tôi đi học.",
        "translation": "Every day I go to school.",
    },
    {
        "word_candidates": "\n".join(
            [
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it'). | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "thích | verb | To like, enjoy, or be fond of something or doing something, feeling pleased and comfortable, making one want to experience or do it whenever there is an opportunity. | thích đi du lịch * thích sống tự lập * không thích cuộc sống tù túng",
                "kẹo | noun | candy, sweets; a food item in the form of drops, pieces, or bars, made of sugar or syrup, often with added fats and flavorings | nấu kẹo * viên kẹo * kẹo lạc",
                "bạc hà | noun | A plant in the same family as spearmint, containing aromatic compounds, used for distilling essential oils or as medicine (mint/peppermint). | dầu bạc hà * kẹo bạc hà",
            ]
        ),
        "output": "Cô ấy thích kẹo bạc hà.",
        "translation": "She like peppermint candy.",
    },
    {
        "word_candidates": "\n".join(
            [
                "học sinh | noun | a student at the primary or secondary school level; pupil | học sinh tiểu học * thời học sinh",
                "diễu hành | verb | (of a group of people) to march or parade in formation in front of a grandstand or on the streets to demonstrate strength or express a political stance | đoàn biểu tình diễu hành qua các phố lớn",
                "nghiêm trang | adjective | (of dress, gestures, or speech) highly proper, dignified, and serious, showing a respectful attitude | nét mặt nghiêm trang * đi đứng nghiêm trang",
            ]
        ),
        "output": "Học sinh diễu hành nghiêm trang.",
        "translation": "The students march in solemn formation.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "dự định | verb | To intend or plan to do something, provided there are no changes | dự định mở trường học tư * dự định ăn tết xong sẽ đi",
                "đi | verb | To go or move to another place to perform a certain activity or task | đi ngủ * đi chợ * đi bộ đội * làm đơn đi kiện * chuyến đi biển dài ngày",
                "du học | verb | to study abroad | cho con đi du học * sang Mĩ du học",
            ]
        ),
        "output": "Tôi dự định đi du học.",
        "translation": "I plan to study abroad.",
    },
    {
        "word_candidates": "\n".join(
            [
                "du khách | noun | tourist, traveler, visitor | du khách đến tham quan",
                "thích | verb | To like, enjoy, or be fond of something or doing something, feeling pleased and comfortable, making one want to experience or do it whenever there is an opportunity | thích đi du lịch * thích sống tự lập * không thích cuộc sống tù túng",
                "mua sắm | verb | To shop; to buy or purchase various things for use (general term) | mua sắm đồ đạc",
            ]
        ),
        "output": "Du khách thích mua sắm.",
        "translation": "Tourists like shopping.",
    },
    {
        "word_candidates": "\n".join(
            [
                "nội | noun | (dialect, colloquial) paternal grandfather or paternal grandmother (used as an affectionate short form) | con đi nghe nội!",
                "đèo | verb | To carry or transport someone or something on a bicycle or motorcycle, usually on the back seat or rack | đèo con đến trường * đèo thùng hàng sau xe",
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "đi | verb | To go or move to another place to perform a certain activity or task | đi ngủ * đi chợ * đi bộ đội * làm đơn đi kiện * chuyến đi biển dài ngày",
                "chợ | noun | A public place where people gather to buy and sell goods, which may be held at specific times or on certain days; a market. | phiên chợ * ồn ào như chợ vỡ * đầu đường xó chợ (tng)",
            ]
        ),
        "output": "Nội đèo tôi đi chợ.",
        "translation": "My grandmother takes me to the market.",
    },
    {
        "word_candidates": "\n".join(
            [
                "đám cưới | noun | wedding, wedding ceremony, usually attended by many people | đi dự đám cưới * làm đám cưới",
                "tràn ngập | N/A | to be flooded, overwhelmed, or overflowing with something; to cover or fill a surface or space completely | không gian tràn ngập hương hoa sữa * niềm vui tràn ngập",
                "hạnh phúc | adjective | being in a state of joy and satisfaction from feeling that one's wishes or desires have been fulfilled; happy | năm tháng hạnh phúc * hai người sống rất hạnh phúc",
            ]
        ),
        "output": "Đám cưới tràn ngập hạnh phúc.",
        "translation": "The wedding was filled with happiness.",
    },
    {
        "word_candidates": "\n".join(
            [
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it'). | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "là | particle | A word used to emphasize an affirmative tone or assertion. | quyển sách ấy là của tôi * anh nói như vậy là nó không nghe đâu",
                "giáo viên | noun | A teacher at the general education level or equivalent | giáo viên tiểu học * giáo viên chủ nhiệm",
            ]
        ),
        "output": "Cô ấy là giáo viên.",
        "translation": "She is a teacher.",
    },
    {
        "word_candidates": "\n".join(
            [
                "biển báo | noun | signs placed on roads and in public places to notify about restrictions or characteristics of traffic conditions or public order | biển báo đường một chiều * biển báo cấm hút thuốc",
                "cảnh báo | verb | To warn or alert in advance about a potential danger or emergency. | cảnh báo nguy cơ cháy rừng * rung một hồi chuông cảnh báo",
                "nguy hiểm | noun | danger; hazard; something that causes great harm | bất chấp nguy hiểm * coi thường nguy hiểm",
            ]
        ),
        "output": "Biển báo cảnh báo nguy hiểm.",
        "translation": "The sign warns of danger.",
    },
    {
        "word_candidates": "\n".join(
            [
                "người | noun | a term used to refer to an individual person belonging to a certain category or social class | người lính * người thiếu nữ * người lao động",
                "già | adjective | being at an age characterized by a gradual decline in physiological functions, in the final stage of the natural life cycle; old; aged | bệnh người già * về già * con bò già * mèo già hoá cáo (tng)",
                "thường | adverb | usually, normally, as is common | ông cụ thường thức dậy lúc năm giờ sáng",
                "khó tính | adjective | having a demanding or fastidious nature, not easy-going in social relations, and not easily pleased with anyone or anything; hard to please | người già thường hay khó tính * bà ấy khó tính lắm!",
            ]
        ),
        "output": "Người già thường khó tính.",
        "translation": "The elderly are often hard to please.",
    },
]
