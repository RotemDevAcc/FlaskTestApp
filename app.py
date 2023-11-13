from flask import Flask, request, jsonify
from flask_cors import CORS
from my_numbers.comp import *
from my_numbers.simp import *
from tools.col import *

app = Flask(__name__)
app.secret_key = 'FASDEW443DFG'
CORS(app)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    number = data.get('number')
    number2 = data.get('number2')

    if not number or not number2 or not is_integer(number) or not is_integer(number2):
        return jsonify({"answer": "None", "message": "One or both of the arguments are missing or not integers"})

    ans = AddNumbers(number, number2)
    return jsonify({"answer": ans, "message": f"{number} + {number2} = {ans}"})

@app.route('/sub', methods=['POST'])
def sub():
    data = request.get_json()
    number = data.get('number')
    number2 = data.get('number2')

    if not number or not number2 or not is_integer(number) or not is_integer(number2):
        return jsonify({"answer": "None", "message": "One or both of the arguments are missing or not integers"})

    ans = SubNumbers(number, number2)
    return jsonify({"answer": ans, "message": f"{number} - {number2} = {ans}"})

@app.route('/sumofdigits', methods=['POST'])
def sumof():
    data = request.get_json()
    number = data.get('number')

    if not number or not is_integer(number):
        return jsonify({"answer": "None", "message": "The argument is missing or not an integer"})

    ans = sumofdigits(number)
    return jsonify({"answer": ans, "message": f"Sum Of Digits Of {number} = {ans}"})

@app.route('/ispal', methods=['POST'])
def pal():
    data = request.get_json()
    number = data.get('number')

    if not number or not is_integer(number):
        return jsonify({"answer": "None", "message": "The argument is missing or not an integer"})

    ans = ispal(number)
    ansmsg = "Not Palindrome"
    if ans:
        ansmsg = "Palindrome"

    return jsonify({"answer": ans, "message": ansmsg})

@app.route('/zipit', methods=['POST'])
def zip():
    data = request.get_json()
    table1 = data.get('table1')
    table2 = data.get('table2')
    if not table1 or not table2: return jsonify({"answer":"None", "message":"One of the arguments is missing"})
    ans = myzip(table1,table2)
    return jsonify({"answer":ans})

    


if __name__ == '__main__':
    app.run(debug=False)
