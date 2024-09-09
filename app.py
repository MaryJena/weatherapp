from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    data = response.json()
    
    # Pass the data to the template
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)