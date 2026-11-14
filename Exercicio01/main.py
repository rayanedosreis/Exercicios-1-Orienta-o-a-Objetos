from model.Funcionario import Funcionario


def principal():
    f1 = Funcionario("Rayane", 3000.0, 500.0, 200.0)
    f2 = Funcionario("Claudio", 2000.0, 1000.0, 550.0)

    print(f1.calcularSalarioLiquido())

    f1.setSalarioBruto(3500.0)
    print(f1.calcularSalarioLiquido())

    try:
        f1.setSalarioBruto(-1000.0)
    except ValueError as erro:
        print(erro)

    print(f2.calcularSalarioLiquido())

    f2.nome = "Outro"
    print(f2.getNome())


if __name__ == "__main__":
    principal()
