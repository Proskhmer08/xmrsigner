from hashlib import sha256
from typing import List, Optional
from polyseed import seed_phrase_from_bytes


def generate_mnemonic_from_bytes(entropy_bytes: bytes, language: str = 'en', timestamp: Optional[int] = None) -> List[str]:  # TODO: 2024-07-02, language selection not working issue in polyseed-python
    return seed_phrase_from_bytes(entropy_bytes, timestamp, language=language).split()
