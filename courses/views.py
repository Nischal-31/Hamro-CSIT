# courses/views.py
from django.shortcuts import render,HttpResponse,redirect
import requests  # For making HTTP requests
from django.http import Http404

def courses_view(request):
    api_url = 'http://127.0.0.1:8000/syllabus_api/course-list/'
    response = requests.get(api_url)

    if response.status_code == 200:
        courses = response.json()  # API response with courses
        print("API Response:", courses)  # Debugging
    else:
        courses = []

    return render(request, 'courses/courses.html', {'courses': courses})




#-------------------------------------------------------------------------------------------------------------------
#                       COURSE VIEWS
#-------------------------------------------------------------------------------------------------------------------


def course_list_view(request):
    api_url = 'http://127.0.0.1:8000/syllabus_api/course-list/'
    response = requests.get(api_url)

    if response.status_code == 200:
        courses = response.json()  # API response with courses
        print("API Response:", courses)  # Debugging
    else:
        courses = []

    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail_view(request, pk):
    url = f"http://127.0.0.1:8000/syllabus_api/course-detail/{pk}/"  # Adjust API URL for course detail
    response = requests.get(url)

    if response.status_code == 200:
        course = response.json()
        return render(request, 'courses/course_detail.html', {'course': course})
    else:
        return render(request, 'courses/course_detail.html', {'error': 'Course not found'})


def course_create_view(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description"),
        }
        api_url = "http://127.0.0.1:8000/syllabus_api/course-create/"
        response = requests.post(api_url, json=data)

        if response.status_code == 201:
            return redirect("course-list")  # Redirect to course list page
    
    return render(request, "courses/course_create.html")


def course_update_view(request, pk):
    # Get the current course data from the API to pre-populate the form
    api_url = f"http://127.0.0.1:8000/syllabus_api/course-detail/{pk}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        course = response.json()
    else:
        return redirect("course-list")

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description"),
        }

        # Send POST request to update the course
        update_url = f"http://127.0.0.1:8000/syllabus_api/course-update/{pk}/"
        update_response = requests.post(update_url, json=data)

        if update_response.status_code == 200:
            return redirect("course-list")
        else:
            return render(request, "courses/course_update.html", {"course": course, "error": "Failed to update course."})

    return render(request, "courses/course_update.html", {"course": course})


def course_delete_view(request, pk):
    # Get the course to be deleted
    api_url = f"http://127.0.0.1:8000/syllabus_api/course-detail/{pk}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        course = response.json()
    else:
        return redirect("course-list")

    if request.method == "POST":
        # Send DELETE request to delete the course
        delete_url = f"http://127.0.0.1:8000/syllabus_api/course-delete/{pk}/"
        delete_response = requests.delete(delete_url)

        if delete_response.status_code == 204:
            return redirect("course-list")
        else:
            return render(request, "courses/course_delete.html", {"course": course, "error": "Failed to delete course."})

    return render(request, "courses/course_delete.html", {"course": course})


#-------------------------------------------------------------------------------------------------------------------
#                       SEMESTER VIEWS
#-------------------------------------------------------------------------------------------------------------------

def semester_list_view(request):
    api_url = 'http://127.0.0.1:8000/syllabus_api/semester-list/'
    response = requests.get(api_url)

    if response.status_code == 200:
        semesters = response.json()
        print("API Response:", semesters)  # Debugging
    else:
        semesters = []
    
    return render(request, 'courses/semester_list.html', {'semesters': semesters})


def semester_detail_view(request, pk):
    url = f"http://127.0.0.1:8000/syllabus_api/semester-detail/{pk}/"  # Adjust API URL
    response = requests.get(url)
    if response.status_code == 200:
        semester = response.json()
        return render(request, 'courses/semester_detail.html', {'semester': semester})
    else:
        return render(request, 'courses/semester_detail.html', {'error': 'Semester not found'})

def semester_create_view(request):
    if request.method == "POST":
        data = {
            "number": request.POST.get("number"),
            "description": request.POST.get("description"),
        }
        api_url = "http://127.0.0.1:8000/syllabus_api/semester-create/"
        response = requests.post(api_url, json=data)

        if response.status_code == 201:
            return redirect("semester-list")  # Redirect to the semester list page
    
    return render(request, "courses/semester_create.html")

def semester_update_view(request, pk):
    # Get the current semester data from the API to pre-populate the form
    api_url = f"http://127.0.0.1:8000/syllabus_api/semester-detail/{pk}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        semester = response.json()  # Get the current semester data
    else:
        return redirect("semester-list")

    if request.method == "POST":
        # Get updated fields from the form data
        data = {
            "number": request.POST.get("number"),
            "description": request.POST.get("description"),
        }

        print("Data being sent to the API:", data)  # Debugging print

        # Send POST request to update the semester
        update_url = f"http://127.0.0.1:8000/syllabus_api/semester-update/{pk}/"
        update_response = requests.post(update_url, json=data)

        print("API Response:", update_response.status_code, update_response.json())  # Debugging print

        if update_response.status_code == 200:
            return redirect("semester-list")
        else:
            return render(request, "courses/semester_update.html", {"semester": semester, "error": "Failed to update semester."})

    return render(request, "courses/semester_update.html", {"semester": semester})


def semester_delete_view(request, pk):
    # Get the semester to be deleted
    api_url = f"http://127.0.0.1:8000/syllabus_api/semester-detail/{pk}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        semester = response.json()  # Get the current semester data
    else:
        return redirect("semester-list")

    if request.method == "POST":
        # Send DELETE request to delete the semester
        delete_url = f"http://127.0.0.1:8000/syllabus_api/semester-delete/{pk}/"
        delete_response = requests.delete(delete_url)

        if delete_response.status_code == 204:
            return redirect("semester-list")  # Redirect to the semester list after successful deletion
        else:
            return render(request, "courses/semester_delete.html", {"semester": semester, "error": "Failed to delete semester."})

    return render(request, "courses/semester_delete.html", {"semester": semester})


#-------------------------------------------------------------------------------------------------------------------
#                       SUBJECT VIEWS
#-------------------------------------------------------------------------------------------------------------------

def subject_list_view(request):
    api_url = 'http://127.0.0.1:8000/syllabus_api/subject-list/'
    response = requests.get(api_url)

    if response.status_code == 200:
        subjects = response.json()
        print("API Response:", subjects)  # Debugging
    else:
        subjects = []
    
    return render(request, 'courses/subject_list.html', {'subjects': subjects})


def subject_detail_view(request, pk):
    api_url = f"http://127.0.0.1:8000/syllabus_api/subject-resources/{pk}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return render(request, "courses/subject_detail.html", {"subject": data["subject"], "notes": data["notes"], "past_questions": data["past_questions"]})
    else:
        return render(request, "courses/subject_detail.html", {"error": "Subject not found"})



def subject_create_view(request):
    api_url = "http://127.0.0.1:8000/syllabus_api/semester-list/"
    response = requests.get(api_url)

    if response.status_code == 200:
        semesters = response.json()
    else:
        semesters = []

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "code": request.POST.get("code"),
            "semester": request.POST.get("semester"),  # Sending correct semester ID
        }
        create_url = "http://127.0.0.1:8000/syllabus_api/subject-create/"
        create_response = requests.post(create_url, json=data)

        if create_response.status_code == 201:
            return redirect("subject-list")

    return render(request, "courses/subject_create.html", {"semesters": semesters})



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