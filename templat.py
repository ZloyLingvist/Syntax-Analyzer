work=[]

def checker(str1,str2,str3):
    if str2=="S":
        for i in range(len(str1)):
            if str1[i]!=str3[i]:
                if str1[i]=='n' or str1[i]=='f' or str1[i]=='m':
                    continue
                return 0

        return 1

def check(m,arr,rule,block_length,conll):
    rule_tmp=[]
    rule_svod=[]
    mark=[]

    ############################################

    for i in range(len(rule)):
        rule_tmp.append(rule[i])
        if (i% block_length==(m-1) and i!=0):
            rule_svod.append(rule_tmp)
            rule_tmp=[]

    for i in range(len(arr)):
        if arr[i][7]!=rule_svod[0][i] and rule_svod[0][i]!="_": ## проверили тип связи
            return []
        
        if "/" in  rule_svod[1][i]:
            str0=str(rule_svod[1][i]).split('/')
            for j in range(len(str0)):
                if not str0[j] in arr[i][4] and len(str0[j])>1: 
                    return []
        else:
            if not rule_svod[1][i] in arr[i][4] and rule_svod[1][i]!="_":
                return []
            
        if rule_svod[2][i]!="_":
            if "root" in rule_svod[2][i]: ##не работает
                arr[i][6]="0"
            else:
                arr[i][6]=str(int(arr[i][0])+int(rule_svod[2][i]))
                
        if rule_svod[3][i]!="_":
            if "|" in rule_svod[3][i]: ## | совпадение по морфологии с родителем
                str1=str(rule_svod[3][i]).split('|')
                if (checker(conll[int(arr[i][6])-1][4],arr[i][3],arr[i][4]))==1:
                    arr[i][7]=str1[1]
                    work.append(rule_svod)
                else:
                    arr[i][7]=str1[0]
                    work.append(rule_svod)
            else:
                arr[i][7]=rule_svod[3][i]
                work.append(rule_svod)
                
            
    ############################################
    for i in range(len(conll)):
        if conll[i][0]==arr[0][0]:
            for j in range(len(arr)):
                conll[i+j]=arr[j]
    
    return 1

def temp2(conll,tmp_arr):
    flag=1
    k=0
    tmp=[]
    tmp_g=[]

    block_length=len(tmp_arr[1])-1

    if block_length==1:
        return conll
    
    for i in range(len(conll)):
        if conll[i]==['\n']:
            continue
         
        ########### проверяем на очередность ######
        if (conll[i][3]==tmp_arr[1][0] or conll[i][1]==tmp_arr[1][0]):
            flag=1
            for m in range(block_length):
                if conll[i+m][3]!=tmp_arr[1][m] and conll[i+m][1]!=tmp_arr[1][m]:
                    flag=0
                    break
                
            if flag==1:
                ####### для прошедших проверку проверяем на тип связи ########
                for k in range(block_length):
                    tmp.append(conll[i+k])

    m=block_length
    for i in range(len(tmp)):
        tmp_g.append(tmp[i])
        if (i%block_length==(m-1) and i!=0):
            val=check(m,tmp_g,tmp_arr[2],block_length,conll) ## arr[2]--это строка правила
            tmp_g=[]
            
    ##################################
            
    return conll


def temp(conll,arr):
    for j in range(len(arr)):
        temp2(conll,arr[j])

    return conll,work
    
                   
