#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None

