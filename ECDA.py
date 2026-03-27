#ECDA ---> Electrical Circuit Design & Analysis
import sympy as sp
import schemdraw
import schemdraw.elements as elm

class Wire:
    def __init__(self, n1:int, n2:int):
        self.n1 = n1
        self.n2 = n2
                                   
class Resistor:                 
    def __init__(self, n1:int, n2:int, R:int):
        self.n1 = n1
        self.n2 = n2
        self.R = R
        assert self.R!=0, 'The Resistor cannot be 0 Ohm'


class VoltageSource:
    def __init__(self, n1:int, n2:int, V):
        self.n1 = n1
        self.n2 = n2
        self.V = V 
        assert self.V!=0, 'The VoltageSource cannot be 0V'

class CurrentSource:                            #######
    def __init__(self, n1:int, n2:int, I):      #######
        self.n1 = n1                            #######
        self.n2 = n2                            #######
        self.I = I                              #######
        assert self.I!=0, 'The CurrentSource cannot be 0A'
        
class Capacitor:                    #######
    def __init__(self,n1,n2,C):     #######
        self.n1 = n1                #######
        self.n2 = n2                ####3#3
        self.C = C                  #333333  I_c=CDV -> I=CjwV
        assert self.C!=0, 'The Capacitor cannot be 0 F'

class Inductor:                     #######
    def __init__(self,n1,n2,L):     #######
        self.n1=n1                  #######
        self.n2=n2                  #######
        self.L=L                    #######  V_L=LDI -> I=V_L/jwL
        assert self.L!=0, 'The Inductor cannot be 0 H'

class Circuit:   #class |circuit| have 3 |fun.| 1 inif(element and node) 2 add(to add them) 3 solve(bigset part)
    def __init__(self):   #
        self.elements = []  #
        self.nodes = set()
        self.loop = set()         #######
    
    def penfrq(self,w):
        self.w=w*2*sp.pi

    def __str__(self):
        return f'Circuit With {len(self.elements)} elements' #self.__ne__
    
    def add(self, element):  #here def. element in add fun. 
        self.elements.append(element)   #add element in elements is add element in end of list [a,b].append(c) ==> [a,b,c]
        self.nodes.update([element.n1, element.n2]) # x={a,b,c} y={a,m,v} z={g,a} x.update(y,z) ==> x={a,b,c,m,v,g} the order chenge on every run
    #
    def Loop_solve(self):
        Loops= list(self.loop)
        pass



    def solve(self,name,w=None, ref=0):   #select ref voltage 
        nodes = list(self.nodes - {ref})
        cc=[]
        ccc=[]
        V = sp.symbols(' '.join([f'V{n}' for n in nodes]))   #first use of sympy Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs' // it have for loop in it
        I = sp.symbols(' '.join([f'I{n}' for n in nodes]))   #######################
        
        #self.w = sp.symbols('w') if w is None else w
        
        eqs = [] 
        eqss = []                                            #list of slotion of liner eq's
        for n in nodes: 
            current_sum = 0
            for e in self.elements:
                if isinstance(e, Resistor): #here for Resistor
                    if e.n1 == n:
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0 #sp.Symbol(f'V{e.n1}') to def varebal is dep on you 
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0 #if e.n2 != ref else 0 to det if the node in V_ref
                        current_sum += (v2 - v1) / e.R  #here to def currents in nude fuces on (+=) 
                    elif e.n2 == n:
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0
                        current_sum += (v1 - v2) / e.R #suap the sign of v2 and v1

                elif isinstance(e, VoltageSource): #here for VoltageSource
                    if e.n1 == n:
                        current_sum += sp.Symbol(f'I_V{e.n1}_{e.n2}') 
                    elif e.n2 == n:
                        current_sum -= sp.Symbol(f'I_V{e.n1}_{e.n2}')

                elif isinstance(e, CurrentSource): #here for CurrentSource      #####
                    if e.n1 == n:                                               #####
                        current_sum += e.I
                        #current_sum += sp.Symbol(f'I_V{e.n1}_{e.n2}') 
                    elif e.n2 == n:                                             #####
                        current_sum -= e.I 
                        #current_sum -= sp.Symbol(f'I_V{e.n1}_{e.n2}')           #####

                ####fffff####
                elif isinstance(e, Capacitor): #here for capsetor      #####
                    if e.n1 == n:                                               #####
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0        #####
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0        #####
                        current_sum += e.C*(sp.I*self.w)*(v2-v1) # e.C*s*(v1-v2)
                        #current_sum += sp.Symbol(f'I_V{e.n1}_{e.n2}') 
                    elif e.n2 == n:                                             #####
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0        #####
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0        #####
                        current_sum += e.C*(sp.I*self.w)*(v1-v2) 
                        #current_sum -= sp.Symbol(f'I_V{e.n1}_{e.n2}')
                ####eeeee####
                #sp.laplace_transform(sp.diff(V,t),t,s)
                ####fffff####
                elif isinstance(e, Inductor): #here for indector      #####
                    if e.n1 == n:                                               #####
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0        #####
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0        #####
                        current_sum += (v2-v1)/(sp.I*self.w*e.L) # (v2-v1)/s*e.L
                        #current_sum += sp.Symbol(f'I_V{e.n1}_{e.n2}') 
                    elif e.n2 == n:                                             #####
                        v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0        #####
                        v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0        #####
                        current_sum -= (v2-v1)/(sp.I*self.w*e.L)
                        #current_sum -= sp.Symbol(f'I_V{e.n1}_{e.n2}')
                ####eeeee####


            eqs.append(sp.Eq(current_sum, 0)) #--> sum(I)=0 it solve and add slotions in eqs list ###
        for e in self.elements:
            if isinstance(e, VoltageSource):
                v1 = sp.Symbol(f'V{e.n1}') if e.n1 != ref else 0
                v2 = sp.Symbol(f'V{e.n2}') if e.n2 != ref else 0
                eqs.append(sp.Eq(v1 - v2, e.V))
                cc.append(sp.solve(eqs, dict=True))
        #return f'for {name.__str__()} --> {sp.solve(eqs, dict=True)}///{cc}' ################:return self} --> {sp.solve(eqs, dict=True)}' ################
        for e in self.elements:
            if isinstance(e, CurrentSource):
                i1 = sp.Symbol(f'I{e.n1}') if e.n1 != ref else 0
                i2 = sp.Symbol(f'I{e.n2}') if e.n2 != ref else 0
                eqss.append(sp.Eq(i1-i2, e.I))
                ccc.append(sp.solve(eqss, dict=True))
        return f'for {name.__str__()} --> {sp.solve(eqs, dict=True)}///{sp.solve(eqss, dict=True)}'
    # lambda self:return self 
    

    def show(self): # not ready/useful
        d = schemdraw.Drawing()
        for e in self.elements:
            if isinstance(e, Resistor):
                a,b=e.n1,e.n2
                d.add(elm.Resistor().label(f'{e.R}Ω'))
            elif isinstance(e, VoltageSource):
                d.add(elm.SourceV().label(f'{e.V}V'))
           
        d.draw()

 
print('\n','='*50)
 # Example 
E = Circuit()
E.penfrq(60)
E.add(VoltageSource(1, 0, 120))   # VS1
E.add(VoltageSource(4, 0, 60))    # VS2
E.add(VoltageSource(6, 5, 30))    # VS3
E.add(CurrentSource(2, 0, 2))     # IS1
E.add(CurrentSource(5, 0, 3))     # IS2
E.add(Resistor(1, 2, 10))         # R1
E.add(Capacitor(1, 2, 100e-6))    # C1
E.add(Resistor(2, 3, 20))         # R2
E.add(Inductor(2, 3, 0.05))       # L1
E.add(Resistor(3, 0, 5))          # R3
E.add(Resistor(3, 4, 12))         # R6
E.add(Resistor(4, 5, 15))         # R4
E.add(Capacitor(4, 5, 200e-6))    # C2
E.add(Resistor(5, 6, 8))          # R5
E.add(Inductor(5, 6, 0.08))       # L2
E.add(Capacitor(6, 0, 50e-6))
print(E.solve('E')) # for E --> [{I_V1_0: 2.96102662761248 - 1.83234387091313*I, I_V4_0: -0.369844918942153 + 2.29211885523061*I, I_V6_5: 4.30986879506152 + 0.75847579299064*I, V1: 120.000000000000, V2: 100.122538053436 + 25.8170653199314*I, V3: 35.1565645680441 - 6.4670960149875*I, V4: 60.0000000000000, V5: 63.0098403703861 - 29.7019620723147*I, V6: 93.0098403703861 - 29.7019620723147*I}]///[{I2: 2, I5: 3}]

e = Circuit()
e.add(VoltageSource(1,0,48))
e.add(VoltageSource(3,0,12))
e.add(Resistor(1,2,10))
e.add(Resistor(2,3,15))
e.add(Resistor(2,0,20))
print(e.solve('e'))

c = Circuit() #Correct 
c.penfrq(60)
c.add(VoltageSource(1,2,5))
c.add(Resistor(1, 0, 5))
c.add(VoltageSource(2,0,4))
c.add(Resistor(1,2,10))
c.add(Resistor(1,2,5))
c.add(Capacitor(1,2,10))
print(c.solve('c')) #---> [{I_V1_2: 3.3 - 18849.5559215388*I, I_V2_0: 1.80, V1: 9.0, V2: 4.0}]

c281= Circuit() #2.71 Real  issss correct !!!!!!
c281.add(CurrentSource(0,1,12))
c281.add(Resistor(1,2,6))
c281.add(Resistor(0,1,12))
c281.add(Resistor(0,2,12))
c281.add(Resistor(0,2,12))
print(c281.solve('c281')) #---> [{V1: -72, V2: -36}]///[] # the V1 corect BUT V2 is ground in calc not -36V

d= Circuit()         #is correct (:
d.add(Resistor(0,1,2000)) # the circuit model in prbelem 5.32 in book basic engineering circet analysis page 255
d.add(Resistor(0,2,4000))
d.add(Resistor(0,3,2000))
d.add(VoltageSource(2,3,12))
d.add(VoltageSource(2,1,6)) # All of them OK BUT V2 is 72/5 not 36/5 or V3 + 12
print(d.solve('d')) #---> [{I_V2_1: -3/5000, I_V2_3: 3/1250, V1: 6/5, V2: 36/5, V3: -24/5}]] 

c270= Circuit() #2.70
c270.add(VoltageSource(0,1,15))   
c270.add(Resistor(0,1,10))
c270.add(Resistor(1,2,16))
c270.add(Resistor(0,2,8)) # correct but is not have V2 is ground 
print(c270.solve('c270')) #---> [{I_V0_1: -17/8, V1: -15, V2: -5}] I_V0_1 is for overall I supplyed by VoltageSource

print('\n','='*50,'\n')

 # Example
c = Circuit()
c.add(VoltageSource(1, 0, 10))
c.add(Resistor(1, 0, 5))
c.add(VoltageSource(2,0,4))
c.add(Resistor(1,2,10))
c.add(Resistor(1,2,5))
c.penfrq(60)
c.add(Capacitor(1,2,10))
print(c.solve('c')) #for c --> [{I_V1_0: 3.8 + 3600.0*I, I_V2_0: -1.8 - 3600.0*I, V1: 10.0000000000000, V2: 4.00000000000000}]///[[{I_V1_0: V2*(-0.3 - 600.0*I) + 5.0 + 6000.0*I, I_V2_0: V2*(0.3 + 600.0*I) - 3.0 - 6000.0*I, V1: 10.0000000000000}], [{I_V1_0: 3.8 + 3600.0*I, I_V2_0: -1.8 - 3600.0*I, V1: 10.0000000000000, V2: 4.00000000000000}]
#print(c.show())

c281= Circuit() #2.71 Real Q issss correct !!!!!!
c281.add(CurrentSource(0,1,12))
c281.add(Resistor(1,2,6))
c281.add(Resistor(0,1,12))
c281.add(Resistor(0,2,12))
c281.add(Resistor(0,2,12))
print(c281.solve('c281')) #for c281 --> [{V1: -72, V2: -36}]///[]

d= Circuit()         #is correct (:
d.add(Resistor(0,1,2000)) # the circuit model in prbelem 5.32 in book basic engineering circet analysis page 255
d.add(Resistor(0,2,4000))
d.add(Resistor(0,3,2000))
d.add(VoltageSource(2,3,12))
d.add(VoltageSource(2,1,6))
print(d.solve('d')) #for d --> [{I_V2_1: -3/5000, I_V2_3: 3/1250, V1: 6/5, V2: 36/5, V3: -24/5}]///[[{I_V2_1: 3*V3/4000 + 3/1000, I_V2_3: -V3/2000, V1: -3*V3/2 - 6, V2: V3 + 12}], [{I_V2_1: -3/5000, I_V2_3: 3/1250, V1: 6/5, V2: 36/5, V3: -24/5}]]

c270= Circuit() #2.70
c270.add(VoltageSource(0,1,15))   
c270.add(Resistor(0,1,10))
c270.add(Resistor(1,2,16))
c270.add(Resistor(0,2,8))
print(c270.solve('c270')) #for c270 --> [{I_V0_1: 17/8, V1: -15, V2: -5}]///[[{I_V0_1: 17/8, V1: -15, V2: -5}]]

ex=Circuit()
ex.add(VoltageSource(0,1,15))
ex.add(CurrentSource(1,4,5))
ex.add(Resistor(1,2,1))
ex.add(Resistor(2,3,1))
ex.add(Resistor(3,4,1))
ex.add(Resistor(4,0,1))
print(ex.solve('ex')) #for ex --> [{I_V0_1: 15/2, V1: -15, V2: -25/2, V3: -10, V4: -15/2}]///[[{I_V0_1: 15/2, V1: -15, V2: -25/2, V3: -10, V4: -15/2}]]

# c270= Circuit() #2.68
# c270.add(VoltageSource(0,1,6))
# c270.add(Resistor(0,1,12))
# c270.add(Resistor(1,2,2))
# c270.add(Resistor(0,2,4))
# print(c270.solve())

# c270= Circuit() #2.67
# c270.add(VoltageSource(0,1,12))
# c270.add(Resistor(1,2,2))
# c270.add(Resistor(0,2,6))
# c270.add(Resistor(2,3,8))
# c270.add(Resistor(0,3,4))
# print(c270.solve())

# c270= Circuit() #
# c270.add(VoltageSource(0,1,12))
# c270.add(VoltageSource(2,1,12))
# c270.add(Resistor(1,2,2))
# c270.add(Resistor(0,2,6))
# c270.add(Resistor(2,3,8))
# c270.add(Resistor(0,3,4))
# print(c270.solve())

# c281= Circuit() #2.81
# c281.add(VoltageSource(0,1,12))
# c281.add(Resistor(1,2,8))
# c281.add(Resistor(0,2,4))
# print(c281.solve())

# c281= Circuit() #2.80
# c281.add(VoltageSource(0,1,100))
# c281.add(Resistor(1,2,20))
# c281.add(Resistor(2,0,100))
# c281.add(Resistor(1,3,30))
# c281.add(Resistor(3,0,50))
# print(c281.solve())

# c281= Circuit() #2.72
# c281.add(VoltageSource(4,0,12))
# c281.add(Resistor(0,1,4))
# c281.add(Resistor(1,2,12))
# c281.add(Resistor(0,2,16))
# c281.add(Resistor(2,3,4))
# c281.add(Resistor(3,0,6))
# c281.add(Resistor(3,4,2))
# print(c281.solve())

# c281= Circuit() #2.71
# c281.add(VoltageSource(0,1,12**2))
# c281.add(Resistor(1,2,6))
# c281.add(Resistor(0,1,12))
# c281.add(Resistor(0,2,12))
# c281.add(Resistor(0,2,12))
# print(c281.solve())


# c281= Circuit() #2.107
# c281.add(VoltageSource(3,2,24))
# c281.add(Resistor(0,2,12))
# c281.add(Resistor(0,3,12))
# c281.add(Resistor(2,1,12))
# c281.add(Resistor(3,1,12))
# c281.add(Resistor(0,1,12))
# c281.add(Resistor(0,1,12))
# print(c281.solve())

# c281= Circuit() #2.105
# c281.add(VoltageSource(2,3,21))
# c281.add(Resistor(0,1,12))
# c281.add(Resistor(0,3,2))
# c281.add(Resistor(0,2,18))
# c281.add(Resistor(2,1,6))
# c281.add(Resistor(3,1,6))
# print(c281.solve())

# c281= Circuit() #2.102 Error!!! rebrsint curent sourse
# c281.add(VoltageSource(2,3,12))
# c281.add(VoltageSource(4,1,6))
# c281.add(Resistor(3,4,2))
# c281.add(Resistor(2,1,12))
# c281.add(Resistor(0,2,1))
# print(c281.solve())   

# c281= Circuit() #2.102 Error!!! rebrsint curent sourse
# c281.add(VoltageSource(2,3,12))
# c281.add(VoltageSource(4,1,6))
# print(c281.solve()) 




import time
print(f'it take {time.process_time()}sec to finish')  # to measure the needed time to Execute 



