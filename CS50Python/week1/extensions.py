"""
File Extensions
https://cs50.harvard.edu/python/2022/psets/1/extensions/

.gif        image/gif
.jpeg, .jpg image/jpeg
.png        image/png
.pdf        application/pdf
.txt        text/plain
.zip        application/zip
"""

file = input("File name: ").strip().lower()
if file.endswith("gif") == 1:
    print("image/gif")
elif file.endswith("jpeg")  == 1 or file.endswith("jpg")  == 1:
    print("image/jpeg")
elif file.endswith("png") == 1:
    print("image/png")
elif file.endswith("pdf") == 1:
    print("application/pdf")
elif file.endswith("txt") == 1:
    print("text/plain")
elif file.endswith("zip") == 1:
    print("application/zip")
else:
    print("application/octet-stream")
