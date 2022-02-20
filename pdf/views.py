from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from pdf.models import ExcelBoodrami

def index(request):
    template = loader.get_template('pdf/index.html')
    excelBoodrami = ExcelBoodrami()
    for row in excelBoodrami.df.itertuples():
        excelBoodrami.df.at[row.Index, '우편번호'] = str(row.우편번호).zfill(5)
        excelBoodrami.df.at[row.Index, '고유번호'] = str(row.Index + 1)
    
    context = {
        'excel': excelBoodrami.df.itertuples(),
    }
    return HttpResponse(template.render(context, request))