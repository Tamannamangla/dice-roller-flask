from flask import Flask, render_template, request, flash,redirect, url_for, session,jsonify
import random

app = Flask(__name__)
app.secret_key = 'dicegame123'  # Session ke liye chahiye hota hai

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll')
def roll_dice():
    dice_value = random.randint(1,6)
    flash(f'🎲 You rolled a {dice_value}!')
    return jsonify({'value':dice_value})

@app.route('/roll-page', methods=['GET', 'POST'])
def roll_page():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        dice = random.randint(1, 6)
        session['history'].append(dice)
        session.modified = True
        flash(f'🎲 You rolled a {dice}!')
    dice_value = session['history'][-1] if session['history'] else None
    total_score = sum(session['history'])

    return render_template('roll_page.html', result=dice_value, history=session['history'], total=total_score)

@app.route('/new-game')
def new_game():
    session.pop('history', None)
    flash("🔁 New game started!")
    return redirect('/roll-page')


if __name__ == "__main__":
    app.run(debug=True)