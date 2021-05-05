from django.shortcuts import render
# from django.http import HttpResponse
from .forms import CsvMOdelForm
from django.contrib.auth.models import User
from .models import Csv
import csv
from sales.models import Sale 

# Create your views here.

def upload_file_view(request):

    form= CsvMOdelForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvMOdelForm()
        obj = Csv.objects.get(actived=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row= "".join(row)
                    row=row.replace(";" , " ")
                    row= row.split()
                    product = row[1].upper()
                    user = User.objects.get(username=row[3])
                    Sale.objects.create(
                        product = product,
                        quantity = int(row[2]) ,
                        salesman = user,

                    )
                    # print(row)
                    # print(type(row))

                obj.activated = True
                obj.save()

    # return HttpResponse("drop a file here")
    return render(request, 'csvs/upload.html' , {"form": form}) 