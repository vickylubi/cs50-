import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern =r"<iframe.*src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})\""
    match = re.search(pattern, s)
    if match:
        return (f"https://youtu.be/{match.group(2)}" )
    

if __name__ == "__main__":
    main()