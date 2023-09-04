"""
Watch on YouTube
https://cs50.harvard.edu/python/2022/psets/7/watch/
"""
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r'^<iframe(?: width="560" height="315")? src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)"(?: title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>$', s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"

if __name__ == "__main__":
    main()
