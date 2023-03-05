from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from app.models import jobPost


# Create your views here.


def hello(request):
    # template = loader.get_template('app/hello.html')
    context = {"name": "mahdi"}
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)


def job_list(request):
    # list_of_job = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     print(reversed('job_detail'))
    #     list_of_job += f"<li><a href='job/{job_id}'>{j}</a></li>"
    # list_of_job += "</ul>"
    # return HttpResponse(list_of_job)
    jobs = jobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    print(type(id))
    try:
        if id == 0:
            return redirect(reversed('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        # context = {"job_title": job_title[id], "job_description": job_description[id]}
        job = jobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("<h2>Not found</h2>")
