from flask import Flask, render_template
import analysis

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    results = analysis.run_analysis()
    print(results)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
