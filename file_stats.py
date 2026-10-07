filename = "servers.txt"
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print(f"number of lines: {len(lines)}")
        for line in lines:
            words = line.split()
            print(f"number of words: {len(words)}")
            characters = line.strip()
            print(f"number of characters: {len(characters)}")
        max_line = max(lines, key=len)
        print(max_line.strip())
finally:
    print("finally executed")
