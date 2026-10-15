
# Combine the two Bill Clinton speech files

part1 = open("Bill Clinton - OKC bombing speech - Part 1.txt", "r")
part1_text = part1.read()
part1.close()

part2 = open("Bill Clinton - OKC bombing speech - Part 2.txt", "r")
part2_text = part2.read()
part2.close()

part3 = open("Bill Clinton - OKC bombing speech - Part 3.txt", "w")
part3.write(part1_text)
part3.write(part2_text)
part3.close()


# Write and print the important sentence

important_sentence = (
    "You have lost too much, but you have not lost everything. "
    "And you have certainly not lost America, for we will stand "
    "with you for as many tomorrows as it takes."
)

sentence_file = open("Important Sentence.txt", "w")
sentence_file.write(important_sentence)
sentence_file.close()

print(important_sentence)


# Count the lines in Part 3

line_count = 0

with open("Bill Clinton - OKC bombing speech - Part 3.txt", "r") as part3:
    for line in part3:
        line_count += 1

print("Number of lines in Part 3:", line_count)
