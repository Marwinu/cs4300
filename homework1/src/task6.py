
# reads a text file and counts the words in them
def count_words(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()  # split on whitespace
    return len(words)

if __name__ == "__main__":
    path = "src/task6_read_me.txt"
    total_words = count_words(path)
    print(f"Total words in file: {total_words}")