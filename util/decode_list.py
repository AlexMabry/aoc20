import re
from types import SimpleNamespace
from typing import List, Sequence, Union


def decode_list(items: List[str], regex: str) -> Sequence[Union[SimpleNamespace, Sequence[str]]]:
    pattern = re.compile(regex)
    if pattern.groupindex.keys():
        return [SimpleNamespace(**pattern.search(item).groupdict()) for item in items]
    else:
        return [pattern.search(item).groups() for item in items]
