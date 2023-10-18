from flask import Flask, request, render_template
from gene_info import get_gene_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    gene_info = get_gene_info(query)
    return render_template('result.html', gene_info=gene_info)

if __name__ == '__main__':
    app.run(debug=True)