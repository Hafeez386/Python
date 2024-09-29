PLACEHOLDER = "[name]"
with open("my_file.txt", mode="w") as file:
    file.write("ali")
    file.write("\nalia")
    file.write("\naliaa")
    file.write("\nalain")
    file.write("\nalien")
    file.write("\nhafee")
    file.write("\nhafeez")
with open("starting_letters.txt ", mode= "w") as file:
    file.write(" dear [name] i wish you all the best")
#     file.write("\nI a 21 years old ")
#     file.write("\nI am a software engineer ")
# with open("my_file.txt", mode="a") as file:
#     file.write("\n nu tech")
# with open("/Users/hafee/OneDrive/Desktop/my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)
with open("my_file.txt", mode="r" ) as  name_file:
    names = name_file.readlines()
    print(names)
with open("starting_letters.txt", mode="r") as letter_file:
    letters_contents = letter_file.read()
    for name in names:
        new_letter = letters_contents.replace(PLACEHOLDER, name)
        print(new_letter)
