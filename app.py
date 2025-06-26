from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>My Cloud Journey Dashboard</h1><p>Week 1: EC2 Deployment Success!</p><p>Tester paragraph.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
