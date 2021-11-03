my_dict = {
    "Javascript": "an object-oriented computer programming language commonly used to create interactive effects within web browsers.",
    "Python": "an interpreted, object-oriented, high-level programming language with dynamic semantics.",
    "HTML": "a standardized system for tagging text files to achieve font, color, graphic, and hyperlink effects on World Wide Web pages.",
    "CSS": "describes how HTML elements are to be displayed on screen, paper, or in other media",
    "C": "a high-level and general-purpose programming language that is ideal for developing firmware or portable applications."
}

print([key for key in my_dict.keys()][2], "=", [value for value in my_dict.values()][2])
print([key for key in my_dict.keys()][1], "=", [value for value in my_dict.values()][1])
print([key for key in my_dict.keys()][3], "=", [value for value in my_dict.values()][3])
print([key for key in my_dict.keys()][0], "=", [value for value in my_dict.values()][0])
print([key for key in my_dict.keys()][4], "=", [value for value in my_dict.values()][4])