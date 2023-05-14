import os

if os.path.exists("C:/temp/keycode.txt"):
    pass
else:
    key = b'7dsvb5q_bmInW5_nQy8mK-JMiy9ZlLgw-a1tRMCpntA='
    with open("C:/temp/keycode.txt", "wb") as f:
        f.write(key)
with open("C:/temp/keycode.txt", "rb") as f:
    key = f.readline().decode("utf-8").encode("utf-8")

