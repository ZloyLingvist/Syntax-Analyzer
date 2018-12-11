############## Вспомогательные правила #################
pr=[] ##массив предлогов
rules=[]
pr_set=[]

##индексы
x=6 ##родитель
y=7 ##тип связи

def find_padej(index,conll): #ищем падеж
        s=''
        case_param=['nom','gen','dat','acc','ins','loc']
        
        for i in range(6):
            if case_param[i] in conll[index][4]:
                s=case_param[i]
                break
        
        return s


def link(arr,parent,type_of_link,index): ###устанавливаем связь
    if parent=="_":
        parent="-1"
    if arr[index][y]=="_":
        arr[index][x]=str(parent+1)
        arr[index][y]=type_of_link

  
#################### Основные функции #######################

def function_1(conll,row,i,index,st,st2,t,f_1,param,pr):
    fl_check=0
   
    if conll[i][y]!="_":
        return 0

    if param==1:
        if conll[t][3]==st[index] or conll[t][y]==st[index]:
            if row[5]=="same_padej":
               str1=find_padej(i,conll)
               if str1 in conll[t][4]:
                    fl_check=1

            if row[5]!="same_padej":
                fl_check=1

            if fl_check==1:
                if f_1==1:
                    link(conll,t,st2[index],i)
                    return 1
                if f_1==0.5:
                    link(conll,t,row[2],i)
                    return 1
            
    if param==2:
        if row[4]=="PR":
            for k in range(len(row)):
                if pr[k][0]==conll[t][1]: ## нашли данный предлог в таблице
                    if pr[k][1] in conll[i][4] or pr[k][2] in conll[i][4]:
                        link(conll,t,row[2],i)
                        
        if row[4]=="table_value": ## пока только для таблицы с предлогами
            if conll[t][y]=="root":
                link(conll,t,"obst",i)
            else:
                link(conll,t,"atrib",i)
                                  
        if row[4]!="PR" and row[4]!="table_value":
            link(conll,t,row[2],i)
            

        return 1

    
def right_left_search(conll,row,i,st,st2,f_1,t,pr):
    value=0
    str1=''

    if f_1>=0.5:
        if conll[t][3]==st[0]:
            value=function_1(conll,row,i,0,st,st2,t,f_1,1,pr)
            return value
                   
        if conll[t][3]==st[1]:
            value=function_1(conll,row,i,1,st,st2,t,f_1,1,pr)
            return value
                                              
        if conll[t][y]=="root":
            if f_1>=0.5 and conll[i][y]=="_":
                if f_1==0.5:
                    link(conll,t,row[2],i)
                    return 1
                
                if f_1==1:
                    if st2[1]=="1-kompl":
                      conll[i][y]=st2[0]
                      return 1
                    
                    if st2[1]=="atrib":
                        conll[i][y]=st2[1]
                        return 1
                        

def function_2(conll,row,opt,st,st2,f_1,t,i,pr): ### для поиска влево и вправо
    if opt==3:
        value=right_left_search(conll,row,i,st,st2,f_1,t,pr)
                                                       
    if opt==2:
        if (conll[t][3]==row[4] and row[4] in conll[t][4]):
            value=function_1(conll,row,i,0,[],[],t,f_1,2,pr)
                                                                           
    if opt==1 or opt==0:    
        if (conll[t][3]==row[4] or conll[t][y]==row[4]): ## поиск по части речи
            value=function_1(conll,row,i,0,[],[],t,f_1,2,pr)          


def search(i,conll,row,pr):
    root=0
    opt=0
    value=0
    st2=''
    f_1=0 # 0.5 - тип связи с выбором; 1 тип связи и тип отношения с выбором
    check_flag=0
    meet_arr=[]
    check_comp=0

    for j in range(len(row)): ##
        if row[j]=="if":
                for k in range(j+1,len(row)):
                    if "pos" in row[k]:##позиция в таблице
                        if i!=(int(row[k+1])-1):
                            return 0
                    if "значение" in row[k]:
                        for m in range(k+1,len(row)):
                            if "параметр" in row[m] or "стоп" in row[m] or "конец" in row[m] or "prev" in row[m] or "next" in row[m]:
                                break

                            ## проверить значение со словом как есть
                            if check_comp==0 and (conll[i][1]==row[m] or conll[i][2]==row[m]):
                                check_comp=1    

                        if check_comp==0:
                            return 0

                    if "стоп" in row[k]: ## указание параметра который нельзя встретить
                        if row[k+1]=="root":
                            for m in range(len(conll)):
                                if conll[m]==['\n']:
                                    continue
                                
                                if conll[m][y]=="root": 
                                    meet_arr.append(conll[m][y])
                                    break
                        else:
                            meet_arr.append(row[k+1]) ## пока ограничение на часть речи

                    if "параметр2" in row[k]:
                        if row[k-2]=="prev":
                            if not row[k+1] in conll[i-1][4]:
                                return 0
                        if row[k-2]=="next":
                            if not row[k+1] in conll[i+1][4]:
                                return 0
                                         
                        
                    if "параметр" in row[k] or "prev" in row[k] or "next" in row[k]:
                        if "!" in row[k]: ## параметра быть не должно
                            if "prev" in row[k] and row[k+1]==conll[i-1][3]:
                                return 0

                            if i<(len(conll)-1):
                                if "next" in row[k] and row[k+1]==conll[i+1][3]:
                                    return 0
                                
                            if row[k+1] in conll[i][4]:
                               if conll[i][3]!=conll[i][4]: #не применять если есть совпадение части речи и морфологии
                                    return 0
                                
                        if not "!" in row[k]:
                             if "next" in row[k] and i<(len(conll)-1):
                                 if conll[i+1][3]!=row[k+1]:
                                    return 0
                                    
                             if "prev" in row[k] and i>0:
                                 if "prev" in row[k] and row[k+1]=="same_ps": ##однородные
                                    if i>=1 and conll[i][3]!=conll[i-1][3]:
                                        return 0

                                 if (row[k+1]=="root" and i>=1 and conll[i-1][y]!=row[k+1]):
                                     return 0
                                    
                                 if (row[k+1]!="root"):
                                     if i>=1 and (conll[i-1][3]!=row[k+1]):
                                        return 0


    
    if '|' in row[2]:
        st2=str(row[2]).split('|')
        f_1=0.5 ##$ если возможен выбор одного из двух типов связи
        
    ###### ищем родителя ####
    if row[2]=="root":
        link(conll,int(row[3])-1,row[2],i)
        
    if row[3]=="linkroot":
        conll[i][x]=row[3]
        
    if row[3]=="prev": ## если указано, что родитель предыдущее слово. Применимо например для запятой
        link(conll,i-1,row[2],i)
            
    if row[3]=="next": ## если указано, что родитель последующее слово.
        link(conll,i+1,row[2],i)

    if row[3]=="left" or row[3]=="right" or row[3]=="everywhere":
        if '|' in row[4]: ## тип родителя с выбором с выбором
            st=str(row[4]).split('|')
            opt=3
            f_1=f_1+0.5

        if opt==0 and row[5]=="-": ### параметр не важен
            opt=1
        if opt==0 and row[5]!="-" and row[5]!="root" and row[5]!="same_padej":
            opt=2
        if row[3]=="everywhere":
            for m in range(len(conll)):
                if conll[m]==['\n']:
                    continue
                if opt==3:
                    function_2(conll,row,opt,st,st2,f_1,t,i,pr)
                if opt==2:
                    function_2(conll,row,opt,[],[],f_1,t,i,pr)
                if opt==1 or opt==0:
                    if row[4]=="table_value":
                            if row[0]=="PR":
                                    for l in range(len(pr)):
                                        if (conll[i][1]==pr[l][0]): ## нашли предлог в словаре
                                           if 'root' in pr[l][3]:
                                               for u in range(len(conll)):
                                                   if conll[u]==['\n']:
                                                        continue
                                                   if conll[u][y]=="root":
                                                       value=function_1(conll,row,i,0,[],[],u,f_1,2,pr)
                                                       
                                                    
                                           if 'p' in pr[1][3]:
                                               t=i-1
                                               while(t>=0):
                                                   if (conll[t][3]=="S" or conll[t][y]=="root"):   
                                                       break
                                                    
                                                   t=t-1

                                               value=function_1(conll,row,i,0,[],[],t,f_1,2,pr)
                                                                             
                                
                    if (conll[m][3]==row[4] or conll[m][y]==row[4]): ## поиск по части речи
                            value=function_1(conll,row,i,0,[],[],m,f_1,2,pr)
                                
                            
                    
        if row[3]=="left":
             if row[4]=="copy_prev":
                        t=i-1
                        while(t>=0):
                            if (conll[t][3]==conll[i][3]): ##пока для существительного
                                if conll[t][3]=="S":
                                    st4=find_padej(i,conll)
                                    if st4 in conll[t][4]:
                                        if conll[t][x]=="_":
                                                conll[t][x]="-2"
                                        link(conll,int(conll[t][x])-1,conll[t][y],i)
                                        break
                                else:
                                    if conll[t][x]=="_":
                                        conll[t][x]="-2"
                                    link(conll,int(conll[t][x])-1,conll[t][y],i)
                                    break

                            t=t-1
             t=i-1
             while(t>=0):
                    if conll[t]==['\n']:
                        t=t-1
                        continue

                    if len(meet_arr)>0 and (conll[t][3]==meet_arr[0] or conll[t][y]==meet_arr[0]):
                        break
                       
                    if opt==3:
                        function_2(conll,row,opt,st,st2,f_1,t,i,pr)
                    else:
                        function_2(conll,row,opt,[],[],f_1,t,i,pr)
                            
                    t=t-1

        if row[3]=="right":
                    t=i
                    while(t<len(conll)):
                        if conll[t]==['\n']:
                            t=t+1
                            continue

                        if opt==3:
                            function_2(conll,row,opt,st,st2,f_1,t,i,pr)
                        else:
                            function_2(conll,row,opt,[],[],f_1,t,i,pr)
                            
                        t=t+1

                                        
        #if row[8]!="prev" and row[8]!="left" and row[8]!="next" and row[8]!="right" and row[8]!="everywhere":
            #conll[i][5]=row[8]

                   
    return value                
                
    
def analyzing(str2,conll,pr):
    find_name=[]
    find_param=[]
    
    row=str2[0].split(' ')
    value=0
    
    if "#" in row[0]: #не применять правило
        return 0

    ######## Начало правила. К чему будем применять правило ? ###

    if '|' in row[0]: # если правило может быть применимо к 2-м частям речи, то они разделены :
        st2=str(row[0]).split('|')
        for k in range(len(st2)):
            find_name.append(st2[k])
    else:
        if row[0]!="all":
            find_name.append(row[0])
                
            if row[0]=="all":
                for i in range(len(conll)):
                    if conll[i]==['\n']: ## пропуск пустых строк
                        continue

                    if not conll[i][x].isnumeric(): ## пока проверка чтобы родитель на момент применения правила не был проставлен
                        find_name.append(conll[i][1])

    ###### Возможно, что для правила важен определенный параметр (падеж, число и т.д.)
            
    find_param.append(row[1])
    for i in range(len(conll)):    
        if conll[i]==['\n']: ## пропуск пустых строк
            continue
        for j in range(len(find_name)):
            for k in range(len(find_param)):
                    if find_param[k]=="-": ## параметр не важен ищем совпадения по части речи
                        if conll[i][3]==find_name[j] or conll[i][1]==find_name[j] or conll[i][8]==find_name[j]:
                            value=search(i,conll,row,pr)
                                
                    else: ## если есть параметр поиска
                        if "!" in row[1]: # правило не применимо при наличии данного параметра
                            if conll[i][3]==find_name[j] and not find_param[k] in conll[i][4]: ## ищем совпадения по части речи и отсутствию параметру
                                value=search(i,conll,row,pr)
                                    
                        else:
                            if conll[i][3]==find_name[j] and find_param[k] in conll[i][4]: ## ищем совпадения по части речи и параметру
                                value=search(i,conll,row,pr)

                            
    ### пост-обработка ##
    for i in range(len(conll)):
        if conll[i]==['\n']:
            continue

        if conll[i][y]=="root":
            for t in range(len(conll)):
                if conll[t]==['\n']:
                    continue
                
                if conll[t][x]=="linkroot":
                    conll[t][x]=str(i+1)
                    conll[t][y]=row[2]
                                        
    return 0
            

def pravilo_primenitel(tmp,rules,pr):
    
    for i in range(len(rules)):
        if rules[i]==['\n']:
            continue
        analyzing(rules[i],tmp,pr)

    return tmp

