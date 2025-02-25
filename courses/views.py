# courses/views.py
from django.shortcuts import render,HttpResponse,redirect
import requests  # For making HTTP requests

def subject_list_view(request):
    api_url = 'http://127.0.0.1:8000/syllabus_api/subject-list/'  # API URL
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            subjects = response.json()  # Convert JSON to Python dictionary
            print(subjects)  # Log the response for debugging
        else:
            subjects = []  # If API fails, show an empty list
    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        subjects = []  # Handle API errors gracefully

    return render(request, 'courses/subject_list.html', {'subjects': subjects})



def subject_detail_view(request, pk):
    url = f"http://127.0.0.1:8000/syllabus_api/subject-detail/{pk}/"  # Adjust API URL
    response = requests.get(url)
    if response.status_code == 200:
        subject = response.json()
        return render(request, 'courses/subject_detail.html', {'subject': subject})
    else:
        return render(request, 'courses/subject_detail.html', {'error': 'Subject not found'})

def subject_create_view(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "code": request.POST.get("code"),
            "semester": request.POST.get("semester"),
        }
        api_url = "http://127.0.0.1:8000/syllabus_api/subject-create/"
        response = requests.post(api_url, json=data)

        if response.status_code == 201:
            return redirect("subject-list")
    
    return render(request, "courses/subject_create.html")

# ✅ Subject Update View
def subject_update_view(request, pk):
    api_url = f"http://127.0.0.1:8000/syllabus_api/subject-detail/{pk}/"
    response = requests.get(api_url)
    subject = response.json() if response.status_code == 200 else {}

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "code": request.POST.get("code"),
            "semester": request.POST.get("semester"),
        }
        update_url = f"http://127.0.0.1:8000/syllabus_api/subject-update/{pk}/"
        response = requests.put(update_url, json=data)

        if response.status_code == 200:
            return redirect("subject-list")

    return render(request, "courses/subject_update.html", {"subject": subject})

# ✅ Subject Delete View
def subject_delete_view(request, pk):
    api_url = f"http://127.0.0.1:8000/syllabus_api/subject-detail/{pk}/"
    response = requests.get(api_url)
    subject = response.json() if response.status_code == 200 else {}

    if request.method == "POST":
        delete_url = f"http://127.0.0.1:8000/syllabus_api/subject-delete/{pk}/"
        response = requests.delete(delete_url)

        if response.status_code == 204:
            return redirect("subject-list")

    return render(request, "courses/subject_delete.html", {"subject": subject})