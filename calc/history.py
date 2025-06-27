import pandas as pd
import os

class HistoryManager:
    def __init__(self, file="history.csv"):
        self.file = file
        self.df = pd.read_csv(self.file) if os.path.exists(self.file) else pd.DataFrame(columns=["operation", "result"])

    def add_record(self, op, res):
        new_record = pd.DataFrame([{"operation": op, "result": res}])
        self.df = pd.concat([self.df, new_record], ignore_index=True)
        self.df.to_csv(self.file, index=False)

    def show_history(self):
        print(self.df)

    def clear_history(self):
        self.df = pd.DataFrame(columns=["operation", "result"])
        self.df.to_csv(self.file, index=False)
