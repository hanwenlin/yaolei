from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from issues.models import Issues

# Create your views here.
def index(request):
    isssues = Issues.objects.all()
    return render(request,'issues/index.html',{"isssues":isssues})


def search(request):
    search_name = request.POST.get('search')

    isssues = Issues.objects.filter(id=search_name)
    return render(request, 'issues/index.html', {"isssues":isssues})


def addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        issue = clean_data.get('issue')
        reason = clean_data.get('reason')
        solution = clean_data.get('solution')

        Issues.objects.create(issue=issue,reason=reason,solution=solution)
        # return render(request, 'material/addition.html')
        return redirect(reverse('issues:index', args=()))

    return render(request, 'issues/addition.html')


def modifys(request,issueid):
    issue = Issues.objects.get(id=issueid)
    if request.method=='POST':
        clean_data = request.POST
        issue = clean_data.get('issue')
        reason = clean_data.get('reason')
        solution = clean_data.get('solution')
        Issues.objects.filter(id=issueid).update(issue=issue,reason=reason,solution=solution)

        return redirect(reverse('issues:index', args=()))
    return render(request,'issues/modiftion.html',{"issue":issue})
