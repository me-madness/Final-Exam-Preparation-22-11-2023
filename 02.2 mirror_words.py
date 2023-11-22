# First task from the lecture

import re

data = input()
pattern = r"(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
result = re.findall(pattern, data)      #Wen use findall, we get a tuple, not a list.
mirror_words = []
the_count_of_mirror_words = len(result)

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f"{pair[1]} <=> {pair[3]}")

if the_count_of_mirror_words > 0:
    print(f"{the_count_of_mirror_words} word pairs found")
    if not mirror_words:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_words))
else:
    print("No word pairs found!")
    print("No mirror words!")

# Second task is from me

