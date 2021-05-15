from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

correct_answers = []
data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
x_list = data['x'].to_list()
y_list = data['y'].to_list()
data_dict = {}
for i in range(len(states_list)):
    data_dict[states_list[i].lower()] = {
        'x': x_list[i],
        'y': y_list[i]
    }

while len(correct_answers) < len(data):
    answer_state = screen.textinput(title=f'Guess the State {len(correct_answers)}/50', prompt="What's another state's name?")
    stripped_answer_state = answer_state.strip().lower()
    if stripped_answer_state in data_dict and stripped_answer_state not in correct_answers:
        correct_answers.append(stripped_answer_state)
        x = data_dict[stripped_answer_state]['x']
        y = data_dict[stripped_answer_state]['y']
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.color('red')
        t.write(stripped_answer_state.capitalize(), False, 'left', ('Arial', 10, 'bold'))
    if answer_state == 'e':
        break

print(f"You answered {len(correct_answers)} out of 50 correctly.")
print("Your correct answers:")
for name in correct_answers:
    print('\t',name)

missed_states = [state for state in states_list if state not in correct_answers]
df = pandas.DataFrame(missed_states)
df.to_csv('missed_states.csv')