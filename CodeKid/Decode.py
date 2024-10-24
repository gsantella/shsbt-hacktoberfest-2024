from Encoder import x
byte_seq = x
decoded_string = byte_seq.decode("utf-32", "replace")
print(decoded_string)