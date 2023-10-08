n1=int(input("entre votre première note svp : "))
n2=int(input("entre votre deuxième note svp : "))
n3=int(input("entre votre troisième note svp : "))
moyenne=(n1+n2+n3)/3
if moyenne<10 :
    print("insuffisant")
elif moyenne>=10 and moyenne<=12 :
    print("passable")
elif moyenne>=12 and moyenne<=14 :
    print("assez bien")
elif moyenne>=114 and moyenne<=16 :
    print("bien")
else :
    print("très bien")