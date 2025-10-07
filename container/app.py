from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    operand1 = request.args.get("operand1")
    operand1 = int(operand1) if operand1.isdigit() else 0

    operand2 = request.args.get("operand2")
    operand2 = int(operand2) if operand2.isdigit() else 0

    operation = request.args.get("operation")

    match operation:
        case "add":
            result = operand1 + operand2
            operation = "+"
        case "subtract":
            result = operand1 - operand2
            operation = "-"
        case "multiply":
            result = operand1 * operand2
            operation = "*"
        case "divide":
            if operand2 == 0:
                result = "На ноль делить нельзя"
            else:
                result = operand1 / operand2
            operation = "/"
        case "power":
            result = operand1**operand2
            operation = "^"
        case _:
            result = "Неверная операция"

    expression = f"{operand1} {operation} {operand2} = {result}"

    return f"""<!DOCTYPE html>
              <html>
              <head>
                <title>Результат</title>
              </head>
              <body>
                <h1>Результат</h1>
                <p>Выражение: { expression }</p>
              </body>
              </html>"""


@app.route("/")
def root():
    return """<!DOCTYPE html>
              <html>
              <head>
                <title>Калькулятор</title>
              </head>
              <body>
                <h1>Калькулятор</h1>
                <form method="get" action="/calc"> 
                  <label>Первое число:</label>
                  <input type="text" name="operand1"><br><br>

                  <label>Операция:</label>
                  <select name="operation">
                    <option value="add">Сумма</option>
                    <option value="subtract">Разность</option>
                    <option value="multiply">Произведение</option>
                    <option value="divide">Деление</option>
                    <option value="power">Степень</option>
                  </select><br><br>

                  <label>Второе число:</label>
                  <input type="text" name="operand2"><br><br>

                  <input type="submit" value="Отправить">
                </form>
              </body>
              </html>"""


if __name__ == "__main__":
    app.run(debug=True)
