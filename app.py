from flask import Flask, render_template
from graph import legend2M, legend1M, legend0M,labels, values2M, values1M, values0M

app = Flask(__name__)

@app.route("/")
def chart():
    return render_template('index.html', labels=labels,
    values2M=values2M, values1M=values1M, values0M=values0M,
    legend2M=legend2M, legend1M=legend1M, legend0M=legend0M)

if __name__ == "__main__":
    app.run(debug=True)