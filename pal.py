from flask import Flask, render_template, request, jsonify
import requests
import html

app = Flask(__name__)
emoji = " "
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_fact', methods=['POST'])
def get_fact():
    genre = request.json.get('genre', 'any')

    if genre == "science":
        emoji = "🔬"
        url = "https://opentdb.com/api.php?amount=1&category=17&type=multiple"
    elif genre == "history":
        emoji = "📜"
        url = "https://opentdb.com/api.php?amount=1&category=23&type=multiple"
    elif genre == "geography":
        emoji = "🗺️"
        url = "https://opentdb.com/api.php?amount=1&category=22&type=multiple"
    elif genre == "IT":
        emoji = "💻"
        url = "https://opentdb.com/api.php?amount=1&category=18&type=multiple"
    elif genre == "arts":
        emoji = "🎨"
        url = "https://opentdb.com/api.php?amount=1&category=25&type=multiple"
    elif genre == "math":
        emoji = "📐"
        url = "http://numbersapi.com/random/math?json"
    elif genre == "sports":
        emoji = "🏅"
        url = "https://opentdb.com/api.php?amount=1&category=21&type=multiple"
    else:
        emoji = "🔍"
        url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        res = requests.get(url).json()
    except Exception:
        return jsonify({'fact': "Error fetching data from the API."})

    if "text" in res:
        fact = res['text']
    elif "fact" in res:
        fact = res['fact']
    elif "results" in res:
        fact = f"{html.unescape(res['results'][0]['question'])} Answer: {html.unescape(res['results'][0]['correct_answer'])}"
    else:
        fact = "Could not find a fact for the selected genre. Click the button once again."

    return jsonify({'fact': f"{emoji} {fact}"})

if __name__ == '__main__':
    app.run(debug=True)
