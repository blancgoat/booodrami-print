from django.db import models
import pandas as pd

# Create your models here.
class ExcelBoodrami():
    def __init__(self):
        self.df = self.excelLoad()

    def excelLoad(self):
        data = pd.read_excel("./booodrami.xlsx", engine = "openpyxl")

        df = pd.DataFrame(data, columns = [
            "수취인명",
            "배송지",
            "수취인연락처1",
            "우편번호",
            "배송메세지",
            "수량"])

        return df