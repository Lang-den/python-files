from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash('supersecretpassword')

print(pbkdf2_sha256.verify('supersecretpassword', hash))