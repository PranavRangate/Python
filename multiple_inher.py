class Physics:
        p_marks=70
            
class Chemestry:
        c_marks=80
            
class Maths:
        m_marks=90
    
class PCM(Physics,Chemestry,Maths):
    per = (Physics.p_marks+Chemestry.c_marks+Maths.m_marks)/3
    
d1 = PCM()
print(d1.per)