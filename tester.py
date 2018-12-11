test_1=[]
test_2=[]
test_gl=[]


def test_process(param):
    f=open("syntax.txt","r",encoding="utf-8")
    for line in f:
        row=line.split('	')
        test_1.append(row)

    f.close()

    f=open("my_test.txt","r",encoding="utf-8")

    for line in f:
        row=line.split('	')
        test_gl.append(row)
    f.close()

    for i in range(len(test_1)):
        test_2.append(test_gl[i])

    equal(param)


    only_num=1
    
    if only_num==1:
        a=0
        b=0
        m=0
        for i in range(len(test_1)):
            if test_1[i]==['\n'] or test_2[i]==['\n']:
                 continue
            if test_1[i][7]=="punc" or test_2[i][7]=="punc":
                continue

            if test_2[i][7]==param:
                b=b+1
            
            if test_1[i][6]!=test_2[i][6] and test_2[i][7]==param:
                a=a+1;

            if test_1[i][6]==test_2[i][6]:
                m=m+1;

        f=open("result.txt","w",encoding="utf-8")
        f.write(str(a)+'\n')
        f.write(str((m/b)*100)+'\n')
        f.write(str(m)+'\n')
        f.close()

    else:
        test(param)

    if param=="special_test":
         k=0
         m=0
         flag=0
         param="1-kompl"
         
         for i in range(len(test_1)):
             if test_1[i]==['\n'] or test_2[i]==['\n']:
                 continue
             if test_1[i][7]=="punc" or test_2[i][7]=="punc":
                continue

             if test_2[i][7]!=param:
                 continue

             row1=test_1[i][7].split(':')
             row2=test_1[i][6].split(':')

             for j in range(len(row1)):
                 if row1[j]==test_2[i][7] and row2[j]==test_2[i][6]:
                     m=m+1
                     break
               
             k=k+1

         print('Проверка с вариантами '+' '+str(m)+'/'+str(k)+' : '+str((m/k)*100))
        


def equal(param):
    for i in range(len(test_1)):
        if test_1[i]==['\n'] or test_2[i]==['\n']:
            continue
        if test_1[i][7]=="punc" or test_2[i][7]=="punc":
            continue
        if test_1[i]==['\n'] and test_2[i]!=['\n']:
            if param=="all":
                print('Ошибка на строке '+str(i))
            return 0
        if test_1[i]!=['\n'] and test_2[i]==['\n']:
            if param=="all":
                print('Ошибка на строке '+str(i))
            return 0
        if test_1[i]==['\n'] and test_2[i]==['\n']:
            continue
        if test_1[i][1]!=test_2[i][1]:
             if param=="all":
                 print('Ошибка на строке '+str(i)+' в файле syntax.txt\n')
                 print(str(test_1[i])+'\n')
                 print(str(test_2[i])+'\n')
             return 0



def test(param):
    error_list=[]
    k=0
    m=0
    p=0
    g=0
    c=0
    s=0
    d=0
    a=0
    b=0
    l=0
    count=0

    for i in range(len(test_1)):
        if test_1[i]==['\n'] or test_2[i]==['\n']:
            count=count+1
            continue
        if test_1[i][7]=="punc" or test_2[i][7]=="punc":
            continue

        ##################################

        if param!="all":
            if test_1[i][7]==param and test_2[i][7]!=param:
                if param!="all":
                    error_list.append('Ошибка '+str(test_1[i][6])+' Должно быть:'+str(test_2[i][6])+' Строка :' +str(i)+'\n')
 
                s=s+1

            if test_1[i][7]==param and test_2[i][7]==param:
                a=a+1

            if test_2[i][7]==param:
                b=b+1

            if test_1[i][7]==param or test_2[i][7]==param:
                l=l+1
            
            if test_2[i][7]!=param:
                continue


        ######################################

        if test_1[i][6]!=test_2[i][6] and test_1[i][7]==test_2[i][7]:
            if param!="all":
                0#error_list.append('Ошибка '+str(test_1[i][6])+' Должно быть:'+str(test_2[i][6])+' Строка :' +str(i)+'\n')
            m=m+1
            
        if test_1[i][7]!=test_2[i][7] and test_1[i][6]==test_2[i][6]:
            if param!="all":
                0#error_list.append('Ошибка '+str(test_1[i][7])+' Должно быть:'+str(test_2[i][7])+' Строка :' +str(i)+'\n')
            p=p+1

        if test_1[i][7]==test_2[i][7] and test_2[i][6]==test_1[i][6]:
            c=c+1

        if test_1[i][6]!=test_2[i][6] or test_1[i][7]!=test_2[i][7]:
            g=g+1
        
        k=k+1

        if param!="all":
            #print('1) Количество неверно поставленных связей 2) Отношение верных родителя и связи к общему числу по всем связям 3) Отношение верных связей к общему количеству связей 4) Количество верных связей 5)Количество связей в эталоне 6) Общее количество связей ')
            f=open("result.txt","w",encoding="utf-8")
            f.write(str(s)+'\n')
            #f.write(str((c/k)*100)+'\n')
            f.write(str((a/b)*100)+'\n')
            f.write(str(a)+'\n')
            f.write(str(b)+'\n')
            f.write(str(l)+'\n')
            f.close()

        if param=="all":
            f=open("result.txt","w",encoding="utf-8")
            f.write('Количество '+str(count)+'\n')
            f.write('Неверно определен только родитель '+str(m)+'/'+str(k)+'\n')
            f.write('Неверно определен только тип связи '+str(p)+'/'+str(k)+'\n')
            f.write('Неверно определен или тип связи или родитель '+str(g)+'/'+str(k)+'\n')
            f.write('Корректны и тип связи и родитель  '+str(c)+'/'+str(k)+' (Процент:'+str((c/k)*100)+')'+'\n')
            print('Корректны и тип связи и родитель  '+str(c)+'/'+str(k)+' (Процент:'+str((c/k)*100)+')'+'\n')
            f.close()

#test_process("special_test")       
        
