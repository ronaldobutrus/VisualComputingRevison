import numpy as np
import os
from datetime import datetime
import time

class QuestionAnswer:
    def __init__(self, id, question, answer, chapter):
        self.id = id
        self.question = question
        self.answer = answer
        self.chapter = chapter

def WriteQuestionsToFile(path, title, questions, display_a = True):
    file = open(path, "w")
    file.write("# " + title + "\n")
    for i in range(len(questions)):
        file.write(f"### Question {i+1}\n{questions[i].question}\n")
        if display_a:
            file.write(f"#### Answer {i+1}:\n{questions[i].answer}\n")
        file.write(f"#### *[This question was from {questions[i].chapter}]*\n<hr>\n\n")
    file.close()

NUMBER_OF_QUESTIONS_PER_SET = 20
NUMBER_OF_SETS = 13
GENERATE_ALL = False
REPLACEMENT_ENABLED = False
QUESTIONS_WITH_ANSWERS = True
CHAPTERS = ["5", "6"]
FILTER_CHAPTERS = False

source_file = open("source.md", "r")
source_lines = [r'' + line.rstrip('\n') for line in source_file]
source_file.close()
source_lines.append("### Question")

all_questions = []

current_chapter = ""
current_question = ""
current_answer = ""
count = 0
is_question = False
current_chapter_enabled = True

for line in source_lines:
    if line.startswith("# "):
        current_chapter = line[2:]
        current_chapter_enabled = False or not FILTER_CHAPTERS
        for c in CHAPTERS:
            if current_chapter.startswith(c):
                current_chapter_enabled = True
    elif line.startswith("### Question"):
        is_question = not is_question
        if current_answer != "":
            if current_chapter_enabled:
                all_questions.append(QuestionAnswer(count, current_question, current_answer, current_chapter))
            count += 1
            current_answer = ""
            current_question = ""
    elif line.startswith("### Answer"):
        is_question = not is_question
    else:
        if is_question:
            current_question += line + "\n"
        else:
            current_answer += line + "\n"

datetime_object = datetime.utcfromtimestamp(time.time())
timestamp_string = datetime_object.strftime('%Y%m%d%H%M%S')
os.makedirs(timestamp_string, exist_ok=True)
file_path = os.path.join(timestamp_string, 'All Questions - Fundamentals of Visual Computing.md')

if GENERATE_ALL:
    if QUESTIONS_WITH_ANSWERS:
        file_path = os.path.join(timestamp_string, f"Fundamentals of Visual Computing.md")
        WriteQuestionsToFile(file_path, f"Fundamentals of Visual Computing", all_questions)
    else:
        file_path_q = os.path.join(timestamp_string, f"Questions - Fundamentals of Visual Computing.md")
        WriteQuestionsToFile(file_path_q, f"Questions - Fundamentals of Visual Computing", all_questions, False)
        file_path_a = os.path.join(timestamp_string, f"Answers - Fundamentals of Visual Computing.md")
        WriteQuestionsToFile(file_path_a, f"Answers - Fundamentals of Visual Computing", all_questions, True)
else:
    if REPLACEMENT_ENABLED or NUMBER_OF_QUESTIONS_PER_SET * NUMBER_OF_SETS <= len(all_questions):
        for i in range(1, NUMBER_OF_SETS + 1):
            questions = np.random.choice(all_questions, size=NUMBER_OF_QUESTIONS_PER_SET, replace=False)
            if not REPLACEMENT_ENABLED:
                for q in questions:
                    all_questions.remove(q)
            if QUESTIONS_WITH_ANSWERS:
                file_path = os.path.join(timestamp_string, f"Question Set {i} - Fundamentals of Visual Computing.md")
                WriteQuestionsToFile(file_path, f"Question Set {i} - Fundamentals of Visual Computing", questions)
            else:
                file_path_q = os.path.join(timestamp_string, f"Question Set {i} - Fundamentals of Visual Computing.md")
                WriteQuestionsToFile(file_path_q, f"Question Set {i} - Fundamentals of Visual Computing", questions, False)
                file_path_a = os.path.join(timestamp_string, f"Answer Set {i} - Fundamentals of Visual Computing.md")
                WriteQuestionsToFile(file_path_a, f"Answer Set {i} - Fundamentals of Visual Computing", questions, True)