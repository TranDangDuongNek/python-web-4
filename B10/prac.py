import string

# đếm số lần từ xuất hiện trong 1 đoạn văn bản
def count_words(paragraph) -> None:
    # thay đổi thành chữ thường
    paragraph = paragraph.lower()

    # loại dấu câu
    for char in string.punctuation:
        paragraph = paragraph.replace(char, '')

    # tách từ
    words = paragraph.split()

    # đếm tần suất
    word_count = {}  # dict
    for word in words:
        if word in word_count:
            word_count[word] += 1  # cộng 1 lần đếm
        else:
            word_count[word] = 1  # đếm 1 lần

    return word_count

    
result = count_words(paragraph=p)

# hiển thị danh sách theo thứ tự chữ cái
max = 0
word_count_max = ""

for word, counter in sorted(result.items()):
    print(f"{word}: {counter}")
    if counter > max:
        max = counter
        word_count_max = word

print(f"Từ với số lần lặp cao nhất: {word_count_max}, lặp {max} lần")
