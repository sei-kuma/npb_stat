from django.http.response import HttpResponse
from django.shortcuts import render
from npb_stats.forms import SelectForm
from npb_stats.pitcher import pitcherSearch
from npb_stats.hitter import hitterSearch


def index(request):
    f= SelectForm()
    playerChoice = request.GET.get('playerChoice')
    teamChoice = request.GET.get('teamChoice')
    hitterTargetChoice = request.GET.get('hitterTargetChoice')
    pitcherTargetChoice = request.GET.get('pitcherTargetChoice')
    hitterDataChoice = request.GET.get('hitterDataChoice')
    pitcherDataChoice = request.GET.get('pitcherDataChoice')
    number = request.GET.get('number')

    if playerChoice==None:
        return render(request, 'form.html', {'form1': f})
    elif playerChoice=="1":
        isFarm = ""
        result = hitterSearch(isFarm, teamChoice, hitterTargetChoice, hitterDataChoice, number, request)
    elif playerChoice=="2":
        isFarm = "-farm"
        result = hitterSearch(isFarm, teamChoice, hitterTargetChoice, hitterDataChoice, number, request)
    elif playerChoice=="3":
        isFarm = ""
        result = pitcherSearch(isFarm, teamChoice, pitcherTargetChoice, pitcherDataChoice, number, request)
    elif playerChoice=="4":
        isFarm = "-farm"
        result = pitcherSearch(isFarm, teamChoice, pitcherTargetChoice, pitcherDataChoice, number, request)
    else:
        return render(request, 'error.html')

    return render(request, 'result.html', {'result':result})