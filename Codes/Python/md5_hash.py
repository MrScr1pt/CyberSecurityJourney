import hashlib

def md5_hash(text):
    # Create an instance of the MD5 hash object
    md5 = hashlib.md5()

    # Convert the text to bytes and hash it
    md5.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = md5.hexdigest()

    return hashed_text

# Example usage
text = "a locker room"
hashed_text = md5_hash(text)
print("Text:", text)
print("MD5 Hash:", hashed_text)
