from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(numero):
    # Calcula o fatorial de um número não negativo.
    if not isinstance(numero, int) or numero < 0:
        return None
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def calcular_fibonacci(numero):
    # Calcula o número na sequência de Fibonacci.
    if not isinstance(numero, int) or numero < 0:
        return None
    fib_sequence = [0, 1]
    while len(fib_sequence) <= numero:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[numero]

def validar_numero(data):
    # Função auxiliar para validar a presença e tipo do número no JSON.
    numero = data.get('numero')
    return numero if isinstance(numero, int) else None

@app.route('/fatorial', methods=['GET', 'POST'])
def calcular_fatorial_api():
    # Rota para calcular o fatorial de um número.
    data = request.get_json()

    numero = validar_numero(data)
    if numero is None:
        return jsonify({"erro": "Número não fornecido ou inválido"}), 400

    resultado = calcular_fatorial(numero)
    if resultado is None:
        return jsonify({"erro": "Número deve ser não negativo"}), 400

    return jsonify({"resultado_fatorial": resultado})

@app.route('/fibonacci', methods=['GET', 'POST'])
def calcular_fibonacci_api():
    # Rota para calcular o número na sequência de Fibonacci.
    data = request.get_json()

    numero = validar_numero(data)
    if numero is None:
        return jsonify({"erro": "Número não fornecido ou inválido"}), 400

    resultado = calcular_fibonacci(numero)
    if resultado is None:
        return jsonify({"erro": "Número deve ser não negativo"}), 400

    return jsonify({"resultado_fibonacci": resultado})

@app.route('/fatorial_fibonacci', methods=['GET', 'POST'])
def calcular_fatorial_fibonacci_api():
    # Rota para calcular tanto o fatorial quanto o número na sequência de Fibonacci.
    data = request.get_json()

    numero = validar_numero(data)
    if numero is None:
        return jsonify({"erro": "Número não fornecido ou inválido"}), 400

    resultado_fatorial = calcular_fatorial(numero)
    resultado_fibonacci = calcular_fibonacci(numero)

    if resultado_fatorial is None or resultado_fibonacci is None:
        return jsonify({"erro": "Número deve ser não negativo"}), 400

    return jsonify({"resultado_fatorial": resultado_fatorial, "resultado_fibonacci": resultado_fibonacci})

if __name__ == '__main__':
    app.run(debug=True)