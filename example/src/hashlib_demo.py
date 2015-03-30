import hashlib

def sha_1_demo():
    s = hashlib.sha1()
    s.update("test content")
    print(s.digest_size)
    print(s.digest)
    print(s.hexdigest())

sha_1_demo()
