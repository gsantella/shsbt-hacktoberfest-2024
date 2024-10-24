txt = input("Input: ")

x = txt.encode(encoding="utf-32",errors="xmlcharrefreplace")

print(x)