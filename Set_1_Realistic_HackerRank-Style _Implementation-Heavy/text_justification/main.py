'''
🧩 Text Justification
Given a list of words, left justify them. See the test case as an example

🔒 Constraints
text
Copy
Edit
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] contains only lowercase English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''
'''
MY ATTEMPT:

def text_justification(words, max_width):
    justified_text = []
#--------------------------------------------------------------
    words_j = " ".join(words)

    words_l = words_j[0:max_width].split(" ")

    if words_l[-1] < words[-1]:
        words_l.pop(-1)

    #print(words_l)

    on_join = " "

    words_j2 = on_join.join(words_l)
    #print(words_j2)

    while len(words_j2) < max_width:
        on_join += " "

        words_j2 = on_join.join(words_l)

    #print(words_j2)
    justified_text.append(words_j2)

    #------------------------------------------------------------------

    words_j = " ".join(words)

    print(words_j)

    words_l = words_j[max_width:max_width + max_width].split(" ")

    print(words_l)

    if len(words_l[-1]) < len(words[-1]):
        words_l.pop(-1)

    if len(words_l[0]) < len(words[3]):
        words_l.pop(0)
        words_l.insert(0, words[3])

    on_join = " "

    words_j2 = on_join.join(words_l)
        # print(words_j2)

    while len(words_j2) < max_width:
        on_join += " "

        words_j2 = on_join.join(words_l)

        # print(words_j2)
    justified_text.append(words_j2)

    print(words_l)

    return justified_text
'''

def text_justification(words, max_width):
    res = []
    i = 0

    while i < len(words):
        # Step 1: Figure out how many words fit in the current line
        line_len = len(words[i])
        j = i + 1
        while j < len(words) and line_len + 1 + len(words[j]) <= max_width:
            line_len += 1 + len(words[j])
            j += 1

        # Step 2: Get the words for this line
        line_words = words[i:j]
        num_words = j - i
        num_spaces = max_width - sum(len(word) for word in line_words)

        # Step 3: Format line
        if j == len(words) or num_words == 1:
            # Last line or single word: left-justify
            line = ' '.join(line_words)
            line += ' ' * (max_width - len(line))
        else:
            # Fully justify
            space_slots = num_words - 1
            even_space = num_spaces // space_slots
            extra = num_spaces % space_slots

            line = ""
            for k in range(space_slots):
                line += line_words[k]
                line += ' ' * (even_space + (1 if k < extra else 0))
            line += line_words[-1]  # Add the last word (no trailing space)

        res.append(line)
        i = j

    return res


print(text_justification(["This", "is", "an", "example", "of", "text", "justification."], 16))