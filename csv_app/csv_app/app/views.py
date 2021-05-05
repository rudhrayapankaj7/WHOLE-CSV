import csv

from django.http import HttpResponse
from django.shortcuts import render
from app.models import Employee

#     name = models.CharField(max_length=100)
#     salary = models.IntegerField()
#     company = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     DOJ = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

def home(request):
    return render(request, template_name="home.html")

# 
def csv_export(request):
    all_active_data = Employee.objects.filter(active=True)
    # print(all_active_data)
    # return HttpResponse(all_active_data)
    response = HttpResponse(content_type='text/csv')
    csv_writer = csv.writer(response)
    csv_writer.writerow(["ID", "Name", "Salary", "Company","Designation", "DOJ", "Active"])

    for emp in all_active_data.values_list('id', 'name', 'salary', 'company', 'designation', 'DOJ', 'active'):
        # print(type(emp))
        csv_writer.writerow(emp)

    response['Content-Disposition'] = 'attachement; filename="employee_data.csv" '
    return response


# video -- 7 - 8.30  ---- 45 minutes  ---  

from django.http import HttpResponseRedirect
def upload_csv(request):
	data = {}
	if request.method == "GET":
		return render(request, "upload.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			return HttpResponseRedirect(reverse("upload_csv"))

		file_data = csv_file.read().decode("utf-8")		
        print(file_data)
		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		# for line in lines:						
		# 	fields = line.split(",")
		# 	data_dict = {}
		# 	data_dict["name"] = fields[0]
		# 	data_dict["start_date_time"] = fields[1]
		# 	data_dict["end_date_time"] = fields[2]
		# 	data_dict["notes"] = fields[3]
		# 	try:

		# 		else:
		# 			print("Error")
		# 	except Exception as e:
		# 		print(e)
		# 		pass

	except Exception as e:
		print(e)

	return HttpResponseRedirect(reverse("upload_csv"))