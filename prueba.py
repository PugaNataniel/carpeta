repro = 0
aprob = 0
promo = 0
sumanotas = 0
N = int(input("ingrese cantidad de alumnos a corregir: "))
for x in range (N):
    nota = int(input("ingrese puntaje: "))
    if nota == 0:
        print ("error")
    else:
        if nota>=1 and nota<=29:
            repro=repro+1
            sumanotas = sumanotas+1
            print ("reprobo, nota: 1 ")
        else:
            if nota>=30 and nota<=47:
                repro=repro+1
                sumanotas = sumanotas+2
                print ("reprobo, nota: 2 ")
            else:
                if nota>=48 and nota<=59:
                    repro=repro+1
                    sumanotas = sumanotas+3
                    print ("reprobo, nota: 3")  
                else:
                    if nota>=60 and nota<=65:
                        aprob=aprob+1
                        sumanotas = sumanotas+4
                        print ("aprobo, nota: 4")
                    else:
                        if nota>=66 and nota<=71:
                            aprob=aprob+1
                            sumanotas = sumanotas+5
                            print ("aprobo, nota: 5")
                        else:
                            if nota>=72 and nota<=77:
                                aprob=aprob+1
                                sumanotas = sumanotas+6
                                print ("aprobo, nota: 6")
                            else:
                                if nota>=78 and nota<=83:
                                    promo=promo+1
                                    sumanotas = sumanotas+7
                                    print ("promociona, nota: 7")
                                else:
                                    if nota>=84 and nota<=89:
                                        promo=promo+1
                                        sumanotas = sumanotas+8
                                        print ("promociona, nota: 8")
                                    else:
                                        if nota>=90 and nota<=95:
                                            promo=promo+1
                                            sumanotas = sumanotas+9
                                            print ("promociona, nota: 9")
                                        else:
                                            if nota>=96 and nota<=100:
                                                promo=promo+1
                                                sumanotas = sumanotas+10
                                                print ("promociona, nota: 10")

porcentajeR = (repro*100)/N
porcentajeA = (aprob*100)/N
porcentajeP = (promo*100)/N

print ("porcentaje de reprobados: ",porcentajeR)
print ("porcentaje de aprobados: ", porcentajeA)
print ("porcentaje promocionados: ", porcentajeP)

promedio = sumanotas/N

print ("el promedio de nota total: ",promedio)
                            
                