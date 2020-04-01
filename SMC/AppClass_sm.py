# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : AppClass.sm

import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def Digital(self, fsm, ch):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def EqSign(self, fsm):
        self.Default(fsm)

    def Letter(self, fsm, ch):
        self.Default(fsm)

    def MinSign(self, fsm):
        self.Default(fsm)

    def OpSign(self, fsm):
        self.Default(fsm)

    def SpaceSym(self, fsm):
        self.Default(fsm)

    def Start(self, fsm):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Zero(self, fsm, ch):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class MainMap_Default(AppClassState):

    def Start(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearSMC()
        finally:
            fsm.setState(MainMap.Start)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Zero(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def EqSign(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def OpSign(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def MinSign(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


class MainMap_Start(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.InsertDigstr(ch)
        finally:
            fsm.setState(MainMap.StrNum)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Start)
        fsm.getState().Entry(fsm)


class MainMap_Space(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.EqSignIsUsed() and ctxt.isCountTermsOne() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(MainMap.StrDig)
                fsm.getState().Entry(fsm)
        elif ctxt.OperSignIsUsed() and ctxt.isCountTermsMoreOne() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(MainMap.StrDig)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.Digital(self, fsm, ch)
        
    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.OperSignIsUsed() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)
        elif ctxt.isCounterMoreOrOne() and ctxt.CheckNames() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.EOS(self, fsm)
        
    def EqSign(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.EqSignIsNotUsed() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.UseEqSign()
            finally:
                fsm.setState(MainMap.EqualSign)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.EqSign(self, fsm)
        
    def Letter(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isCounterZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsertValname(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(MainMap.StrLit)
                fsm.getState().Entry(fsm)
        elif ctxt.EqSignIsUsed() and ctxt.isCountTermsOne() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearLitstr()
                ctxt.InsertLitstr(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(MainMap.StrLit)
                fsm.getState().Entry(fsm)
        elif ctxt.OperSignIsUsed() and ctxt.isCountTermsMoreOne() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearLitstr()
                ctxt.InsertLitstr(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(MainMap.StrLit)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.Letter(self, fsm, ch)
        
    def MinSign(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.OperSignIsUsed() or ctxt.isCountTermsOne() and ctxt.EqSignIsUsed() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.MinusSign)
            fsm.getState().Entry(fsm)
        elif ctxt.EqSignIsUsed() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.UseOperSign()
            finally:
                fsm.setState(MainMap.OperSign)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.MinSign(self, fsm)
        
    def OpSign(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.EqSignIsUsed() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.UseOperSign()
            finally:
                fsm.setState(MainMap.OperSign)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.OpSign(self, fsm)
        
    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Space)
        fsm.getState().Entry(fsm)


class MainMap_StrDig(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isLess16() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Digital(self, fsm, ch)
        
    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.CheckNames() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
                ctxt.CountTermsInc()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearOperSign()
            ctxt.LengthZero()
            ctxt.CountTermsInc()
        finally:
            fsm.setState(MainMap.Space)
            fsm.getState().Entry(fsm)


    def Zero(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isLess16() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Zero(self, fsm, ch)
        
class MainMap_StrNum(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.InsertDigstr(ch)
        finally:
            fsm.setState(endState)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Space)
        fsm.getState().Entry(fsm)


    def Zero(self, fsm, ch):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.InsertDigstr(ch)
        finally:
            fsm.setState(endState)


class MainMap_StrLit(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isLess16() and ctxt.isCounterMoreOrOne() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertLitstr(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        elif ctxt.isLess16() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertValname(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Digital(self, fsm, ch)
        
    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCounterMoreOrOne() and ctxt.CheckNames() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
                ctxt.CounterInc()
                ctxt.CountTermsInc()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


    def Letter(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isLess16() and ctxt.isCounterMoreOrOne() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertLitstr(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        elif ctxt.isLess16() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertValname(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Letter(self, fsm, ch)
        
    def SpaceSym(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.CheckNames() and ctxt.isLess16() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearOperSign()
                ctxt.LengthZero()
                ctxt.CounterInc()
                ctxt.CountTermsInc()
            finally:
                fsm.setState(MainMap.Space)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.SpaceSym(self, fsm)
        
    def Zero(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.isLess16() and ctxt.isCounterMoreOrOne() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertLitstr(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        elif ctxt.isLess16() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsertValname(ch)
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Zero(self, fsm, ch)
        
class MainMap_EqualSign(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Space)
        fsm.getState().Entry(fsm)


class MainMap_OperSign(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Space)
        fsm.getState().Entry(fsm)


class MainMap_MinusSign(MainMap_Default):

    def Digital(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
        finally:
            fsm.setState(MainMap.StrDig)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


class MainMap_Error(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(endState)


class MainMap_OK(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Acceptable()
            ctxt.InsertValnameinDict()
        finally:
            fsm.setState(endState)


class MainMap(object):

    Start = MainMap_Start('MainMap.Start', 0)
    Space = MainMap_Space('MainMap.Space', 1)
    StrDig = MainMap_StrDig('MainMap.StrDig', 2)
    StrNum = MainMap_StrNum('MainMap.StrNum', 3)
    StrLit = MainMap_StrLit('MainMap.StrLit', 4)
    EqualSign = MainMap_EqualSign('MainMap.EqualSign', 5)
    OperSign = MainMap_OperSign('MainMap.OperSign', 6)
    MinusSign = MainMap_MinusSign('MainMap.MinusSign', 7)
    Error = MainMap_Error('MainMap.Error', 8)
    OK = MainMap_OK('MainMap.OK', 9)
    Default = MainMap_Default('MainMap.Default', -1)

class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, MainMap.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
