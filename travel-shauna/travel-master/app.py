from flask import Flask, url_for, render_template, jsonify, request
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

@app.route('/furtherinformation')
def furtherinformation():
	return render_template('furtherinformation.html')

with app.test_request_context():
    print(url_for('index'))

# What actually runs the app
app.run()

#
# if __name__ == '__main__':
# 	app.run(debug=True)
