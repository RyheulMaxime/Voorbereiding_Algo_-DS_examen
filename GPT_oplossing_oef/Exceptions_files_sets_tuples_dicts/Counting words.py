def word_split(filename):
    words = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word = ""
            for ch in line:
                if ch.isalpha():
                    word += ch
                else:
                    if word:
                        words.append(word)
                        word = ""
            if word:  # end-of-line trailing word
                words.append(word)

    return words

def word_count(filename):
    counts = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word = ""
            for ch in line:
                if ch.isalpha():
                    word += ch
                else:
                    if word:
                        w = word.lower()
                        counts[w] = counts.get(w, 0) + 1
                        word = ""
            if word:  # trailing word
                w = word.lower()
                counts[w] = counts.get(w, 0) + 1

    return counts