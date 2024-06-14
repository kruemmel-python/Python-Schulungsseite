from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_random_question():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    c.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
    question_data = c.fetchone()

    if not question_data:
        return None

    question_id, question_text = question_data

    c.execute("SELECT * FROM answers WHERE question_id=?", (question_id,))
    answers_data = c.fetchall()

    answers = [{'id': a[0], 'answer': a[2], 'is_correct': a[3], 'explanation': a[4]} for a in answers_data]

    conn.close()
    return {'id': question_id, 'question': question_text, 'answers': answers}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/grundlagen')
def grundlagen():
    return render_template('grundlagen.html')

@app.route('/grundlagen/<topic>')
def grundlagen_topic(topic):
    return render_template(f'grundlagen/{topic}.html')

@app.route('/konzepte')
def konzepte():
    return render_template('konzepte.html')

@app.route('/konzepte/<topic>')
def konzepte_topic(topic):
    return render_template(f'konzepte/{topic}.html')

@app.route('/wiki')
def wiki():
    return render_template('wiki.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/bibliotheken')
def bibliotheken():
    return render_template('bibliotheken.html')

@app.route('/bibliotheken/<library>')
def bibliotheken_library(library):
    return render_template(f'bibliotheken/{library}.html')

@app.route('/quiz')
def quiz():
    question = get_random_question()
    return render_template('quiz.html', question=question, is_correct=None, explanations=[])

@app.route('/quiz/<int:question_id>', methods=['POST'])
def next_question(question_id):
    submitted_answers = request.form.getlist(f'question{question_id}')
    correct_answers = []
    explanations = []

    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    c.execute("SELECT * FROM answers WHERE question_id=? AND is_correct=1", (question_id,))
    correct_answers_data = c.fetchall()

    for answer in correct_answers_data:
        correct_answers.append(str(answer[0]))
        explanations.append({'answer': answer[2], 'explanation': answer[4]})

    # Check if all correct answers are selected and no incorrect answers are selected
    is_correct = all(a in submitted_answers for a in correct_answers) and all(a in correct_answers for a in submitted_answers)

    if is_correct:
        question = get_random_question()
        return render_template('quiz.html', question=question, is_correct=True, explanations=[])
    else:
        return render_template('quiz.html', question=get_random_question(), is_correct=False, explanations=explanations)

if __name__ == '__main__':
    app.run(debug=True)
