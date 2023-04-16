def TRB(P10,P40,P200,LL,IP):
    '''
    Classificação segundo o TRB-HRB-AASHTO

    Consulta: 
    http://www.cct.udesc.br/arquivos/id_submenu/1470/classificacao___rodoviaria___hrb.pdf
    https://www.guiadaengenharia.com/classificacao-solos/

    P10 = percentual passante na peneira n° 10
    P40 = percentual passante na peneira n° 40
    P200 = percentual passante na peneira n° 200
    LL = valor do limite de liquidez
    IP = índice de plasticidade

    * Adotar valores percentuais, não decimais (12 ao invés de 0.12 por exemplo)
    '''
    
    # Filtrar possíveis NP e NL
    if type(LL)==str or type(IP)==str:
        LL = 0
        IP = 0
    
    # Cálculo do índice de grupo (IG)
    a = P200 - 35 if 35<=P200<=75 else (0 if P200<35 else 40)
    b = P200 - 15 if 15<=P200<=55 else (0 if P200<15 else 40)
    c = LL - 40 if 40<=LL<=40 else (0 if LL<40 else 20)
    d = IP - 10 if 10<=IP<=30 else (0 if IP<10 else 20)
    IG = (0.2*a)+(0.005*a*c)+(0.01*b*d)

    # Classificação
    class_TRB = ''
    if P200<=35:
        if P10<=50:
            if P40<=30 and P200<=15 and IP<=6 and IG==0:
                class_TRB = class_TRB + 'A-1-a'
            if P40<=50 and P200<=25 and IP<=6 and IG==0 and 'A-1-a' not in class_TRB:
                class_TRB = class_TRB + 'A-1-b'
            if P40>50 and P200<=25 and IP==-1 and IG==0:
                class_TRB = class_TRB + 'A-3'
        if P10>50:
            if IP<=10:
                if LL<=40 and IG==0:
                    class_TRB = class_TRB + 'A-2-4'
                if LL>40 and IG==0:
                   class_TRB = class_TRB + 'A-2-5'
            if IP>10:
                if LL<=40 and IG<=4:
                    class_TRB = class_TRB + 'A-2-6'
                if LL>40 and IG<=4:
                    class_TRB = class_TRB + 'A-2-7'
    else:
        if IP<=10:
            if LL<=40 and IG<=8:
                class_TRB = class_TRB + 'A-4'
            if LL>40 and IG<=12:
                class_TRB = class_TRB + 'A-5'
        if IP>10:
            if LL<=40 and IG<=16:
                class_TRB = class_TRB + 'A-6'
            if LL>40 and IG<=20:
                if IP<=LL-30:
                    class_TRB = class_TRB + 'A-7-5'
                if IP>LL-30:
                    class_TRB = class_TRB + 'A-7-6'

    return class_TRB
