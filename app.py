from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_break_with
load_dotenv()

app = Flask(__name__) # create an app instance

@app.route('/') # at the end point /
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST']) # at the end point /
def process():
    name = request.form['name']
    summary, profile_pic_url = ice_break_with(name=name)
    # return render_template('summary.html', summary=summary, profile_pic_url=profile_pic_url)
    return jsonify({
        "summary": summary.to_dict(),
        "profile_pic_url": profile_pic_url
    })

if __name__ == '__main__': # on running python app.py

    app.run(debug=True, host="0.0.0.0") # run the flask app