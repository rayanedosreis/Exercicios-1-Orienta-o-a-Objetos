from model.ContaBancaria import ContaBancaria

def principal():
    c1 = ContaBancaria("Kauan", 100.0)
    c2 = ContaBancaria("Rayane")

    try:
        c1.depositar(150.0)

        try:
            c1.sacar(500.0)
        except ValueError as erro:
            print(erro)

        c1.transferir(c2, 80.0)

    finally:
        c1.exibirExtrato()
        print(c2.getSaldo())


if __name__ == "__main__":
    principal()
