import os
import pandas as pd
from calc.history import HistoryManager

def test_add_and_show_record(tmp_path):
    file = tmp_path / "history.csv"
    history = HistoryManager(file=str(file))
    
    history.add_record("add 2 3", 5)
    df = pd.read_csv(file)

    assert not df.empty
    assert df.iloc[0]["operation"] == "add 2 3"
    assert df.iloc[0]["result"] == 5

def test_clear_history(tmp_path):
    file = tmp_path / "history.csv"
    history = HistoryManager(file=str(file))
    history.add_record("add 1 1", 2)
    history.clear_history()
    
    df = pd.read_csv(file)
    assert df.empty
