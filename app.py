from flask import Flask,render_template,request
import requests,time
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def get_value():
    url = request.form['url']
    print(url)
    r = requests.post(
    "https://api.deepai.org/api/colorizer",
    data= {
        'image': {url},
    },
    headers={'api-key': 'api'}
    )
    print("reached")
    
    time.sleep(10)
    data = r.json()
    print(data)
    print(data['output_url'])   
    return render_template('io.html',org=url,data=data['output_url'])


if __name__ == '__main__':
    app.run()