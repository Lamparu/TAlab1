import AppClass
import time


def readTimeFileSMC():
    f = open('timeSMC.txt', 'r')
    print('SMC time: ' + f.read())
    f.close()


def checkSMCstr(strch):
    machine = AppClass.AppClass()
    match = machine.CheckString(strch)
    # return machine.Acceptable()
    if match:
        return machine.GetStrNum() + ': ' + str(machine.GetCounter())
    else:
        return 'Unacceptable'


def SMCcheck():
    machine = AppClass.AppClass()
    f = open('genSTR.txt', 'r')
    res = open('resSMC.txt', 'w')
    ftime = open('timeSMC.txt', 'w')
    time_start = time.perf_counter()
    numline = 0
    for line in f.readlines():
        numline += 1
        match = machine.CheckString(line)
        if match:
            res.write(machine.GetStrNum() + ': ' + str(machine.GetCounter()) + '\n')
        if numline % 10000 == 0:
            ftime.write(str(time.perf_counter() - time_start) + '\n')
    ftime.close()
    f.close()
    res.close()
