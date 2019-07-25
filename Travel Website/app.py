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

@app.route('/1a')
def Affordability_Beach():
	return render_template('1a.html')

@app.route('/1b')
def Affordability_Nature():
	return render_template('1b.html')

@app.route('/1c')
def Affordability_Snow():
	return render_template('1c.html')

@app.route('/1d')
def Affordability_Nightlife():
	return render_template('1d.html')

@app.route('/1e')
def Affordability_Culture():
	return render_template('1e.html')

@app.route('/2a')
def Luxury_Beach():
	return render_template('2a.html')

@app.route('/2b')
def Luxury_Nature():
	return render_template('2b.html')

@app.route('/2c')
def Luxury_Snow():
	return render_template('2c.html')

@app.route('/2d')
def Luxury_Nightlife():
	return render_template('2d.html')

@app.route('/2e')
def Luxury_Culture():
	return render_template('2e.html')

if __name__ == '__main__':
	app.run(debug=True)