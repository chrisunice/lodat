import os
import hashlib


def filename_to_sha256_hash(filename):
    sha256_hash = hashlib.sha256(filename.encode()).hexdigest()
    return sha256_hash


def filename_to_md5_hash(filename):
    md5_hash = hashlib.md5(filename.encode()).hexdigest()
    return md5_hash


if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    files = os.listdir(this_dir)

    for f in files:
        print(filename_to_sha256_hash(f))
        print(filename_to_md5_hash(f))
