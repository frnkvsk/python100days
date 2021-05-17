import random

# names = ['Alex', 'Beth', 'Carol', 'Dave', 'Kim', 'Sam', 'Heather', 'Hank']
# students_scores = {student:random.randint(1, 100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score > 59}
# print(students_scores)
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladden Swallow?"
# result = {word:len(word) for word in sentence.split(' ')}
# print(result)

# weather_c = {
#     'Monday': 12,
#     'Tuesday': 14,
#     'Wednesday': 15,
#     'Thursday': 14,
#     'Friday': 21,
#     'Saturday': 22,
#     'Sunday': 24
# }
# weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# import pandas
#
# student_dict = {
#     'student': ['Mary', 'Andy', 'Peter'],
#     'score': [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (index, row) in student_data_frame.iterrows():
#     if row.student == 'Mary':
#         print(row.score)
import pandas

letter_dict = {r.letter:r.code for (i, r) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}


def generate_phonetic():
    in_word = input('Enter a word ').upper()
    try:
        phonetic_list = [letter_dict[letter] for letter in list(in_word.strip())]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()