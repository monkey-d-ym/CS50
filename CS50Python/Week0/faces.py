"""
Making Faces
https://cs50.harvard.edu/python/2022/psets/0/faces/
"""
def main():
    emoticon = input("Write some emoticons: ")
    emoji = convert(emoticon)
    print(emoji)
def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
main()
