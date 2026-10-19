from typing import Dict, List, Literal, TypedDict, Union


class FewShotExample(TypedDict):
    word_candidates: str
    output: str
    translation: str


# Allowed buckets: 5/10/15/20-word sentences, or a paragraph.
LengthBucket = Literal["5", "10", "15", "20", "paragraph"]
FewShotsByLength = Dict[str, List[FewShotExample]]
LengthKey = Union[int, str]
