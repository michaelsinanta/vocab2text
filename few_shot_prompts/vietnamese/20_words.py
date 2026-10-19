"""20-word few-shot examples for vietnamese.

Append another dict to EXAMPLES to add a few-shot.
"""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "cung điện | noun | The residence and workplace of a monarch; a palace. | cung điện của nhà vua",
                "kia | pronoun | A word used to indicate an object, location, or phenomenon that is far from the speaker's position but within a visible range; that, over there, out there. | ngoài kia nắng rất đẹp * đây là chị tôi còn kia là em tôi",
                "có | verb | A word indicating a state of existence in general; to exist, to have, there is/are. | có bóng người ngoài cửa sổ * trong túi có tiền * lúc có lúc không",
                "phong cách | noun | systematic characteristics of thought and art, expressed in the works of an artist or in works of the same genre in general; style | phong cách của Nguyễn Du * phong cách thơ mới",
                "cổ điển | adjective | classical, traditional, following old ways or established long ago; opposite of modern | lối tư duy cổ điển * cách làm cổ điển",
                "kiến trúc | noun | the art of designing and decorating houses or buildings; architecture | ngôi nhà có kiến trúc độc đáo * học ngành kiến trúc",
                "độc đáo | adjective | unique, original, distinctive; having its own special character, not imitating anything pre-existing, and not to be confused with others | một ý tưởng hết sức độc đáo * ngôi nhà có kiến trúc độc đáo",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "vô cùng | adverb | extremely, infinitely, or to the highest degree; beyond description | vô cùng đau xót * ghét vô cùng * đẹp vô cùng",
                "tráng lệ | adjective | (công trình kiến trúc) to lớn và đẹp một cách lộng lẫy | lâu đài tráng lệ",
                "lộng lẫy | adjective | splendidly beautiful and luxurious; gorgeous | trang phục lộng lẫy * sắc đẹp lộng lẫy",
            ]
        ),
        "output": "Cung điện kia có phong cách cổ điển, kiến trúc độc đáo và vô cùng tráng lệ, lộng lẫy.",
        "translation": "That palace has a classical style, unique architecture, and is extremely magnificent and splendid.",
    },
    {
        "word_candidates": "\n".join(
            [
                "tôi | pronoun | I, me (first-person singular pronoun used to refer to oneself when speaking to peers or in neutral contexts without expressing specific emotional attitudes; in Southern dialects, often pronounced as 'tui') | Việc của tôi cứ để tôi làm. * quê hương tôi * \"Chồng gì anh, vợ gì tôi, Chẳng qua là cái nợ đời chi đây!\"",
                "mong muốn | verb | To desire, wish, or hope to obtain or achieve something | mong muốn một gia đình hạnh phúc * đạt kết quả như mong muốn",
                "kiếm | verb | to find a way to obtain or get something; to earn or seek | kiếm cớ thoái thác * kiếm tiền * xoay đủ nghề để kiếm sống",
                "nhiều | adjective | having a large quantity or at a high level; many, much, a lot of | lắm tiền nhiều của * được đi nhiều nơi * nhiều năm đã trôi qua * có tật nói nhiều",
                "tiền | noun | money; currency (objects cast in metal or printed on paper issued by a central bank, used as a unit of currency) | tiền giấy * tiền xu",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "mua | verb | To buy, to purchase; to exchange money for goods or items | mua hàng * đi chợ mua thức ăn",
                "nhà | noun | a building or structure with a roof and walls, used for living in or for a specific purpose | xây nhà * căn nhà lá * đồ đạc để đầy nhà * nhà dột từ nóc dột xuống (tng)",
                "xe | noun | a wheeled land vehicle used for travel or transport | đi xe * chạy xe nhanh * đánh xe ra khỏi ga ra",
                "vì thế | conjunction | A word used to indicate that what is about to be mentioned has its reason or cause in what was just stated; therefore, for that reason. | không đi học đều, vì thế không hiểu bài",
                "bắt đầu | verb | To begin, start, or enter the initial stage of an activity, process, or state | một ngày mới bắt đầu * trẻ bắt đầu tập đi * thời tiết đã bắt đầu ấm dần lên",
                "khởi nghiệp | verb | to start a career; to start a business | khởi nghiệp với hai bàn tay trắng",
                "cùng | adjective | sharing the same identity, characteristics, or having things in common; same, shared | anh em cùng cha khác mẹ * có cùng một sở thích",
                "bạn bè | noun | friends (in general) | đối xử tốt với bạn bè * hai người là chỗ bạn bè thân thiết",
            ]
        ),
        "output": "Tôi mong muốn kiếm nhiều tiền để mua nhà, xe vì thế tôi bắt đầu khởi nghiệp cùng bạn bè.",
        "translation": "I want to earn a lot of money to buy a house and a car, so I have started a business with my friends.",
    },
    {
        "word_candidates": "\n".join(
            [
                "hôm qua | noun | yesterday; the day immediately preceding today | vừa nói hôm qua, hôm nay đã quên",
                "thời tiết | noun | the state of the atmosphere at a particular place and time, such as temperature, humidity, rain, wind, etc. | dự báo thời tiết * thời tiết ấm áp",
                "đang | adverb | A particle indicating that an action or state is currently in progress and has not yet finished at the reference point in time (usually the moment of speaking); equivalent to the progressive aspect (-ing). | trời đang mưa to * đang mải suy nghĩ * đang học đại học",
                "oi bức | adjective | stiflingly hot and humid; muggy or sultry (generally speaking) | trời oi bức, không có lấy một ngọn gió",
                "ngột ngạt | adjective | stifling, suffocating, or stuffy; having a feeling of difficulty breathing due to heat or lack of air | hơi nóng ngột ngạt * căn phòng ngột ngạt",
                "thì | conjunction | A conjunction indicating a sequential relationship between two events, where one occurs immediately after the other | vừa về đến nhà thì trời đổ mưa",
                "đột nhiên | adverb | suddenly, abruptly (referring to an action or process happening in a very sudden manner) | đang đi đột nhiên đứng lại * giá xi măng đột nhiên tăng vọt",
                "mưa rào | noun | heavy rain with large drops that starts and stops quickly, usually caused by thunderclouds; a shower | trận mưa rào",
                'khiến | verb | To affect, to cause or provoke a certain psychological or emotional reaction; to make or cause (someone to do or feel something). | tiếng động khiến mọi người tỉnh giấc * "Bốn dây như khóc, như than, Khiến người trên tiệc cũng tan nát lòng!" (TKiều)',
                "không khí | noun | the mixture of gases surrounding the Earth, consisting mainly of nitrogen and oxygen, which is essential for the life of humans and other organisms | càng lên cao không khí càng loãng * hít thở bầu không khí trong lành",
                "vô cùng | adverb | extremely, infinitely, or to the highest degree; beyond description | vô cùng đau xót * ghét vô cùng * đẹp vô cùng",
                "trong lành | adjective | pure, clean, and beneficial to human health (usually referring to air or climate); fresh | khí hậu trong lành * hít thở bầu không khí trong lành",
            ]
        ),
        "output": "Hôm qua, thời tiết đang oi bức, ngột ngạt thì đột nhiên mưa rào khiến không khí vô cùng trong lành.",
        "translation": "Yesterday, the weather was hot and stufffy when a sudden rain shower made the air much fresher.",
    },
    {
        "word_candidates": "\n".join(
            [
                "đội | noun | A tightly organized group of a specific number of people working together on a common task; a team, squad, unit, or band. | đội du kích Bắc Sơn * đội kèn * đội tuyển quốc gia",
                "bóng rổ | noun | a sport played by two teams in which players use their hands to control the ball and try to throw it into the opponent's netted hoop, called a basket | trận thi đấu bóng rổ * sân bóng rổ",
                "nữ | adjective | (of items or sports) specifically for women or girls; women's | xe đạp nữ * bóng đá nữ",
                "của | conjunction | A word indicating that the following person or thing has ownership or control over the previously mentioned object; of, belonging to | chiếc áo của mẹ * tiền của tôi * tài nguyên của đất nước",
                "trường | noun | school (usually used in a specific sense or context) | trường viết văn * trường đại học * học sinh đến trường",
                "đã | adverb | A particle indicating that the action or event occurred before the present or before a specific reference point in the past or future (often corresponding to 'already' or past tense markers in English). | anh ấy đã đi từ hôm qua * đã hứa thì phải giữ lời",
                "giành | verb | To strive, struggle, or compete to obtain, win, or keep something for oneself, preventing it from being taken by others | giành nhau miếng mồi * đấu tranh giành độc lập * giành giải nhất",
                "chiến thắng | noun | victory or triumph achieved in combat or war | chiến thắng Điện Biên Phủ * liên hoan mừng chiến thắng",
                "đầy | adjective | being in a state of having a large quantity or being filled với something throughout; full of, filled with | trời đầy sao * cơ thể đầy sức sống * chặng đường đầy thử thách",
                "thuyết phục | N/A | To persuade or convince someone by making them see the correctness or value of something so that they believe or follow it. | thuyết phục mãi nó mới đồng ý * lập luận chặt chẽ đầy sức thuyết phục",
                "trong | conjunction | A preposition used to indicate that the following element is the time limit or duration of the mentioned activity or event; equivalent to 'within', 'during', or 'in'. | đi ngay trong đêm nay * công trình hoàn thành trong ba năm",
                "trận | noun | a match, game, or contest in which competitors vie to win or lose | trận bóng đá * thắng liên tiếp mấy trận liền",
                "chung kết | noun | The final round of a competition or tournament to determine the champion or first-place winner. | trận chung kết bóng đá * lọt vào vòng chung kết cuộc thi hoa hậu",
                "hôm qua | noun | yesterday; the day immediately preceding today | vừa nói hôm qua, hôm nay đã quên",
            ]
        ),
        "output": "Đội bóng rổ nữ của trường đã giành chiến thắng đầy thuyết phục trong trận chung kết hôm qua.",
        "translation": "The school's women's basketball team won the championship game convincingly yesterday.",
    },
    {
        "word_candidates": "\n".join(
            [
                "chính phủ | noun | The highest executive and administrative organ of a country, responsible for state management at the central level; the government. | thủ tướng chính phủ * dự án được chính phủ phê duyệt",
                "ban hành | verb | To promulgate, issue, or enact (legal documents, policies, etc.) | ban hành hiến pháp * ban hành một điều luật mới",
                "đạo luật | noun | a legal document or statute enacted by the state | đạo luật chống độc quyền",
                "mới | adjective | new, recently appeared or acquired | tin mới * người bạn mới * sách mới",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "điều chỉnh | verb | to adjust, modify, or rearrange slightly to make something more correct, accurate, or reasonable | điều chỉnh mức lương * điều chỉnh giá xăng dầu",
                "quy định | N/A | To stipulate, regulate, or lay down rules to be followed and implemented in work or specific activities | quy định thời gian làm việc * làm đủ các thủ tục theo quy định",
                "liên quan | verb | to be related, connected, or relevant to each other | hai vấn đề có liên quan mật thiết với nhau * việc đó chẳng liên quan gì tới tôi",
                "tới | conjunction | To reach, affect, or refer to a certain object or target | đừng động tới nó * tác động tới tinh thần * chuyện đó, tôi chưa nghĩ tới",
                "trí tuệ | noun | The capacity for rational perception and understanding that has reached a certain level; intellect, intelligence, or wisdom. | trí tuệ minh mẫn * sản phẩm trí tuệ * quyền sở hữu trí tuệ",
                "nhân tạo | adjective | man-made, artificial, modeled after what exists in nature | tơ nhân tạo * hô hấp nhân tạo * thụ tinh nhân tạo",
            ]
        ),
        "output": "Chính phủ ban hành đạo luật mới để điều chỉnh quy định liên quan tới trí tuệ nhân tạo.",
        "translation": "The government enacted a new law to regulate regulations related to artificial intelligence.",
    },
    {
        "word_candidates": "\n".join(
            [
                "nhà trường | noun | school (in a general or institutional sense) | rời ghế nhà trường",
                "dự định | verb | To intend or plan to do something, provided there are no changes | dự định mở trường học tư * dự định ăn tết xong sẽ đi",
                "tổ chức | verb | to organize, arrange, or set up the necessary steps to conduct an activity for the best possible outcome | tổ chức mít tinh * tổ chức sinh nhật",
                "cuộc | noun | An event, situation, affair, or gathering that unfolds over a period of time and involves multiple participants (often used as a classifier for meetings, games, campaigns, etc.) | người ngoài cuộc * cuộc họp giao ban * cuộc vui chưa tàn",
                "thi | verb | To compete or participate in a contest of talent, strength, etc., to win a prize | thi chạy * thi toán quốc tế * đoạt giải nhất cuộc thi giọng hát hay toàn quốc",
                "hùng biện | verb | To speak eloquently with tight reasoning and strong persuasiveness; eloquent. | có tài hùng biện",
                "nhằm | conjunction | A word indicating that what is about to be mentioned is the target or goal of the action just described; aiming to, in order to, with the purpose of. | làm thế nhằm trấn an dư luận * thực hiện nhiều biện pháp nhằm đẩy mạnh sản xuất",
                "khuyến khích | verb | To encourage, motivate, or stimulate someone's spirit to make them feel excited, confident, and strive harder | khuyến khích các em học tập * giải khuyến khích",
                "học sinh | noun | a student at the primary or secondary school level; pupil | học sinh tiểu học * thời học sinh",
                "tự tin | verb | to believe in oneself; to be self-confident | tự tin ở sức mình * giọng nói dứt khoát, đầy vẻ tự tin",
                "giao tiếp | verb | to communicate, interact with each other | ngôn ngữ là công cụ giao tiếp * biết cách giao tiếp",
            ]
        ),
        "output": "Nhà trường dự định tổ chức cuộc thi hùng biện nhằm khuyến khích học sinh tự tin giao tiếp.",
        "translation": "The school plans to organize a speaking competition to encourage students to communicate confidently.",
    },
    {
        "word_candidates": "\n".join(
            [
                "người | noun | the most highly evolved animal, capable of speech, thought, creativity, and using tools in the process of social labor | xã hội loài người * mặt người dạ thú",
                "tham gia | verb | To participate, take part in, or join in a collective activity. | tham gia cách mạng * tham gia thi tuyển * việc này tôi không tham gia",
                "giao thông | noun | traffic, transport, or the movement of people and vehicles from one place to another | ách tắc giao thông * giao thông đường bộ",
                'phải | verb | to be under obligation, must, have to, cannot do otherwise | ốm thì phải uống thuốc * phải làm cho xong * "Cách sông nên phải luỵ đò, Tối trời nên phải luỵ o bán dầu." (Cdao)',
                "đội | verb | To wear on the head or to carry on the head | đội mũ * đội thúng gạo * đầu đội trời, chân đạp đất (tng)",
                "mũ | noun | An item worn on the head, fitting closely over the hair, used to protect against rain, sun, etc. (In Southern Vietnam, often referred to as 'nón') | đội mũ * đan mũ len * mũ sắt chống đạn",
                "bảo hiểm | verb | To ensure safety, prevent accidents; safety, protective | mũ bảo hiểm * thắt dây bảo hiểm",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "đảm bảo | N/A | To guarantee, ensure, or secure (same as 'bảo đảm') | đời sống được đảm bảo * tôi đảm bảo việc đó là đúng",
                "an toàn | adjective | safe, secure, free from danger, or avoiding accidents | cầu đã được sửa, đi lại rất an toàn * van an toàn",
                "cho | conjunction | A word indicating that the following element is the target or the object affected by what has just been mentioned; equivalent to 'to' or 'for'. | gửi thư cho bạn * đưa tiền cho mẹ * nói cho mọi người rõ * không may cho anh ta",
                "tính mạng | noun | human life | nguy hiểm đến tính mạng * coi thường tính mạng",
                "bản thân | noun | oneself, the very person, or the thing/matter itself being referred to | chính bản thân ông ta nói ra * không làm chủ được bản thân * bản thân sự việc này không có gì quan trọng",
            ]
        ),
        "output": "Người tham gia giao thông phải đội mũ bảo hiểm để bảo đảm an toàn tính mạng cho bản thân.",
        "translation": "Road users must wear helmets to ensure their own safety.",
    },
    {
        "word_candidates": "\n".join(
            [
                'vợ chồng | noun | husband and wife, as a couple (generally speaking) | một cặp vợ chồng hạnh phúc * "Đi đâu có anh có tôi, Người ta mới biết rằng đôi vợ chồng." (ca dao)',
                "chúng tôi | pronoun | we, us (first-person plural pronoun used by a speaker to refer to themselves and others, typically excluding the listener) | ngày mai chúng tôi sẽ đi * công ti chúng tôi",
                "sẽ | adverb | A word indicating that the event or phenomenon mentioned will occur in the future, after the moment of speaking, or after a certain point in the past used as a reference point (will, shall, would). | mai sẽ làm * tuần sau, anh ấy sẽ về * điều đó chắc chắn sẽ xảy ra",
                "đi | verb | To go, move, or travel to another place, regardless of the method or means of transportation | đi chợ * đi máy bay * đi du lịch * đi đến nơi về đến chốn",
                "du lịch | verb | To travel to distant places for pleasure and to learn more about the scenery, people, and life; to go sightseeing or touring. | khu du lịch sinh thái * hướng dẫn viên du lịch * đi du lịch nước ngoài",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "nghỉ ngơi | verb | to rest to recover one's health (general term) | nghỉ ngơi cho lại sức * ăn uống, nghỉ ngơi hợp lí",
                "và | conjunction | A word expressing a coordinating relationship between two things, phenomena, processes, or properties of the same type or category | anh và em * học thêm toán và văn",
                "khám phá | verb | To discover, find out, or uncover something hidden or secret | đoàn thám hiểm khám phá hang động",
                "nhiều | adjective | having a large quantity or at a high level; many, much, a lot of | lắm tiền nhiều của * được đi nhiều nơi * nhiều năm đã trôi qua * có tật nói nhiều",
                "địa điểm | noun | A specific location or venue where an activity is conducted or an event takes place. | địa điểm tập kết hàng * địa điểm đóng quân",
                'nổi tiếng | adjective | famous, well-known, renowned, having a reputation spread far and wide | một ca sĩ nổi tiếng * "Bạc tình nổi tiếng lầu xanh, Một tay chôn biết mấy cành phù dung!" (TKiều)',
            ]
        ),
        "output": "Vợ chồng chúng tôi sẽ đi du lịch để nghỉ ngơi và khám phá nhiều địa điểm nổi tiếng.",
        "translation": "My spouse will travel to relax and explore many famous tourist attractions.",
    },
    {
        "word_candidates": "\n".join(
            [
                "ông bà | noun | grandparents (collectively); often used to refer generally to ancestors, in relation to descendants | ruộng vườn của ông bà để lại",
                "thường | adverb | usually, normally, as is common | ông cụ thường thức dậy lúc năm giờ sáng",
                "kể | verb | To tell, narrate, or recount a story or event in detail to someone else | kể lại những điều mắt thấy tai nghe * nghe bà kể chuyện đời xưa",
                "những | noun | A word used to indicate a plural, indefinite quantity | những vì sao đêm * những ngày thơ ấu * nhớ lại những kỉ niệm xưa",
                "câu chuyện | noun | a story, matter, or conversation that is spoken of or told | câu chuyện thương tâm * đang dở câu chuyện thì có khách",
                "ý nghĩa | noun | The content contained within a form of expression using language, writing, or a certain symbol; meaning; significance. | bài thơ có ý nghĩa châm biếm * lời nói hàm nhiều ý nghĩa",
                "về | conjunction | A preposition used to indicate the direction of an action, or the scope, domain, or subject matter of an activity or quality (equivalent to 'about', 'regarding', 'in', 'towards'). | nhìn về phía trước * giỏi về hoá học * về chuyện này, tôi không có ý kiến gì",
                "gia đình | noun | A group of people living together as the smallest unit in society, bound by marriage and blood relations, typically consisting of spouses, parents, and children. | xây dựng gia đình * một gia đình hạnh phúc",
                'quê hương | noun | one\'s homeland or native land, regarded as a place of natural emotional attachment | nỗi nhớ quê hương * "Thuở còn thơ ngày hai buổi đến trường, Yêu quê hương qua từng trang sách nhỏ." (GNam; 2)',
                "đất nước | noun | the territory of a nation, viewed in relation to the people who own and inhabit it; country, homeland | bảo vệ đất nước * lòng yêu quê hương đất nước",
                "cho | conjunction | A word indicating that the following element is the target or the object affected by what has just been mentioned; equivalent to 'to' or 'for'. | gửi thư cho bạn * đưa tiền cho mẹ * nói cho mọi người rõ * không may cho anh ta",
                "con cháu | noun | children and grandchildren; descendants or future generations in general | lưu truyền cho con cháu mai sau",
                "nghe | verb | To listen; to pay attention in order to hear | nghe giảng * nghe kể chuyện * nghe nhạc",
            ]
        ),
        "output": "Ông bà thường kể những câu chuyện ý nghĩa về gia đình, quê hương, đất nước cho con cháu nghe.",
        "translation": "Grandparents often tell their grandchildren meaningful stories about their family, hometown, and country.",
    },
    {
        "word_candidates": "\n".join(
            [
                "bệnh viện | noun | a medical facility for examining and treating sick people as inpatients; a hospital | bệnh viện đa khoa * bệnh viện nhi",
                "đầu tư | verb | To invest human, material, and financial resources into an endeavor to achieve economic and social efficiency. | chính sách đầu tư hợp lí * đầu tư phát triển ngành thủ công mĩ nghệ * kêu gọi vốn đầu tư",
                "thêm | verb | To add, increase, or make/become greater in quantity or degree | mặc thêm áo cho đỡ lạnh * góp thêm ý kiến",
                "nhiều | adjective | having a large quantity or at a high level; many, much, a lot of | lắm tiền nhiều của * được đi nhiều nơi * nhiều năm đã trôi qua * có tật nói nhiều",
                "thiết bị | noun | the collective whole of machinery, tools, and accessories necessary for a specific activity; equipment | không có thiết bị thay thế * thiết bị quân sự",
                "hiện đại | adjective | modern; applying the latest inventions and achievements of science and technology, as opposed to classical or traditional | máy móc hiện đại * toà nhà sang trọng và hiện đại",
                "để | conjunction | A word used to indicate that the following statement is the purpose, function, or utility of the action or object just mentioned; to, in order to, for. | nhà để ở * có đủ điều kiện để làm việc * nói rõ khó khăn để cùng nhau khắc phục",
                "cải thiện | verb | to improve, to make a situation change for the better | phát triển sản xuất để cải thiện đời sống * cải thiện môi trường đầu tư",
                "chất lượng | noun | The characteristics that constitute the quality or value of a thing or event; quality. | hàng kém chất lượng * nâng cao chất lượng giảng dạy",
                "khám | verb | to examine medically in order to determine health status or diagnose a medical condition in the body | khám sức khoẻ * phòng khám nội",
                "chữa | verb | to cure an illness or to repair/fix something damaged | phòng bệnh hơn chữa bệnh * thợ chữa xe máy",
                "bệnh | noun | a state in which the body or a part of the body is not functioning normally; illness; disease; sickness | lúa bị bệnh rầy nâu * bệnh tim * buồn rầu quá mà sinh bệnh",
                "cho | conjunction | A word indicating that the following element is the target or the object affected by what has just been mentioned; equivalent to 'to' or 'for'. | gửi thư cho bạn * đưa tiền cho mẹ * nói cho mọi người rõ * không may cho anh ta",
                "bệnh nhân | noun | a patient undergoing medical treatment, in relation to a healthcare facility and medical practitioners | bệnh nhân điều trị nội trú * bệnh nhân cấp cứu",
            ]
        ),
        "output": "Bệnh viện đầu tư thêm nhiều thiết bị hiện đại để cải thiện chất lượng khám chữa bệnh cho bệnh nhân.",
        "translation": "The hospital invests in more modern medical equipment to improve the quality of medical examination and treatment for patients.",
    },
]
