from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales')
def sales():
    # Implement sales management logic here
    return render_template('sales.html')

@app.route('/inventory')
def inventory():
    # Implement inventory management logic here
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run(debug=True)
