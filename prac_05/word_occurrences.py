# words = "this is a collection of words of nice words this is a fun thing it is".split()
words = input("Text: ").split()
words.sort()
word_to_count_dict = {}
for word in words:
    if word in word_to_count_dict:
        word_to_count_dict[word] += 1
    else:
        word_to_count_dict[word] = 1

word_size_dict = {}
for word in words:
    word_size_dict[f"{word}"] = len(word)
# print(word_size_dict)

for word in word_to_count_dict:
    print(f"{word:{max(word_size_dict.values())}} : {word_to_count_dict[word]}")
