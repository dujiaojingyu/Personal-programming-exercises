__author__ = "Narwhale"
import hashlib

# m = hashlib.md5()
# m.update(b"Hello")
# print(m.hexdigest())
# print(m.digest())
# m.update(b"It's me")
# print(m.hexdigest())
# print(m.digest())
# m.update(b"It's been a long time since last time we ...")
# print(m.hexdigest())  # 16进制格式hash
# print(m.digest())  # 2进制格式hash
# print(len(m.hexdigest()))  # 16进制格式hash

m = hashlib.sha3_256()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since last time we ...")
print(m.hexdigest())


hash = hashlib.sha256()
hash.update('你好！'.encode(encoding='utf-8'))
print(hash.hexdigest())



import hmac
h = hmac.new('年后'.encode(encoding='utf-8'), '瑟吉欧'.encode(encoding='utf-8'))
print (h.hexdigest())
