my_dict = {
    "Javascript": "an object-oriented computer programming language commonly used to create interactive effects within web browsers.",
    "Python": "an interpreted, object-oriented, high-level programming language with dynamic semantics.",
    "HTML": "a standardized system for tagging text files to achieve font, color, graphic, and hyperlink effects on World Wide Web pages.",
    "CSS": "describes how HTML elements are to be displayed on screen, paper, or in other media.",
    "C": "a high-level and general-purpose programming language that is ideal for developing firmware or portable applications."
}
#Answer 1
def key(val):
    for key, value in my_dict.items():
        if val == value:
            return key
    else:
        print("The key doesn't exist")

print(key("a standardized system for tagging text files to achieve font, color, graphic, and hyperlink effects on World Wide Web pages."), "=", my_dict["HTML"])
print(key("an interpreted, object-oriented, high-level programming language with dynamic semantics."), "=", my_dict["Python"])
print(key("describes how HTML elements are to be displayed on screen, paper, or in other media."), "=", my_dict["CSS"])
print(key("an object-oriented computer programming language commonly used to create interactive effects within web browsers."), "=", my_dict["Javascript"])
print(key("a high-level and general-purpose programming language that is ideal for developing firmware or portable applications."), "=", my_dict["C"])

print("\n========================================================================================================================================================\n")

#Answer 2
print([key for key in my_dict.keys()][2], "=", my_dict["HTML"])
print([key for key in my_dict.keys()][1], "=", my_dict["Python"])
print([key for key in my_dict.keys()][3], "=", my_dict["CSS"])
print([key for key in my_dict.keys()][0], "=", my_dict["Javascript"])
print([key for key in my_dict.keys()][4], "=", my_dict["C"])