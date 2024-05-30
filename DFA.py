


""" maybe go into REs, NFAs, then maybe CFGs and PDAs"""

from collections import deque
class DFA: 
    """Implements deterministic finite state automata"""
    
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q #set of states
        self.sigma = sigma # finite set of chars, alphabet
        if len(delta) != len(Q)*len(sigma): raise ValueError("Nuh uh, not deterministic!")
        #for efficiency, lets convert this from set of 3-tuples (fromState, currChar, toState) into
        #a dict of toState: {dict of currChar:toState pairs} pairs
        self.delta = {}
        for state in self.Q:
            self.delta[state] = {}
        for triple in delta:
            fromState, currChar, toState = triple
            self.delta[fromState][currChar] = toState
            
        
        
        
        if q0 not in self.Q: raise ValueError(f"{q0} should be a state in Q, silly!")
        self.q0 = q0 # single initial state
        if not isinstance(F, set) or len(F)==0 or len(F-self.Q)!=0: raise ValueError(f"{F} is not valid set of final states")
        self.F = F
        
    
        
    
    def runOn(self, w):
        """Simulates string w on DFA, let's try it"""
        currState = self.q0
        for char in w:
            currState = self.delta[currState][char]
        return currState in self.F
    
    
    def enumerateTillLen(self, n):
        """Enumerates over all strings w under sigma st |w| <= n"""
        #Now, how tf am I gonna implement this???
        if not isinstance(n, int) or n<0: raise ValueError("You goober ahaha 2nd param should be nonnegative int")
        cand = [] #candidates, let's find all candidates then apply filter on runs on!
        cand.append('')
        dq = deque([''])
        iterations = 0
        while n > 0:
            next= []     
            for string in dq:     
                for char in self.sigma:
                    newStr = string + char
                    cand.append(newStr)
                    next.append(newStr)
            dq = deque(next)
                    
            iterations +=1
            n -=1
                    
            
        
        return list(filter(self.runOn, cand))
        
        
        
if __name__== '__main__':

    Q = {'i','f','d'}#initial state, final state, dead state
    sigma = {'a','b'}
    delta = {('i','b','d'),('i','a','f'),('d','b','d'),('d','a','d'),('f','b','f'),('f','a','f')}
    q0 = 'i'
    F = {'f'}

    dfa = DFA(Q, sigma, delta, q0, F) # should Accept iff w starts with a

    print(dfa.delta)


    print(dfa.runOn('abbabaaba')) # T
    print(dfa.runOn('aaaaa')) # T
    print(dfa.runOn('a')) # T
    print(dfa.runOn('')) # F
    print(dfa.runOn('bababa')) # F
    print(dfa.runOn('baaaaaa')) # F
    print(dfa.runOn('bbbb')) # F
    #I would add randomized test cases if I weren't lazy haha
    
    print(dfa.enumerateTillLen(4))#shit works!!!!
    
