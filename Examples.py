from ECDA import *


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
c270.add(Resistor(0,2,8)) # 
print(c270.solve('c270')) #---> [{I_V0_1: -17/8, V1: -15, V2: -5}]

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

c281= Circuit() #2.71
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

# Other Examples you can use it  

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

# c281= Circuit() #2.102 
# c281.add(VoltageSource(2,3,12))
# c281.add(VoltageSource(4,1,6))
# c281.add(Resistor(3,4,2))
# c281.add(Resistor(2,1,12))
# c281.add(Resistor(0,2,1))
# print(c281.solve())   

# c281= Circuit() #2.102 
# c281.add(VoltageSource(2,3,12))
# c281.add(VoltageSource(4,1,6))
# print(c281.solve()) 
