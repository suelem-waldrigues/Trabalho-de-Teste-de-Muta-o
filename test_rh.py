from rh import calcular_bonus

def test_bonus_valido():
    assert calcular_bonus(5000, 5, "DESENVOLVEDOR") == 750

def test_funcionario_sem_tempo():
    assert calcular_bonus(5000, 2, "DESENVOLVEDOR") == 0

def test_cargo_diferente():
    assert calcular_bonus(5000, 5, "GERENTE") == 0