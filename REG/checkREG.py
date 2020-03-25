import re
import time

refer = r'^(?P<strnum>\d+) +(?P<valname>[a-zA-Z][a-zA-Z0-9]{0,15}) +\= +\-?((?P<lit1>[a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*)( +(\+|\-|\*|\/) +\-?(([a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*))*$'
spref = r'\s[^a-zA-Z]+[^a-zA-Z0-9]*'


def readTimeFileREG():
    fl = open('timeREG.txt', 'r')
    print('RegEx time: ' + fl.read())
    fl.close()


def checkFILE():
    f = open('genSTR.txt', 'r')
    resf = open('resSTR.txt', 'w')
    ftime = open('timeREG.txt', 'w')
    time_start = time.perf_counter()
    numline = 1
    for line in f.readlines():
        res = 1
        match = re.fullmatch(refer, line.rstrip())
        gr = re.split(spref, line.rstrip())
        if match:
            # print(gr)
            if match.group('lit1'):
                if match.group('valname') != match.group('lit1'):
                    continue
            for ind in gr[1:]:
                if match.group('valname') == ind:
                    res += 1
                else:
                    continue
            resf.write(match.group('strnum') + ' : ' + str(res) + '\n')
        if numline % 10000 == 0:
            print(numline)
            ftime.write(str(time.perf_counter() - time_start) + '\n')
        numline += 1
            # print(match.group('strnum') + ' : ' + str(res))
            # print(match.group('valname') + ' : ' + str(res))
    ftime.close()
    f.close()
    resf.close()


def checkREGstr(strch):
    res = 1
    match = re.fullmatch(refer, strch.rstrip())
    gr = re.split(spref, strch.rstrip())
    if match:
        #print(match)
        #print(gr)
        if match.group('lit1'):
            if match.group('valname') != match.group('lit1'):
                return 'Unacceptable'
        for ind in gr[1:]:
            if match.group('valname') == ind:
                res += 1
            else:
                return 'Unacceptable'
        return match.group('strnum') + ': ' + str(res)
    else:
        return 'Unacceptable'
