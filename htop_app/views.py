from django.shortcuts import render, HttpResponse
import os
import getpass as dt
from pytz import timezone 
from datetime import datetime
import subprocess

# Create your views here.
def index(request):
    name = 'Harshvir Singh'
    user_name = dt.getuser()
    

    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    os.system('top -bn 1 > tmp')

    with open('tmp', 'r') as f:
        top_output = "".join(line + "\n" for line in f)  # Ensuring newlines

    os.remove('tmp')

    formatted_output = top_output.replace("\r", "\n")
    # print(formatted_output)

    context = {'name': name, "user_name": user_name, 'time': ind_time, 'top_output': top_output}
    return render(request, 'index.html', context)