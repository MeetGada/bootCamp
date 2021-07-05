from hashlib import md5, sha1, sha256, sha512, pbkdf2_hmac

data = b"ShapeAI"
md5 = md5(data)
sha1 = sha1(data)
sha256 = sha256(data)
sha512 = sha512(data)

hashes = [md5, sha1, sha256, sha512]
print('\nSalt: HelloWorld')

for algo in hashes:
    print('\n{} : {}'.format(algo.name, algo.hexdigest()))
    print('Salted Hash:-> {}'.format(pbkdf2_hmac(algo.name, data, b'HelloWorld', 10000).hex()))