from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def add(request):
    cur_overall = 91 * float(request.POST['curgpa'])

    dl = 4 * float(request.POST['dl'])
    atcd = 3 * float(request.POST['atcd'])
    cc = 4 * float(request.POST['cc'])
    bda = 3 * float(request.POST['bda'])
    sp = 3 * float(request.POST['sp'])
    pfsd = 2 * float(request.POST['pfsd'])
    mcp = 2 * float(request.POST['mcp'])
    ab = 2 * float(request.POST['ab'])

    this_sem_gpa = dl + atcd + cc + bda + sp + pfsd + mcp + ab
    cur_overall = float(cur_overall + dl + atcd + cc + bda + sp + pfsd + mcp + ab)

    cur_sgpa = this_sem_gpa / 23
    cur_gpa = cur_overall / 114

    print(cur_overall, cur_gpa)

    return render(request, "output.html", {'result': cur_gpa})


def cse(request):
    cur_overall = 90.5 * float(request.POST.get('curgpa', 'default'))

    atfl = 5 * float(request.POST.get('atfl', 'default'))
    ts = 4 * float(request.POST.get('ts', 'default'))
    ep = 6 * float(request.POST.get('ep', 'default'))
    pe1 = 6 * float(request.POST.get('pe1', 'default'))
    pe2 = 5 * float(request.POST.get('pe2', 'default'))

    this_sem_gpa = atfl + ts + ep + pe1 + pe2
    cur_overall = float(cur_overall + atfl + ts + ep + pe1 + pe2)

    cur_sgpa = this_sem_gpa / 26
    cur_gpa = cur_overall / 116.5

    return render(request, "output.html", {'result': cur_gpa})


def cser(request):
    cur_overall = 85.5 * float(request.POST.get('curgpa', 'default'))

    atfl = 3 * float(request.POST.get('atfl', 'default'))
    ts = 2 * float(request.POST.get('ts', 'default'))
    ep = 4 * float(request.POST.get('ep', 'default'))
    pe1 = 4 * float(request.POST.get('pe1', 'default'))
    pe2 = 3 * float(request.POST.get('pe2', 'default'))

    this_sem_gpa = atfl + ts + ep + pe1 + pe2
    cur_overall = float(cur_overall + atfl + ts + ep + pe1 + pe2)

    cur_sgpa = this_sem_gpa / 16
    cur_gpa = cur_overall / 101.5

    return render(request, "output.html", {'result': cur_gpa})


def eceh21(request):
    cur_overall = 41 * float(request.POST.get('curgpa', 'default'))

    edc = 6.5 * float(request.POST.get('edc', 'default'))
    cssd = 6 * float(request.POST.get('cssd', 'default'))
    esd = 6.5 * float(request.POST.get('esd', 'default'))
    ann = 5.5 * float(request.POST.get('ann', 'default'))
    pbl = 1.5 * float(request.POST.get('pbl', 'default'))
    ese = 2 * float(request.POST.get('ese', 'default'))
    si = 1 * float(request.POST.get('si', 'default'))

    this_sem_gpa = edc + cssd + esd + ann + pbl + ese + si
    cur_overall = float(cur_overall + edc + cssd + esd + ann + pbl + ese + si)

    cur_sgpa = this_sem_gpa / 29
    cur_gpa = cur_overall / 70
    return render(request, "output.html", {'result': cur_gpa})


def ecer21(request):
    cur_overall = 41 * float(request.POST.get('curgpa', 'default'))

    edc = 4.5 * float(request.POST.get('edc', 'default'))
    cssd = 4 * float(request.POST.get('cssd', 'default'))
    esd = 4.5 * float(request.POST.get('esd', 'default'))
    ann = 3 * float(request.POST.get('ann', 'default'))
    pbl = 1.5 * float(request.POST.get('pbl', 'default'))
    ese = 2 * float(request.POST.get('ese', 'default'))
    si = 1 * float(request.POST.get('si', 'default'))

    this_sem_gpa = edc + cssd + esd + ann + pbl + ese + si
    cur_overall = float(cur_overall + edc + cssd + esd + ann + pbl + ese + si)

    cur_sgpa = this_sem_gpa / 20.5
    cur_gpa = cur_overall / 61.5

    return render(request, "output.html", {'result': cur_gpa})


def csh21(request):
    cur_overall = 39 * float(request.POST.get('curgpa', 'default'))

    os = 3 * float(request.POST.get('os', 'default'))
    ts = 4 * float(request.POST.get('ts', 'default'))
    se = 5 * float(request.POST.get('se', 'default'))
    dbms = 5 * float(request.POST.get('dbms', 'default'))
    aoop = 4 * float(request.POST.get('aoop', 'default'))
    psqt = 4 * float(request.POST.get('psqt', 'default'))
    esc = 2 * float(request.POST.get('esc', 'default'))
    si = 1 * float(request.POST.get('si', 'default'))

    this_sem_gpa = os + ts + se + dbms + aoop + psqt + esc + si
    cur_overall = float( cur_overall + os + ts + se + dbms + aoop + psqt + esc + si)

    cur_sgpa = this_sem_gpa / 28
    cur_gpa = cur_overall / 67

    return render(request, "output.html", {'result': cur_gpa})


def csr21(request):
    cur_overall = 39 * float(request.POST.get('curgpa', 'default'))

    os = 3 * float(request.POST.get('os', 'default'))
    ts = 3 * float(request.POST.get('ts', 'default'))
    se = 3 * float(request.POST.get('se', 'default'))
    dbms = 3 * float(request.POST.get('dbms', 'default'))
    aoop = 4 * float(request.POST.get('aoop', 'default'))
    psqt = 4 * float(request.POST.get('psqt', 'default'))
    esc = 2 * float(request.POST.get('esc', 'default'))
    si = 1 * float(request.POST.get('si', 'default'))

    this_sem_gpa = os + ts + se + dbms + aoop + psqt + esc + si
    cur_overall = float( cur_overall + os + ts + se + dbms + aoop + psqt + esc + si)

    cur_sgpa = this_sem_gpa / 23
    cur_gpa = cur_overall / 62

    return render(request, "output.html", {'result': cur_gpa})


def aih21(request):
    cur_overall = 39 * float(request.POST.get('curgpa', 'default'))

    pns = 3 * float(request.POST.get('pns', 'default'))
    daa = 3.5 * float(request.POST.get('daa', 'default'))
    java = 4 * float(request.POST.get('java', 'default'))
    os = 4 * float(request.POST.get('os', 'default'))
    dm = 5 * float(request.POST.get('dm', 'default'))
    se = 3 * float(request.POST.get('se', 'default'))
    ai = 3 * float(request.POST.get('ai', 'default'))
    pbl = 1.5 * float(request.POST.get('pbl', 'default'))
    ess = 2 * float(request.POST.get('ess', 'default'))

    this_sem_gpa = pns + daa + java + os + dm + se + ai + pbl + ess
    cur_overall = float(cur_overall + pns + daa + java + os + dm + se + ai + pbl + ess)

    cur_sgpa = this_sem_gpa / 29
    cur_gpa = cur_overall / 68

    return render(request, "outai21.html", {'result': cur_gpa})


def air21(request):
    cur_overall = 39 * float(request.POST.get('curgpa', 'default'))

    pns = 3 * float(request.POST.get('pns', 'default'))
    daa = 3.5 * float(request.POST.get('daa', 'default'))
    java = 4 * float(request.POST.get('java', 'default'))
    os = 4 * float(request.POST.get('os', 'default'))
    dm = 3 * float(request.POST.get('dm', 'default'))
    se = 3 * float(request.POST.get('se', 'default'))
    ai = 3 * float(request.POST.get('ai', 'default'))
    pbl = 1.5 * float(request.POST.get('pbl', 'default'))
    ess = 2 * float(request.POST.get('ess', 'default'))

    this_sem_gpa = pns + daa + java + os + dm + se + ai + pbl + ess
    cur_overall = float(cur_overall + pns + daa + java + os + dm + se + ai + pbl + ess)

    cur_sgpa = this_sem_gpa / 27
    cur_gpa = cur_overall / 66

    return render(request, "outai21.html", {'result': cur_gpa})


def ec20(request):
    cur_overall = 90.5 * float(request.POST.get('curgpa', 'default'))

    ech = 4 * float(request.POST.get('ech', 'default'))
    fc2 = 4 * float(request.POST.get('fc2', 'default'))
    fc3 = 4 * float(request.POST.get('fc3', 'default'))
    pe1 = 3 * float(request.POST.get('pe1', 'default'))
    pe2 = 3 * float(request.POST.get('pe2', 'default'))
    ccs = 2 * float(request.POST.get('ccs', 'default'))
    tp = 3 * float(request.POST.get('tp', 'default'))
    ti = 2 * float(request.POST.get('ti', 'default'))
    mcp = 2 * float(request.POST.get('mcp', 'default'))

    this_sem_gpa = ech + fc2 + fc3 + pe1 + pe2 + ccs + tp + ti + mcp
    cur_overall = float(cur_overall+ ech + fc2 + fc3 + pe1 + pe2 + ccs + tp + ti + mcp)

    cur_sgpa = this_sem_gpa / 27
    cur_gpa = cur_overall / 117.5

    return render(request, "outec20.html", {'result': cur_gpa})


def fed(request):

    ctsd = 5.5 * float(request.POST.get('ctsd', 'default'))
    dtw = 2 * float(request.POST.get('dtw', 'default'))
    dlp = 4 * float(request.POST.get('dlp', 'default'))
    mfc = 4.5 * float(request.POST.get('mfc', 'default'))
    ipe = 2 * float(request.POST.get('ipe', 'default'))

    cur_overall = float(ipe + mfc + dlp + dtw + ctsd)

    cur_gpa = cur_overall / 18

    return render(request, "outfed.html", {'result': cur_gpa})















