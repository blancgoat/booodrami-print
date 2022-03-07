from django.shortcuts import render

from pdf.models import ExcelBoodrami

def index(request):
    excelBoodrami = ExcelBoodrami(request.FILES['excel'])
    
    context = {
        'excel': excelBoodrami.export(),
    }

    return render(request, 'pdf/index.html', context)

def withOption(request):
    excelBoodrami = ExcelBoodrami(request.FILES['excel'])
    
    context = {
        'excel': excelBoodrami.exportWithOption(),
    }

    return render(request, 'pdf/withOption.html', context)