from flask import Flask, render_template
import random

def secret_santa(people, people2):
    # person =
    # if person != 'Jason':
    #     print('Access denied')
    # else:
    #     print('Welcome, Jason! Here are the Secret Santa assignments:')
    assignments = []
    for x in people:
        y = random.choice(people2)
        assignment = [x, y]
        while x == y or assignment == ['Jeremiah', 'Anika'] or assignment == ['Jeremiah', 'Anika']:
            y = random.choice(people2)
            assignment = [x, y]
        assignments.append(assignment)
        people2.remove(y)
    for item in assignments:
        print(item[0], 'has', item[1])

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def root():
    return render_template('base.html')

@app.route('/calculate', methods = ['GET', 'POST'])
def calculate(message = ''):
    giver = ['Jeremiah', 'Anika', 'Trevor', 'Ashley', 'Allie']
    receiver = ['Jeremiah', 'Anika', 'Trevor', 'Ashley', 'Allie']
    message = secret_santa(giver, receiver)
    return render_template('calculate.html', message = message)

if __name__ == '__main__':
    app.run()
