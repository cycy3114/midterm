from calc.commands.add import AddCommand

def test_add():
    assert AddCommand().execute(2, 3) == 5
