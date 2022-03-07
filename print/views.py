from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
import mimetypes

from pdf.models import ExcelBoodrami

import os
import datetime

def index(request):
    excelBoodrami = ExcelBoodrami(request.FILES['excel'])
    
    context = {
        'excel': excelBoodrami.export(),
    }

    template = loader.get_template('pdf/index.html')

    return __fileExport(template, context, request)

def withOption(request):
    excelBoodrami = ExcelBoodrami(request.FILES['excel'])
    
    context = {
        'excel': excelBoodrami.exportWithOption(),
    }

    template = loader.get_template('pdf/withOption.html')

    return __fileExport(template, context, request)

def __fileExport(template, context, request) :
    htmlString = template.render(context, request)
    with open('pdfToHtml.html', 'w') as html_file:
        html_file.write(htmlString)

    file_path = str(datetime.datetime.now().strftime("%Y%m%d%I%m%S")) + "booodrami.pdf"
    cwd = os.getcwd()
    os.system("wkhtmltopdf --page-width 150mm --page-height 100mm ${cwd}pdfToHtml.html " + file_path)
    
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(),content_type=mimetypes.guess_type(file_path)[0])
        response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % file_path
        response['fileName'] = file_path

    return response
    