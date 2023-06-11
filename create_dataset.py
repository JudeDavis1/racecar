import hashlib as hl


def hash(s: str) -> str:
    return hl.sha256(s.encode()).hexdigest()

print(hash("Hello, World!"))
