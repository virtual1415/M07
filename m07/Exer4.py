# Patricio Vidal
# -*- coding: utf-8 -*-


def area_rectangle(costat1, costat2):
    a_rec = costat1 * costat2
    return a_rec


def perimetre_rectangle(costat1, costat2):
    p_rec = (costat1 * 2) + (costat2 * 2)
    return p_rec


def area_quadrat(costat):
    a_qua = costat ** 2
    return a_qua


def perimetre_quadrat(costat):
    p_qua = costat * 4
    return p_qua

opcio = "a"
while opcio != "X":
    while opcio != "A" and opcio != "P" and opcio != "X":
        print "####  Menú principal  ####"
        print "§ Calcular area (A)"
        print "§ Calcular perimetre (P)"
        print "§ Sortir (X)"
        opcio = raw_input("Escull una opcio: ")
    if opcio != "X":
        opcio2 = "a"
        while opcio2 != "Q" and opcio2 != "R":
            print "\n####     Submenú     ####"
            print "§ De quadrat (Q)"
            print "§ De rectangle (R)"
            opcio2 = raw_input("Escull una opcio: ")
        if opcio == "A" and opcio2 == "Q":
            costat = int(raw_input("\nIntrodueix el valor del costat del quadrat: "))
            print "Area del quadrat: ", area_quadrat(costat), "\n"
        elif opcio == "A" and opcio2 == "R":
            costat1 = int(raw_input("\nIntrodueix el valor del costat 1 del rectangle: "))
            costat2 = int(raw_input("Introdueix el valor del costat 2 del rectangle: "))
            print "Area del rectangle: ", area_rectangle(costat1, costat2), "\n"
        elif opcio == "P" and opcio2 == "Q":
            costat = int(raw_input("\nIntrodueix el valor del costat del quadrat: "))
            print "Perimetre del quadrat: ", perimetre_quadrat(costat), "\n"
        elif opcio == "P" and opcio2 == "R":
            costat1 = int(raw_input("\nIntrodueix el valor del costat 1 del rectangle: "))
            costat2 = int(raw_input("Introdueix el valor del costat 2 del rectangle: "))
            print "Perimetre del rectangle: ", perimetre_rectangle(costat1, costat2), "\n"
        opcio = "a"
print "Has sortit del programa"
