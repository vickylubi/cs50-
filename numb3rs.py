import re
import sys

#Ask for user input 
def main():
    print(validate(input("IPv4 Address: ")))

#Search for the pattern #.#.#.#. Each # should be a number between 0 and 255
def validate(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match = re.search(pattern, ip)
    if match:
        parts = ip.split(".")
        for part in parts:
            if not (0 <= int(part) <= 255):
                return False
            if len(part) > 1 and part.startswith("0"):
                return False
        return True
    else: 
        return False


if __name__ == "__main__":
    main()