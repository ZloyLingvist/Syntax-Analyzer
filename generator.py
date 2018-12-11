from collections import Counter

arr=[]

def find_padej(index,conll): #ищем падеж
        s=''
        case_param=['nom','gen','dat','acc','ins','loc','pr']
        
        for i in range(6):
            if case_param[i] in conll[index][4]:
                s=case_param[i]
                break
        
        return s

def returnparam(arr,i,j):
        case_param=['nom','gen','dat','acc','ins','loc','mestn']
        s_param=['anim','pl','sg','pr']
        v_param=['indic','pl','praes','ipf','3p','inpraes','strad']
        partcp_param=['ipf','inpraes','brev','praet','strad']
        a_param=['pl','sg','brev','pr']
        ps=arr[i][j][3]

        s=''
        save=''
        was=0
        
        if ps=="S" or ps=="A" or ps=="PARTCP" or ps=="SPRO":
                for m in range(6):
                    if case_param[m] in arr[i][j][4]:
                        s=case_param[m]
                                
        if ps=="S" or ps=="SPRO":
                for m in range(len(s_param)):
                      if s_param[m] in arr[i][j][4]:
                        b='/'+s_param[m]
                        was=was+1
                      

                if was==0:
                   return s
                if was>0:
                    s=s+b
                    return s

        if ps=="A":
                save="/"
                for m in range(len(a_param)):
                      if a_param[m] in arr[i][j][4]:
                        s=a_param[m]
                        b='/'+a_param[m]
                        was=was+1
                      

                if was==0:
                   return s
                if was>0:
                    s=s+b
                    return s
                        

        if ps=="PARTCP":
                save="/"
                for m in range(len(partcp_param)):
                      if partcp_param[m] in arr[i][j][4]:
                        s=partcp_param[m]
                        b='/'+partcp_param[m]
                        was=was+1
                      

                if was==0:
                   return s
                if was>0:
                    s=s+b
                    return s
        

        if ps=="V":
              for m in range(len(v_param)):
                      if v_param[m] in arr[i][j][4]:
                         s=v_param[m]
                         b='/'+v_param[m]
                         was=was+1
                      
              if was==0:
                   return s
              if was>0:
                   s=s+b
                   return s

        return ps.lower()
                

def create_template(p,rule):
     tmp_templ=[]
     templ=[]
     str1=''
     
     for i in range(len(rule)):
             tmp_templ.append('start\n')
             templ.append(tmp_templ)
             tmp_templ=[]
             
             for j in range(len(rule[i])):
                     tmp_templ.append(rule[i][j][3])
                     tmp_templ.append('\t')

                     
             tmp_templ.append('_\n')
             templ.append(tmp_templ)
             tmp_templ=[]

             ###### параметры пока пусто ##########
             
             for j in range(len(rule[i])):
                     if (p==1):
                             if(rule[i][j][7]=="kvaziagent" or rule[i][j][7]=="opred" or rule[i][j][7]=="1-kompl" or rule[i][j][7]=="predl"):
                                     str1=str1+str(rule[i][j][7])+'\t'
                             else:
                                    str1=str1+'_'+'\t' 
                     if (p==0):
                             str1=str1+'_'+'\t'
                                    
                     
             ###########################

             st=''
             for j in range(len(rule[i])):
                     l=returnparam(rule,i,j)
                     if l=='':
                        st=st+str(rule[i][j][3]).lower()
                     else:
                        st=st+l
                        
                     st=st+'\t'

             str1=str1+st
             st=''

             for j in range(len(rule[i])):
                     value=int(rule[i][j][6])-int(rule[i][j][0])
                     if value>2 or value<-2:
                             value='_'
                             st=st+value
                     else:
                             if int(value)==-2 or int(value)==-1:
                                     st=st+str(value)
                             if int(value)==1 or int(value)==2:
                                     st=st+'+'+str(value)
                     st=st+'\t'

             str1=str1+st
             st=''

             for j in range(len(rule[i])):
                     val=int(rule[i][j][0])-int(rule[i][j][6])
                     if val>2 or val<-2:
                             value='_'
                     else:
                             value=rule[i][j][7]
                        
                     st=st+value
                     st=st+'\t'

             str1=str1+st
             

             
             ###############################

             tmp_templ.append(str1)
             tmp_templ.append('_\n')
             templ.append(tmp_templ)
             tmp_templ=[]
             str1=''
             
             tmp_templ.append('end\n')
             tmp_templ.append('\n')
             templ.append(tmp_templ)
             tmp_templ=[]

     return templ
     ############################################


def generate_big_templates(p,arr):
     rule=[]
     tmp_rule=[]

     tmp_num=[]
     tmp_super_num=[]

     for m in range(len(arr)):
             if arr[m]==['\n']:
                     continue

             if "punc" in arr[m][7]:
                        break
             if m==0:
                        if int(arr[m][6])==1:
                              tmp_num.append(arr[m][0])
                              tmp_num.append(arr[m][0])

                      
             if m>1:
                        if int(arr[m][6])-int(arr[m-1][6])==1:
                                if arr[m][6]==arr[m-1][0]:
                                        tmp_num.append(arr[m-1][0])
                                
                                if arr[m-1][6]==arr[m-2][0]:
                                       tmp_num.append(arr[m-2][0])

                                tmp_num.append(arr[m][0])
                       

                        if int(arr[m][6])-int(arr[m-1][6])!=1:
                                for j in range(len(tmp_num)):
                                        if  arr[m+1][6]==tmp_num[j]:
                                                tmp_num.append(arr[m][0])
                                                tmp_num.append(arr[m+1][0])
                                                m=m+2
                                                break
                                
                                        if j==len(tmp_num)-1:
                                                tmp_super_num.append(tmp_num)
                                                tmp_num=[]
                                        
                
     for j in range(len(tmp_super_num)):
             if len(tmp_super_num[j])==0:
                     continue
             tmp_super_num[j]=list(set(tmp_super_num[j]))
             tmp_super_num[j].sort(key=int)
   
     for i in range(len(tmp_super_num)):
             if len(tmp_super_num[i])==0:
                     continue
             for j in range(len(tmp_super_num[i])):
                     tmp_rule.append(arr[int(tmp_super_num[i][j])-1])

             rule.append(tmp_rule)
             tmp_rule=[]

     #################################
    
     templ=create_template(p,rule)
     return templ      
     

def generate_little_templates(p,arr):
     tmp_num=[]
     tmp_super_num=[]

     tmp_rule=[]
     rule=[]
     
     for m in range(len(arr)-1):
             if arr[m]==['\n']:
                     continue
             if arr[m][6]==arr[m+1][0]:
                     tmp_num.append(m+1)
                     tmp_num.append(m+2)
                     tmp_super_num.append(tmp_num)
                     tmp_num=[]

     for i in range(len(tmp_super_num)):
             if len(tmp_super_num[i])==0:
                     continue
             for j in range(len(tmp_super_num[i])):
                     tmp_rule.append(arr[int(tmp_super_num[i][j])-1])

             rule.append(tmp_rule)
             tmp_rule=[]

     #################################
     templ=create_template(p,rule)
     return templ  


def parametr(param,p,n):
        a=[]
       
        for i in range(n):
             try:
                if param==1:
                        a.append(generate_little_templates(p,arr[i]))
                if param==2:
                        a.append(generate_big_templates(p,arr[i]))
                
             except:
                print(i)

        if param==1:
                f=open("template_corp.txt","w",encoding="utf-8")
        if param==2:
                f=open("template_corp.txt","a",encoding="utf-8")


        a.sort()
        
        for i in range(len(a)):
                if a[i]!=None:
                        for j in range(len(a[i])):
                                for k in range(len(a[i][j])):
                                        f.write(a[i][j][k])
        
        f.close()
        a=[]

################################################
        
def creat(name,arr,parent,mode):
        mystr=''
        param=''
        parent_link=''
        n_param=[]
        end=[]

        S_param=['nom','gen','dat','acc','ins','loc','mestn','pr']
        S_end=['ение']
        V_param=['indic']
        A_param=['nom','gen','dat','acc','ins','loc','brev','pr']
        PARTCP_param=['ipf','inpraes','brev','praet','strad','nom','gen','dat','acc','ins','loc','mestn']

        if name=="S":
                n_param=S_param
                end=S_end
        if name=="SPRO":
                n_param=S_param
                end=[]
        if name=="V":
                n_param=V_param
                end=[]
        if name=="A":
                n_param=A_param
                end=[]

        if name=="PARTCP":
                n_param=PARTCP_param
                end=[]
        
        if mode==1:                                   
                for t in range(len(n_param)):
                        ####### Параметр ######
                        if n_param[t] in arr[4]:
                                if len(param)==0:
                                        param=n_param[t]
                                else:
                                        param=param+'/'+n_param[t]

                if len(param)==0:
                        param="_"
        
                mystr=mystr+param


        if mode==2:
                mystr=mystr+'\t'
                for t in range(len(end)):
                        ####### Окончание #####
                        if end[t] in arr[2]:
                                mystr=mystr+end[t]+'\t'
                                break
                                                
                        if t==len(end)-1:
                                 mystr=mystr+'_'+'\t'

                if len(end)==0:
                        mystr=mystr+'_'+'\t' 
                                 
                for t in range(len(n_param)):
                        ####### Параметр ######
                        if n_param[t] in arr[4]:
                                if len(param)==0:
                                        param=n_param[t]
                                        #param=arr[4]
                                else:
                                        param=param+'/'+n_param[t]
                                       # param=arr[4]
                                        break

                if len(param)==0:
                        param="_"
        
                mystr=mystr+param
        
        return mystr;


		
def creator(arr,link,ogranich):
        tmp=[]
        mystr=''
        param=''
        p=1
       
        for i in range(len(arr)):
                for j in range(len(arr[i])):
                        if arr[i][j][7]==link:
                                mystr=arr[i][j][3]+'\t'
                                if arr[i][j][3]=="S":
                                        #mystr=mystr+creat("S",arr[i][j],arr[i],1)
                                        mystr=mystr+arr[i][j][4]
                                        
                                if arr[i][j][3]=="V":
                                        #mystr=mystr+creat("V",arr[i][j],arr[i],1)
                                        mystr=mystr+arr[i][j][4]

                                if arr[i][j][3]=="A":
                                        #mystr=mystr+creat("A",arr[i][j],arr[i],1)
                                        mystr=mystr+arr[i][j][4]

                                if arr[i][j][3]=="PARTCP":
                                        #mystr=mystr+creat("PARTCP",arr[i][j],arr[i],1)
                                        mystr=mystr+arr[i][j][4]
                                        
                                if arr[i][j][3]!="V" and arr[i][j][3]!="S" and arr[i][j][3]!="A" and arr[i][j][3]!="PARTCP":
                                        mystr=mystr+'_'

                                for k in range(len(arr[i])):
                                        if arr[i][j][6]=="0":
                                                mystr=mystr+'\t'+'_'
                                                break
                                        if arr[i][j][6]==str(int(arr[i][k][0])):
                                                if link=="predl":
                                                        mystr=mystr+'\t'+arr[i][k][2]
                                                else:
                                                        mystr=mystr+'\t'+arr[i][k][3]

                                                mystr=mystr+creat(arr[i][k][3],arr[i][k],arr[i],2)
                                               
                                                
                                                if int(arr[i][j][0])-int(arr[i][j][6])>1:
                                                        if p==0:
                                                                mystr=mystr+'\t'+'left'
                                                        if p==1:
                                                                mystr=mystr+'\t'+'left'+'\t'
                                                                t=int(arr[i][j][0])
                                                                k=j
                                                                while(t>=int(arr[i][j][6])):
                                                                        if t==int(arr[i][j][6]):
                                                                                  mystr=mystr+arr[i][k][3]
                                                                        else:
                                                                                  mystr=mystr+arr[i][k][3]+'/'
                                                                        t=t-1
                                                                        k=k-1

                                                                
                                                                mystr=mystr+'\t'
                                                                t=int(arr[i][j][0])
                                                                k=j
                                                                while(t>=int(arr[i][j][6])):
                                                                        if t==int(arr[i][j][6]):
                                                                                  mystr=mystr+arr[i][k][7]
                                                                        else:
                                                                                mystr=mystr+arr[i][k][7]+'/'
                                                                        t=t-1
                                                                        k=k-1
                
                                                                #mystr=mystr+'\t'+arr[i][k][7]
                                                        break
                                                
                                                if int(arr[i][j][0])-int(arr[i][j][6])==1:
                                                        if p==0:
                                                                mystr=mystr+'\t'+'prev'
                                                        if p==1:
                                                                mystr=mystr+'\t'+'prev'+'\t_\t_'
                                                        
                                                        break
                                                if int(arr[i][j][0])-int(arr[i][j][6])<1:
                                                        if p==0:
                                                                mystr=mystr+'\t'+'right'
                                                        if p==1:
                                                                mystr=mystr+'\t'+'right'+'\t'
                                                                t=int(arr[i][j][0])
                                                                k=j
                                                                while(t<=int(arr[i][j][6])):
                                                                        if t==int(arr[i][j][6]):
                                                                                  mystr=mystr+arr[i][k][3]
                                                                        else:
                                                                                  mystr=mystr+arr[i][k][3]+'/'
                                                                        t=t+1
                                                                        k=k+1

                                                                
                                                                mystr=mystr+'\t'
                                                                t=int(arr[i][j][0])
                                                                k=j
                                                                while(t<=int(arr[i][j][6])):
                                                                        if t==int(arr[i][j][6]):
                                                                                  mystr=mystr+arr[i][k][7]
                                                                        else:
                                                                                  mystr=mystr+arr[i][k][7]+'/'
                                                                        t=t+1
                                                                        k=k+1
                
                                                        break
                                                
                                                if int(arr[i][j][0])-int(arr[i][j][6])==-1:
                                                        if p==0:
                                                                mystr=mystr+'\t'+'next'
                                                        if p==1:
                                                                mystr=mystr+'\t'+'next'+'\t_\t_'
                                                        #mystr=mystr+'\t'+arr[i][k][7]
                                                        break
                                                
                                row=mystr.split('\t')
                                if len(row)>2:
                                        tmp.append(mystr+'\t'+'_'+'\n')
                                mystr=''
                                param=''


       
        c = Counter(tmp).most_common()
       
        l = []
        l.append(link+'\t_'+'\n'+'{\n')
        
        for key in sorted(c):
                str1=str(key[1])+'\t'+str(key[0])
                if key[1]<ogranich:
                        str1=''
                        continue
                
                l.append([str1])
                str1=''

       
        l.append(['}'])
        return l

       
def write(arr,link,ogranich):		
        ans=[]
        arr_temp=[]
        arr_t=[]
        ans=creator(arr,link,ogranich)
        ans=ans+['\n']

        f=open(link+".txt","w",encoding="utf-8")
        for i in range(len(ans)):
                for j in range(len(ans[i])):
                        f.write(ans[i][j])
       
        f.close()

        f=open(link+".txt","r",encoding="utf-8")
        for line in f:
                row=line.split('	')
                if row==['}\n']:
                        arr_t.append(arr_temp)
                        arr_temp=[]
                        continue
                
                arr_temp.append(row)

        f.close()

        for i in range(2,len(arr_t[0])-1):
                for j in range(i+1,len(arr_t[0])):
                               if int(arr_t[0][i][0])<int(arr_t[0][j][0]):
                                   x = arr_t[0][i];
                                   arr_t[0][i] = arr_t[0][j];
                                   arr_t[0][j] = x
                               
        f=open(link+".txt","w",encoding="utf-8")
        for i in range(len(arr_t)):
                               for k in range(len(arr_t[i])):
                                       for m in range(len(arr_t[i][k])):
                                             if m==0:
                                                       f.write(arr_t[i][k][m])
                                             else:
                                                       f.write('\t'+arr_t[i][k][m])

        f.write('}\n')
        f.close()
        


def generate(p,n,name):
        arr_temp=[]
        f=open("my_test.txt","r",encoding="utf-8")
        for line in f:
                row=line.split('	')
                if row==['\n']:
                       arr.append(arr_temp)
                       arr_temp=[]
                       continue
                arr_temp.append(row)

        f.close()

        if name=="all":
                parametr(1,p,n)
                parametr(2,p,n)
                write(arr,"predl",10)
                write(arr,"opred",30)
                write(arr,"1-kompl",10)
                write(arr,"kvaziagent",10)
                write(arr,"root",2)
                write(arr,"predic",10)
                write(arr,"atrib",10)
                write(arr,"kolichest",10)
                write(arr,"vspom",10)
                write(arr,"primikat",10)

        if name=="predl":
                write(arr,"predl",2)
        if name=="opred":
                write(arr,"opred",2)
        if name=="1-kompl":
                write(arr,"1-kompl",2)
        if name=="kvaziagent":
                write(arr,"kvaziagent",2)

          
#generate(0,300,"1-kompl")        
