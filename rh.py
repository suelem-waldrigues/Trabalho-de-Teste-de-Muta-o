def calcular_bonus(salario, anos_empresa, cargo):
    if anos_empresa > 2 and cargo == "DESENVOLVEDOR":
        return salario * 0.15
    return 0