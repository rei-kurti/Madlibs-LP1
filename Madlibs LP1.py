# This algorithm will allow user to input words in order to fill the blanks of a paragraph
# The paragraph can be as long as we need and it can contain as many blanks as needed

prog_lang = input("What language is this project: ")
other_work = input("What work have you done in school: ")
bachelor_degree = input("What did you study for: ")

paragraph = f"This is my first project in {prog_lang} without counting the {other_work} that I've done during my studies for {bachelor_degree}."

print(paragraph)