from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from issues.models import Issues,MeterialIssues
from material.models import Meterials


# Create your views here.
def index(request):
    isssues = Issues.objects.all()
    isssuemeterials = MeterialIssues.objects.all()
    return render(request,'issues/index.html',{"isssues":isssues,"issumeters":isssuemeterials})


def search(request):
    search_name = request.POST.get('search')
    # isssues = Issues.objects.filter(id=search_name)
    isssues = get_list_or_404(Issues,id=search_name)

    return render(request, 'issues/index.html', {"isssues":isssues})


def addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        issuetype = clean_data.get('issuetype')
        issue = clean_data.get('issue')
        reason = clean_data.get('reason')
        solution = clean_data.get('solution')

        Issues.objects.create(issueType=issuetype,issue=issue,reason=reason,solution=solution)
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


def issuemeterial_addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        pubtime = clean_data.get('pubtime')
        meterial = clean_data.get('meterial')
        histcode = clean_data.get('histcode')
        issuetype = clean_data.get('issuetype')
        solution = clean_data.get('solution')
        meterial_id = Meterials.objects.get(meterialName=meterial).id
        issue_id = Issues.objects.get(issueType=issuetype).id

        MeterialIssues.objects.create(pubtime=pubtime,meterial_id=meterial_id,issue_id=issue_id,histcode=histcode)
      #  Issues.objects.create(issueType=issuetype,issue=issue,reason=reason,solution=solution)
        # return render(request, 'material/addition.html')
        return redirect(reverse('issues:index', args=()))

    return render(request, 'issues/addtion_issuemeter.html')


def issuemeterial_search(request):
    search_name = request.POST.get('issue_search')
    print(search_name)
    # isssues = Issues.objects.filter(id=search_name)
    isssuemeterials = get_list_or_404(MeterialIssues, id=search_name)

    return render(request, 'issues/index.html', {"issumeters":isssuemeterials})

def issuemeterial_modify(request,issuemeterid):
    meterissues = MeterialIssues.objects.get(id=issuemeterid)
    if request.method == 'POST':
        clean_data = request.POST
        pubtime = clean_data.get('pubtime')
        meterial = clean_data.get('meterial')
        histcode = clean_data.get('histcode')
        issuetype = clean_data.get('issuetype')
        solution = clean_data.get('solution')
        meterial_id = Meterials.objects.get(meterialName=meterial).id
        issue_id = Issues.objects.get(issueType=issuetype).id
        #Issues.objects.filter(id=issueid).update(issue=issue, reason=reason, solution=solution)
        MeterialIssues.objects.filter(id=issuemeterid).update(pubtime=pubtime, meterial_id=meterial_id, issue_id=issue_id, histcode=histcode)

        return redirect(reverse('issues:index', args=()))
    return render(request, 'issues/modiftion_issuemeter.html', {"meterissues": meterissues})