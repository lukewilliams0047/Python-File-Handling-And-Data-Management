
# Question 2 Part A
# Open Black Astronauts Part 1

part1 = open("Black Astronauts (partial)- Part 1.txt", "r")
part1_text = part1.read()
part1.close()

# Open Black Astronauts Part 2
part2 = open("Black Astronauts (partial)- Part 2.txt", "r")
part2_text = part2.read()
part2.close()

# Open Black Astronauts Part 3
part3 = open("Black Astronauts (partial)- Part 3.txt", "r")
part3_text = part3.read()
part3.close()

# Create Black Astronauts Part 4
part4 = open("Black Astronauts Part 4.txt", "w")

# Write all three files into Part 4
part4.write(part1_text)
part4.write(part2_text)
part4.write(part3_text)

# Close Part 4
part4.close()


# Question 2 Part B
# Read and print all names in Part 4

part4 = open("Black Astronauts Part 4.txt", "r")
names = part4.readlines()
part4.close()

for name in names:
    print(name.strip())

# Remove Leland Melvin and save the remaining names in Part 5
part5 = open("Black Astronauts Part 5.txt", "w")

for name in names:
    if "Leland Melvin" not in name:
        part5.write(name)

part5.close()


# Question 2 Part C
import os

# Remove Black Astronauts Part 1
os.remove("Black Astronauts (partial)- Part 1.txt")

# Rename Black Astronauts Part 2 to Part B
os.rename(
    "Black Astronauts (partial)- Part 2.txt",
    "Black Astronauts Part B.txt"
)

# Print all Black Astronauts files
for filename in os.listdir():
    if filename.startswith("Black Astronauts"):
        print(filename)
