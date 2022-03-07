from django.db import models
import pandas as pd

# Create your models here.
class ExcelBoodrami():
    def __init__(self, importFile):
        self.data = pd.read_excel(importFile.read(), engine = "openpyxl")
    
    def export(self):
        dataFrame = pd.DataFrame(self.data, columns = [
            "수취인명",
            "배송지",
            "수취인연락처1",
            "우편번호",
            "배송메세지",
            "수량"])
        
        for row in dataFrame.itertuples():
            dataFrame.at[row.Index, '우편번호'] = str(row.우편번호).zfill(5)
            dataFrame.at[row.Index, '고유번호'] = str(row.Index + 1)

        return dataFrame.itertuples()

    def exportWithOption(self):
        dataFrame = pd.DataFrame(self.data, columns = [
            "상품주문번호",
            "주문번호",
            "수취인명",
            "배송지",
            "수취인연락처1",
            "우편번호",
            "배송메세지",
            "수량",
            "옵션정보"])

        duplicatedDataFrame = dataFrame.drop_duplicates(subset=['주문번호'])
        index = 1
        for row in duplicatedDataFrame.itertuples():
            pink = dataFrame.query(f"주문번호 == {row.주문번호} and 옵션정보 == '컬러: 분홍'")
            sky = dataFrame.query(f"주문번호 == {row.주문번호} and 옵션정보 == '컬러: 하늘'")
            duplicatedDataFrame.at[row.Index, '옵션수량'] = f"분홍: {pink.수량.values} 하늘: {sky.수량.values}"
            duplicatedDataFrame.at[row.Index, '우편번호'] = str(row.우편번호).zfill(5)
            duplicatedDataFrame.at[row.Index, '고유번호'] = str(index)
            index += 1

        return duplicatedDataFrame.itertuples()