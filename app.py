from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.errorhandler(404)
def pag_not_found(error):
    return render_template('error404.html', error=error), 404

@app.route('/numeros/<int:numeros>')
def numeros(numeros):
    num = str(numeros)
    num = ''.join(sorted(num))
    result = int(num)
    return jsonify(f'Numeros ordenados de menor a mayor: {result}')

@app.route('/libro/<libro>')
def libro(libro):
    try:
        with open(f'{libro}.txt', 'r', encoding='utf-8') as libro_file:
            data = libro_file.read()
        counter = 0
        for i in data:
            if i.isupper():
                counter += 1
        return jsonify(f'Cantidad de letras mayusculas: {counter}')
    except FileNotFoundError:
        message = f'Libro "{libro}" no fue encontrado.'
        return(message)

@app.route('/adicional', methods=['POST', 'GET'])
def otro():
    if request.method == 'POST':
        body = request.get_json()
        numer = body.get('numer')
        return jsonify(F'Mi edad es: {numer}')

    if request.method == 'GET':
        return jsonify('Aprendiendo aun de metodos HTTP')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello_world.html', name=name)
