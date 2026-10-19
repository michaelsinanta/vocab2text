"""15-word few-shot examples for vietnamese.

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
                "chưa | adverb | A word indicating negation, showing that what is referred to has not existed or occurred up to the present or up to a certain point in time considered as a milestone, in the past or future (but may occur afterward); not yet. | trời chưa sáng * chưa biết ai đúng ai sai * trong nhà chưa tỏ, ngoài ngõ đã tường (tng)",
                "kết hôn | verb | To get married; to officially become husband and wife | giấy đăng kí kết hôn * làm lễ kết hôn",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "sinh | verb | to give birth to, to bear (usually referring to humans) | sinh con đầu lòng * bà cụ sinh được ba người con",
                "con | noun | A child or offspring (of humans or animals) in relation to their parents; can also be used as a pronoun or term of address. | lợn nái đẻ được mười con * con hơn cha là nhà có phúc (tng)",
                "bạn bè | noun | friends (in general) | đối xử tốt với bạn bè * hai người là chỗ bạn bè thân thiết",
                "của | conjunction | A word indicating that the following person or thing has ownership or control over the previously mentioned object; of, belonging to | chiếc áo của mẹ * tiền của tôi * tài nguyên của đất nước",
                "cũng | adverb | A word used to assert the similarity in phenomenon, state, activity, or property of the case about to be mentioned compared to those previously mentioned or compared to the past; also, too, as well. | nó cũng nghĩ như anh * đêm ấy trời cũng lạnh như đêm nay",
                "thế | particle | A particle used for emphasis, indicating a connection to a known reality or directly relating to what is being said or asked. | cái quái gì thế? * thế tôi đi nhé! * đi đâu mà về khuya thế?",
            ]
        ),
        "output": "Tôi chưa kết hôn và chưa sinh con, bạn bè của tôi cũng thế.",
        "translation": "I haven't got married or had children yet, and neither have my friends.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "từng | adverb | A word indicating that an action or activity has occurred in the past, or that something has been experienced at some point; once, ever, previously. | hai người đã từng gặp nhau * một sự kiện lớn chưa từng thấy",
                "ước muốn | verb | an earnest desire, wish, or aspiration | ước muốn trở thành người nổi tiếng * ước muốn một cuộc sống hạnh phúc",
                "làm | verb | To use effort to create something that did not exist before; to make, build, write, or produce. | chim làm tổ * làm nhà mới * làm đơn * làm thơ",
                "giáo viên | noun | A teacher at the general education level or equivalent | giáo viên tiểu học * giáo viên chủ nhiệm",
                "nhưng | conjunction | A conjunction used to introduce a statement that contrasts with or contradicts what has just been said or implied; but, however. | việc nhỏ nhưng ý nghĩa lớn * nói nhỏ nhưng vẫn nghe thấy * hứa nhưng không thực hiện",
                "sau này | noun | the period of time after the moment of speaking or a certain referred point in time; in the future, later on | lo cho cuộc sống sau này * mong sau này gặp lại",
                "lại | adverb | A word used to indicate an action or characteristic that is contrary to the normal course of events or expectations (often translated as 'yet', 'instead', 'on the contrary', or used for emphasis in questions). | đã không biết lại còn cãi * sao lại nghĩ thế? * \"Hoa tàn mà lại thêm tươi, Trăng tàn mà lại hơn mười rằm xưa.\" (TKiều)",
                "bác sĩ | noun | a medical doctor who has graduated from a medical school | bác sĩ tim mạch * bác sĩ đa khoa * Ho đã lâu thì nên đi khám bác sĩ.",
            ]
        ),
        "output": "Tôi từng ước muốn làm giáo viên nhưng sau này tôi lại làm bác sĩ.",
        "translation": "I used to dream of being a teacher, but later I became a doctor.",
    },
    {
        "word_candidates": "\n".join(
            [
                "anh | noun | A term used to refer to or address a young man, or a man of the same age or of the same generational rank as one's older brother | anh thanh niên * anh giải phóng quân",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it'). | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "đang | adverb | A particle indicating that an action or state is currently in progress and has not yet finished at the reference point in time (usually the moment of speaking); equivalent to the progressive aspect (-ing). | trời đang mưa to * đang mải suy nghĩ * đang học đại học",
                "cố gắng | N/A | To put in more effort than usual to do something (general term); to make an effort, to try hard, or to strive. | cố gắng học hành * có nhiều cố gắng trong công tác",
                "kiếm | verb | to find a way to obtain or get something; to earn or seek | kiếm cớ thoái thác * kiếm tiền * xoay đủ nghề để kiếm sống",
                "tiền | noun | money; currency (objects cast in metal or printed on paper issued by a central bank, used as a unit of currency) | tiền giấy * tiền xu",
                "mua | verb | To buy, to purchase; to exchange money for goods or items | mua hàng * đi chợ mua thức ăn",
                "điện thoại | noun | telephone; phone (a device that transmits voice from one place to another by wire or radio waves) | nói chuyện qua điện thoại * lắp đặt điện thoại",
                "mới | adjective | new, recently appeared or acquired | tin mới * người bạn mới * sách mới",
                "cho | verb | To give, bestow, or transfer ownership of something to someone else without expecting anything in return. | cho quà * cho tiền",
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
            ]
        ),
        "output": "Anh ấy đang cố gắng kiếm tiền mua điện thoại mới cho cô ấy.",
        "translation": "He is trying to earn money to buy her a new phone.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ngày mai | noun | tomorrow; the day immediately after today | hôm nay là thứ hai, ngày mai là thứ ba",
                "cậu | noun | a term used to address each other intimately among friends, usually between young people | cậu trông cháu cho chị một lúc",
                "không | adverb | a word used to express negation of what follows; no, not | đường vắng, không một bóng người * trong người không được khoẻ * không ai giàu ba họ, không ai khó ba đời (tng)",
                "tham dự | verb | (Formal) to participate in or attend a specific activity | tham dự hội nghị * tham dự phiên toà",
                "tiệc | noun | a feast, banquet, or party; a special meal với many delicious dishes and many guests, held on a celebratory occasion | tiệc sinh nhật * mở tiệc mừng nhà mới",
                "độc thân | adjective | living alone, not married; single | sống độc thân * gần bốn mươi tuổi rồi mà còn độc thân",
                "ở | conjunction | A preposition used to indicate that the following element is the place, location, or time period where an object or event exists or takes place; at, in, on. | đi dự hội nghị ở trên tỉnh * xem phim ở rạp * đau ở vùng thắt lưng",
                "khách sạn | noun | A building constructed with many rooms for the purpose of renting to guests, fully equipped with amenities to serve the lodging and dining needs of travelers; a hotel. | khách sạn năm sao (khách sạn đạt tiêu chuẩn cao nhất)",
                "cùng | conjunction | A word indicating that the person about to be mentioned is the target or recipient of the action, implying a close or reciprocal relationship with the subject (similar to 'with' or 'to'). | biết nói cùng ai * mấy lời xin lỗi cùng bạn đọc",
                "tớ | pronoun | A pronoun used to refer to oneself (I, me) in an informal and friendly manner among peers or friends, typically young people. | cậu giúp tớ việc này nhé * chuyện đó, tớ không biết",
                "à | particle | (colloquial) a particle used in questions to clarify or confirm something that one is somewhat surprised about | vẫn còn ngủ đấy à? * mai đã chủ nhật rồi cơ à? * thế à?",
            ]
        ),
        "output": "Ngày mai cậu không tham dự tiệc độc thân ở khách sạn cùng tớ à?",
        "translation": "Can't you come to the bachelorette party at the hotel with me tomorrow?",
    },
    {
        "word_candidates": "\n".join(
            [
                "chúng ta | pronoun | we (inclusive pronoun used by the speaker to refer to themselves and the listener/interlocutor) | tổ quốc của chúng ta * ngày mai chúng ta sẽ bàn tiếp",
                "cần | verb | necessary, essential, or indispensable; something that must be done or had to avoid negative consequences | việc cần phải đi * những thứ cần dùng * quyển sách rất cần cho mọi người",
                "trồng | verb | To plant; to bury or insert a branch, cutting, or root of a seedling into the ground so that it grows into a plant or tree. | xới đất trồng rau * ăn quả nhớ kẻ trồng cây (tng)",
                "nhiều | adjective | having a large quantity or at a high level; many, much, a lot of | lắm tiền nhiều của * được đi nhiều nơi * nhiều năm đã trôi qua * có tật nói nhiều",
                "cây xanh | noun | greenery or trees planted for environmental protection in general | trồng cây xanh trong thành phố",
                "trên | conjunction | A preposition used to indicate that the following noun or phrase is the location, medium, or context where the activity or event takes place (similar to 'on', 'at', 'in', or 'via'). | gặp nhau trên đường đi công tác * nghe giảng trên lớp * phát biểu trên ti vi",
                "đường phố | noun | streets (in general) | đường phố đông đúc",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phụ",
                "bảo vệ | verb | To protect, defend, or safeguard against any destruction or infringement in order to keep something intact | bảo vệ đê điều * phun thuốc bảo vệ thực vật * bảo vệ độc lập, chủ quyền và toàn vẹn lãnh thổ",
                "môi trường | noun | The entirety of natural and social conditions in which humans or an organism exist and develop, in relation to those humans or organisms; environment. | bảo vệ môi trường sống * môi trường công tác thuận lợi",
            ]
        ),
        "output": "Chúng ta cần trồng nhiều cây xanh trên đường phố để bảo vệ môi trường.",
        "translation": "We need to plant more trees on our streets to protect the environment.",
    },
    {
        "word_candidates": "\n".join(
            [
                "thời | noun | A long period of time roughly defined by certain characteristics or major events; an era, period, or epoch. | thời kháng chiến * thời thanh niên sôi nổi * nổi tiếng một thời",
                "chiến tranh | noun | armed conflict between nations, states, classes, or groups to achieve certain political or economic goals | chiến tranh xâm lược * chiến tranh giải phóng dân tộc * dập tắt lò lửa chiến tranh",
                "các | noun | a word used to indicate a specific plural quantity, referring to all of the entities being mentioned | các ngày trong tuần * các nước trên thế giới",
                "anh hùng | noun | A person of exceptional talent and courage far beyond ordinary people, who achieves great deeds praised by others; a hero. | anh hùng lực lượng vũ trang nhân dân * anh hùng lao động",
                "liệt sĩ | noun | a person who sacrificed their life while performing a duty; a martyr | nghiêng mình tưởng niệm linh hồn các liệt sĩ * nghĩa trang liệt sĩ",
                "đã | adverb | A particle indicating that the action or event occurred before the present or before a specific reference point in the past or future (often corresponding to 'already' or past tense markers in English). | anh ấy đã đi từ hôm qua * đã hứa thì phải giữ lời",
                "hi sinh | verb | To die for one's country, duty, and noble ideals; to sacrifice one's life. | hi sinh ngoài chiến trường",
                "vì | conjunction | A word indicating that what is about to be mentioned is the reason or cause of what has just been said; because, because of, due to, for. | mất xe vì không cẩn thận * yêu vì nết, trọng vì tài * thi trượt vì lười học",
                "dân tộc | noun | The name for communities of people who share a common language, territory, economy, and cultural tradition; nation, ethnic group, or people. | dân tộc Việt Nam * cuộc đấu tranh giải phóng dân tộc",
            ]
        ),
        "output": "Thời chiến tranh, các anh hùng liệt sĩ đã hi sinh vì dân tộc.",
        "translation": "During the war, many martyrs sacrificed their lives for the country.",
    },
    {
        "word_candidates": "\n".join(
            [
                "gia đình | noun | A group of people living together as the smallest unit in society, bound by marriage and blood relations, typically consisting of spouses, parents, and children. | xây dựng gia đình * một gia đình hạnh phúc",
                "của | conjunction | A word indicating that the following person or thing has ownership or control over the previously mentioned object; of, belonging to | chiếc áo của mẹ * tiền của tôi * tài nguyên của đất nước",
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it'). | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "có | verb | A word indicating the state of existence in the relationship between a whole and its parts (to have, to consist of). | nhà có năm gian * sách có ba chương * chuyện kể có đầu có đuôi",
                "ông bà | noun | grandparents (collectively); often used to refer generally to ancestors, in relation to descendants | ruộng vườn của ông bà để lại",
                "bố | noun | (dialectal) father (can be used as a term of address) | bố nào con nấy * bố chồng",
                "mẹ | noun | A woman who has a child, in relation to her child (also used as a term of address); mother | cha sinh mẹ dưỡng * sắp được làm mẹ * con lại đây với mẹ",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "em gái | noun | younger sister (biological, female, distinguished from cousin or sister-in-law) | cô em gái * quý em dâu như em gái",
                'phỏng | particle | (colloquial) a word used to ask a question, but actually to confirm what one has already asserted, meaning "isn\'t it?" or "right?" | chị mệt lắm phỏng? * anh muốn gây sự đấy phỏng?',
            ]
        ),
        "output": "Gia đình của cô ấy có ông bà, bố, mẹ và em gái phỏng?",
        "translation": "Her family has her grandparents, parents, and a younger sister, doesn't it?",
    },
    {
        "word_candidates": "\n".join(
            [
                "anh trai | noun | elder brother (biological, as distinguished from a male cousin or brother-in-law) | nhà có hai anh trai",
                "của | conjunction | A word indicating that the following person or thing has ownership or control over the previously mentioned object; of, belonging to | chiếc áo của mẹ * tiền của tôi * tài nguyên của đất nước",
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "quyết định | verb | To make a firm decision on a specific action, choosing one among several possibilities after careful consideration; to decide. | quyết định xin chuyển công tác về gần nhà * tự quyết định mọi việc trong nhà",
                "học | verb | To acquire knowledge or practice skills passed down by others; to learn or study. | học nghề * học đàn * đi một ngày đàng học một sàng khôn (tng)",
                "thêm | verb | To add, increase, or make/become greater in quantity or degree | mặc thêm áo cho đỡ lạnh * góp thêm ý kiến",
                "ngoại ngữ | noun | foreign language | học ngoại ngữ * biết hai ngoại ngữ",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "đi | verb | To go or move to another place to perform a certain activity or task | đi ngủ * đi chợ * đi bộ đội * làm đơn đi kiện * chuyến đi biển dài ngày",
                "du học | verb | to study abroad | cho con đi du học * sang Mĩ du học",
            ]
        ),
        "output": "Anh trai của tôi quyết định học thêm ngoại ngữ để đi du học.",
        "translation": "My older brother decided to learn another foreign language so as to study abroad.",
    },
    {
        "word_candidates": "\n".join(
            [
                "cô | noun | A term used to refer to or address a young girl or a young woman. | mấy cô, cậu học trò * cô hàng xén * cô giao liên của trung đoàn",
                "ấy | pronoun | A word used to refer to something already mentioned or known, but which is not near the speaker or does not belong to the present (equivalent to 'that', 'those', or used to form pronouns like 'she/he/it') | đưa cho tôi quyển sách ấy * cô ấy chưa đến * ngày ấy đã xa rồi * rau nào sâu ấy (tng)",
                "là | particle | A word used to emphasize an affirmative tone or assertion. | quyển sách ấy là của tôi * anh nói như vậy là nó không nghe đâu",
                "người | noun | the most highly evolved animal, capable of speech, thought, creativity, and using tools in the process of social labor | xã hội loài người * mặt người dạ thú",
                "hướng nội | verb | introverted; turning inward toward oneself; opposite of extroverted | sống hướng nội",
                "nên | conjunction | A word indicating the relationship between cause and effect; so, therefore | vì lười nên dốt * bận nên không đến được",
                "không | adverb | a word used to express negation of what follows; no, not | đường vắng, không một bóng người * trong người không được khoẻ * không ai giàu ba họ, không ai khó ba đời (tng)",
                "thích | verb | To like, enjoy, or be fond of something or doing something, feeling pleased and comfortable, making one want to experience or do it whenever there is an opportunity. | thích đi du lịch * thích sống tự lập * không thích cuộc sống tù túng",
                "nói chuyện | verb | To talk or chat with each other in a natural way about everyday matters in communication | vừa đi vừa nói chuyện * không nói chuyện trong giờ học",
                'cùng | conjunction | A word indicating that the person or thing about to be mentioned shares a common relationship (in terms of action, characteristic, or function) with the person or thing just mentioned; with, together with, along with. | nó đến cùng với bạn * "Nàng về nuôi cái cùng con, Để anh đi trẩy nước non Cao Bằng." (ca dao)',
                "mọi | noun | A word indicating an indefinite quantity, meaning 'every' or 'all' of the things referred to. | mọi người đều đã về hết * đi khắp mọi nơi * làm xong mọi việc",
            ]
        ),
        "output": "Cô ấy là người hướng nội nên không thích nói chuyện cùng mọi người.",
        "translation": "She is an introvert, so she doesn't like talking to other people.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "mua | verb | To buy, to purchase; to exchange money for goods or items | mua hàng * đi chợ mua thức ăn",
                "điện thoại | noun | telephone; phone (a device that transmits voice from one place to another by wire or radio waves) | nói chuyện qua điện thoại * lắp đặt điện thoại",
                "mới | adjective | new, recently appeared or acquired | tin mới * người bạn mới * sách mới",
                "nhưng | conjunction | A conjunction used to introduce a statement that contrasts with or contradicts what has just been said or implied; but, however. | việc nhỏ nhưng ý nghĩa lớn * nói nhỏ nhưng vẫn nghe thấy * hứa nhưng không thực hiện",
                "cửa hàng | noun | A commercial business establishment or a small service business; a shop or store | cửa hàng thời trang * mở cửa hàng bách hoá",
                "lại | adverb | A word used to indicate an action or characteristic that is contrary to the normal course of events or expectations (often translated as 'yet', 'instead', 'on the contrary', or used for emphasis in questions). | đã không biết lại còn cãi * sao lại nghĩ thế? * \"Hoa tàn mà lại thêm tươi, Trăng tàn mà lại hơn mười rằm xưa.\" (TKiều)",
                'bán | verb | to sell; to exchange goods for money | bán sức lao động * mua rẻ bán đắt * "Cách sông nên phải luỵ đò, Tối trời nên phải luỵ o bán dầu." (ca dao)',
                "cho | conjunction | A word indicating that the following element is the target or the object affected by what has just been mentioned; equivalent to 'to' or 'for'. | gửi thư cho bạn * đưa tiền cho mẹ * nói cho mọi người rõ * không may cho anh ta",
                "cái | noun | A classifier used to denote individual units of inanimate objects. | cái bàn này cao * cái áo hoa * hai cái nhà mới",
                "bị | verb | A word indicating that the subject is the recipient of an unpleasant or disadvantageous action or event. | bị đòn * mảnh vườn bị tàn phá nặng",
                "hỏng | adjective | broken, damaged, ruined, or in a state of no longer being usable | xe hỏng máy * phá hỏng * một bên mắt bị hỏng",
            ]
        ),
        "output": "Tôi mua điện thoại mới nhưng cửa hàng lại bán cho tôi cái bị hỏng.",
        "translation": "I bought a new phone, but the store sold me a broken one.",
    },
]
