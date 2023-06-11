import os
import json
import random
import string
import hashlib as hl

from tqdm import tqdm


def main():
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    
    json_list = []
    for _ in tqdm(range(100000)):
        real = random_string()
        hashed = hash(real)
        json_list.append(make_json(real, hashed))
    
    with open("dataset/sha256.json", "w") as f:
        json.dump(json_list, f, indent=4)


def make_json(real: str, hashed: str) -> dict:
    return {
        "real": real,
        "hashed": hashed
    }

def hash(s: str) -> str:
    return str(hl.sha256(s.encode()).hexdigest())

def random_string(length: int=None, random_length=True) -> str:
    """Generate random string of variable/specified length"""

    assert bool(length) != bool(random_length), "Specify either `length` or `random_length`"

    chars = string.printable
    if length is None:
        length = random.randint(1, 100)
    return "".join([random.choice(chars) for i in range(length)])


if __name__ == "__main__":
    main()
