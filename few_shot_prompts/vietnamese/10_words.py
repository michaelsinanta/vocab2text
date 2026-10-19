"""10-word few-shot examples for vietnamese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "học sinh | noun | a student at the primary or secondary school level; pupil | học sinh tiểu học * thời học sinh",
                "ngày nay | noun | the present time, nowadays, today | thời đại ngày nay * ngày nay, đời sống người nông dân đã được cải thiện",
                "thường | adverb | usually, normally, as is common | ông cụ thường thức dậy lúc năm giờ sáng",
                "học vẹt | verb | To learn by heart word for word without understanding anything, like a parrot learning to speak; rote learning. | tránh thói học vẹt",
                "bảng cửu chương | noun | multiplication table (specifically listing the products of integers from 2 times 1 to 9 times 10) | học thuộc lòng bảng cửu chương",
            ]
        ),
        "output": "Học sinh ngày nay thường học vẹt bảng cửu chương",
        "translation": "Students today often memorize multiplication tables by rote.",
    },
    {
        "word_candidates": "\n".join(
            [
                "hoạ sĩ | noun | An artist or painter who specializes in creating artistic paintings, possesses professional skills, and is widely recognized. | ước mơ trở thành hoạ sĩ",
                "đang | adverb | A particle indicating that an action or state is currently in progress and has not yet finished at the reference point in time (usually the moment of speaking); equivalent to the progressive aspect (-ing). | trời đang mưa to * đang mải suy nghĩ * đang học đại học",
                "phác thảo | verb | To write a rough draft or create a model using basic lines to express a creative intention in literature or art. | phác thảo chân dung * bản phác thảo đề án xây dựng",
                "bức | noun | A classifier used for flat, sheet-like objects that have writing or images on their surface | bức thư * đánh một bức điện * bức tranh * vẽ một bức chân dung",
                "tranh | noun | A painting or drawing (a work of art that reflects reality through lines and colors) | tranh biếm hoạ * triển lãm tranh",
                "phong cảnh | noun | natural scenery or landscapes, usually beautiful, presented before one's eyes, such as rivers, mountains, villages, streets, etc. (generally speaking) | phong cảnh làng quê ngày mùa * ngắm phong cảnh",
                "đồng quê | noun | fields in the countryside; generally referring to the countryside or rural areas | hương vị đồng quê",
            ]
        ),
        "output": "Hoạ sĩ đang phác thảo bức tranh phong cảnh đồng quê.",
        "translation": "The artist is sketching a countryside landscape painting.",
    },
    {
        "word_candidates": "\n".join(
            [
                "hôm qua | noun | yesterday; the day immediately preceding today | vừa nói hôm qua, hôm nay đã quên",
                "kẻ trộm | noun | a thief; a person who steals | bị kẻ trộm lẻn vào nhà",
                "đột nhập | verb | to enter suddenly and unexpectedly; to break in, intrude, or infiltrate | kẻ gian đột nhập vào nhà * vi trùng đột nhập vào cơ thể",
                "vào | verb | To move to a position that is inside, narrower, or to the south within Vietnam. | vào Nam ra Bắc * từ ngoài khơi vào đất liền * xe vào nội thành",
                "ngân hàng | noun | An economic organization operating in the business and management of monetary and credit transactions. | chuyển tiền qua ngân hàng * vay vốn của ngân hàng để làm ăn",
                "lấy | verb | To take, seize, or appropriate something belonging to someone else as one's own | lấy bút của bạn * lấy của công làm của riêng * lấy đồn địch",
                "tiền | noun | money; currency (objects cast in metal or printed on paper issued by a central bank, used as a unit of currency) | tiền giấy * tiền xu",
            ]
        ),
        "output": "Hôm qua, kẻ trộm đột nhập vào ngân hàng lấy tiền.",
        "translation": "Yesterday, a thief broke into a bank to steal money.",
    },
    {
        "word_candidates": "\n".join(
            [
                "công ty | noun | A business organization established by multiple members who contribute capital, share profits, or bear losses in proportion to their contributed capital; a company or corporation. | lập công ti * công ti xuyên quốc gia",
                "tổ chức | verb | to organize, arrange, or set up the necessary steps to conduct an activity for the best possible outcome | tổ chức mít tinh * tổ chức sinh nhật",
                "liên hoan | N/A | a party, festival, or social gathering of many people to celebrate a specific occasion | liên hoan văn nghệ * liên hoan mừng chiến thắng * ăn liên hoan",
                "cho | verb | To give, bestow, or transfer ownership of something to someone else without expecting anything in return. | cho quà * cho tiền",
                "nhân viên | noun | An employee or staff member working in an agency or organization, in relation to the head or leadership of that agency or organization | nhân viên kế toán * quan hệ giữa giám đốc và nhân viên",
            ]
        ),
        "output": "Công ty tổ chức liên hoan cho nhân viên.",
        "translation": "The company organized a party for its employees.",
    },
    {
        "word_candidates": "\n".join(
            [
                "chúng tôi | pronoun | we, us (first-person plural pronoun used by a speaker to refer to themselves and others, typically excluding the listener) | ngày mai chúng tôi sẽ đi * công ti chúng tôi",
                "đang | adverb | A particle indicating that an action or state is currently in progress and has not yet finished at the reference point in time (usually the moment of speaking); equivalent to the progressive aspect (-ing). | trời đang mưa to * đang mải suy nghĩ * đang học đại học",
                "sống | verb | To live, reside, or dwell permanently in a certain place or environment, spending all or part of one's life there | sống ở miền Nam * động vật sống dưới nước",
                "ở | verb | To be present at a certain place or location for a specific period or point in time; to stay or be at. | bây giờ tôi đang ở cơ quan * ở có mấy hôm rồi lại đi",
                "chung cư | noun | An apartment building or residential complex, typically high-rise, designed with separate self-contained apartments. | nhà chung cư * căn hộ chung cư",
                "đắt đỏ | adjective | having a price much higher than normal, often due to scarcity; expensive; costly | hàng hoá ngày càng đắt đỏ * giá sinh hoạt đắt đỏ",
            ]
        ),
        "output": "Chúng tôi đang sống ở chung cư đắt đỏ.",
        "translation": "We are living in an expensive apartment building.",
    },
    {
        "word_candidates": "\n".join(
            [
                "con trai | noun | a young male, usually unmarried; a boy or young man | nhà có hai con trai",
                "của | conjunction | A word indicating that the following person or thing has ownership or control over the previously mentioned object; of, belonging to. | chiếc áo của mẹ * tiền của tôi * tài nguyên của đất nước",
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "rất | adverb | very, highly; to a high degree, well above the normal level | cô bé học rất giỏi * cười rất có duyên * tính rất thẳng * rất ghét người hay nói dối",
                "cốc láo | adjective | (colloquial) insolent, impudent, or disrespectful | ăn nói cốc láo",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "nghịch ngợm | adjective | mischievous, naughty, or playful (generally speaking) | tính hay nghịch ngợm",
            ]
        ),
        "output": "Con trai của tôi rất cốc láo và nghịch ngợm.",
        "translation": "My son is very insolent and naughty.",
    },
    {
        "word_candidates": "\n".join(
            [
                "nhờ | conjunction | A word indicating that the following statement is the cause of a good or favorable result; thanks to, owing to | nhờ giời, tôi vẫn mạnh khoẻ * nhờ có anh mà nó mới được như ngày nay",
                'mưa thuận gió hoà | N/A | favorable weather conditions for cultivation and farming | "Lạy trời mưa thuận gió hoà, Để cho chiêm tốt mùa tươi em mừng." (ca dao)',
                "mọi | noun | A word indicating an indefinite quantity, meaning 'every' or 'all' of the things referred to. | mọi người đều đã về hết * đi khắp mọi nơi * làm xong mọi việc",
                "người | noun | the most highly evolved animal, capable of speech, thought, creativity, and using tools in the process of social labor | xã hội loài người * mặt người dạ thú",
                "đều | adverb | A word indicating similarity or uniformity in the action, state, or characteristics of multiple different subjects, often translated as 'all', 'both', or 'equally'. | mọi người đều cảm thấy vui vẻ * cả hai chị em đều học giỏi",
                "mừng rỡ | N/A | joyful, delighted, showing happiness clearly on one's face or through gestures | được gặp lại nhau, ai nấy đều mừng rỡ * con chó ngoáy tít đuôi mừng rỡ",
            ]
        ),
        "output": "Nhờ mưa thuận gió hòa, mọi người đều mừng rỡ.",
        "translation": "With favorable conditions, everyone is joyful",
    },
    {
        "word_candidates": "\n".join(
            [
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it'). | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "đã | adverb | A particle indicating that the action or event occurred before the present or before a specific reference point in the past or future (often corresponding to 'already' or past tense markers in English) | anh ấy đã đi từ hôm qua * đã hứa thì phải giữ lời",
                "thành công | N/A | To achieve the intended result or purpose; to succeed; to be successful | bảo vệ thành công luận án tiến sĩ * đại hội thành công tốt đẹp",
                'dạy | verb | To teach or guide someone to distinguish right from wrong, and to know how to cultivate oneself and behave properly. | "Uốn cây từ thuở còn non, Dạy con từ thuở con còn thơ ngây." (ca dao)',
                "con trai | noun | a young male, usually unmarried; a boy or young man | nhà có hai con trai",
                "nên người | verb | To become a good and useful person | nuôi dạy con cho nên người",
            ]
        ),
        "output": "Cô ấy đã thành công dạy con trai nên người.",
        "translation": "She succeeded in raising her son to become decent and useful human beings.",
    },
    {
        "word_candidates": "\n".join(
            [
                "hắn | pronoun | (colloquial) a third-person pronoun used to refer to someone with a derogatory or familiar/informal tone | tôi đến nhưng hắn đã đi rồi",
                "ta | pronoun | (Colloquial) a word used in conversation to refer to a previously mentioned person, often conveying a dismissive, disrespectful, or casual attitude | cô ta là ai? * hắn ta * lão ta",
                "có | verb | A word indicating the state of existence in the relationship between a person or thing and an attribute, property, or mutual interaction, etc. (to have, to possess, or to be characterized by) | anh ta có lòng tốt * động vật có vú * có công với đất nước * thịt đã có mùi",
                "tiền án | noun | a prior criminal conviction; a criminal record for a previously tried offense | có tiền án về tội trộm cắp",
                "giết | verb | To kill; to intentionally cause death. | giết giặc * can tội giết người",
                "người | noun | the most highly evolved animal, capable of speech, thought, creativity, and using tools in the process of social labor | xã hội loài người * mặt người dạ thú",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "trộm cắp | verb | To steal, to commit theft (generally speaking); theft, thievery | quen thói trộm cắp",
            ]
        ),
        "output": "Hắn ta có tiền án giết người và trộm cắp.",
        "translation": "He has a criminal record for murder and theft.",
    },
    {
        "word_candidates": "\n".join(
            [
                "nhà trường | noun | school (in a general or institutional sense) | rời ghế nhà trường",
                "sẽ | adverb | A word indicating that the event or phenomenon mentioned will occur in the future, after the moment of speaking, or after a certain point in the past used as a reference point (will, shall, would). | mai sẽ làm * tuần sau, anh ấy sẽ về * điều đó chắc chắn sẽ xảy ra",
                "trao | verb | To hand over directly to someone with an attitude of trust and respect; to present, entrust, or award. | trao chìa khoá * trao giải thưởng",
                "học bổng | noun | a scholarship or financial aid granted by the state or an organization to students with high academic achievements to support their education | cấp học bổng cho học sinh nghèo * xin học bổng đi du học",
                "cho | conjunction | A word indicating that the following element is the target or the object affected by what has just been mentioned; equivalent to 'to' or 'for'. | gửi thư cho bạn * đưa tiền cho mẹ * nói cho mọi người rõ * không may cho anh ta",
                "học sinh | noun | a student at the primary or secondary school level; pupil | học sinh tiểu học * thời học sinh",
                "xuất sắc | adjective | achieving outstanding achievements far above the normal level; excellent; outstanding | thành tích xuất sắc * học sinh xuất sắc * cầu thủ xuất sắc",
            ]
        ),
        "output": "Nhà trường sẽ trao học bổng cho học sinh xuất sắc.",
        "translation": "The school will award scholarships to outstanding students.",
    },
]
