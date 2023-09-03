from stack import*
def testSymbols(data,stk):
    # to enter the paranthesis for matching
    lefty='{[('
    righty='}])'

# if ch in lefty then push
    for ch in data:
        if ch in lefty:
            stk.stackpush(ch)
            # if no lefty only righty then return false
        elif ch in righty:
            if stk.isStackEmpty():
                return False
                # if lefty is not equal to righty then pop
            if righty.index(ch)!=lefty.index(stk.stackpop()):
                return False
    return(stk.isEmpty())

