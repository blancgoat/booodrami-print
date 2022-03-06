from django.db import models
import pandas as pd

# Create your models here.
class ExcelBoodrami():
    def __init__(self, importFile):
        self.df = self.excelLoad(importFile)

    def excelLoad(self, importFile):
        data = pd.read_excel(importFile.read(), engine = "openpyxl")

        df = pd.DataFrame(data, columns = [
            "수취인명",
            "배송지",
            "수취인연락처1",
            "우편번호",
            "배송메세지",
            "수량"])

        return df
    
    def export(self):
        for row in self.df.itertuples():
            self.df.at[row.Index, '우편번호'] = str(row.우편번호).zfill(5)
            self.df.at[row.Index, '고유번호'] = str(row.Index + 1)

        return self.df.itertuples()