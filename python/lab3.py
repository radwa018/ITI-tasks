#1
def read_file_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

print(read_file_lines("python/test.txt"))

#2
def write_list_to_file(filename):
    words = ["Python", "Programming", "Lab"]
    words.append("Radwa")  
    with open(filename, "w") as f:
        for item in words:
            f.write(item + "\n")
write_list_to_file("python/output.txt")

