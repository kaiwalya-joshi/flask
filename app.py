from flask import Flask, jsonify, request, render_template
import urllib.request
from PIL import Image
from flask_frozen import Freezer

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route('/get_url', methods=['POST'])
def get_url():
    # short_url = request.args.get('short_url')
    data = request.get_json()
    # url = 'https://' + short_url
    # urllib.request.urlretrieve(url, 'image.png')
    # img = Image.open('image.png')
    # cv2.imshow(url)
    url = data["image_url"]
    return url
    # return render_template('show_image.html', user_image = url)


if __name__ == '__main__':
   app.run(debug=True,port=5000)

