from logo import calc

print(calc)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

values = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

historys = {}


previous_result = None

while True:
    try:
        if previous_result is not None:
            num = input("Deseja utilizar o valor anterior? y/n: ")

            if num == "y":
                first_num = previous_result
            else:
                first_num = float(input("Digite o primeiro numero: "))
        else:
            first_num = float(input("Digite o primeiro numero: "))

        for value in values:
            print(value)

        sinal = input("Qual sinal da conta: ")

        if sinal not in values:
            print("Sinal inválido")
            continue

        second_num = float(input("Digite o segundo numero: "))

        if sinal == "/" and second_num == 0:
            print("Undefined")
            continue

        result = values[sinal](first_num, second_num)

        operacao = f"{first_num} {sinal} {second_num} ="
        historys[operacao] = result

        print(operacao, result)

        previous_result = result

        leave = input("Deseja sair da calculadora e ver seu historico? y/n\n")

        if leave == "y":
            print("\nHistorico:\n")

            for number, history in enumerate(historys, start=1):
                print(f"{number} - {history} {historys[history]}")

            break

    except ValueError:
        print("Um valor numérico inválido foi digitado")

    except KeyError:
        print("Sinal inválido")