from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/inspiration')
def inspiration():
	return render_template('inspiration.html')

@app.route('/more')
def more():
	return render_template('more.html')

if __name__ == '__main__':
	app.run(debug=True)
