from tester import test_process
from generator import generate
import subprocess
import math
import sys
#############

def isfloat(value):
        try:
                float(value)
                return True
        except ValueError:
                return False

tmp=[]
def skleika(myarr,p1,p2,n1,n2,n3,n4,name):
        for i in range(len(myarr[0])):
                if myarr[0][i]==['opred', '_\n'] or  myarr[0][i]==['{\n'] or  myarr[0][i]==['}\n']:
                        continue

                if myarr[0][i][1]==p1 and myarr[0][i][3]==p2:
                        for m in range(i+1,len(myarr[0])):
                                if len(myarr[0][m])<6:
                                        myarr[0][m][0]=="del"
                                        continue

                                if myarr[0][m][6]!=n3 and myarr[0][m][6]!=n4:
                                        continue

                                if myarr[0][m][0]=="del":
                                       continue
                        
                                if myarr[0][m][1]!=p1 or myarr[0][m][3]!=p2:
                                       continue                       
                        
                                if myarr[0][m][6]==n3 or myarr[0][m][6]==n4:
                                        if not myarr[0][m][2] in myarr[0][i][2] and myarr[0][m][2]!="_" :
                                                myarr[0][i][2]=myarr[0][i][2]+myarr[0][m][2]+'/'
                                       
                                        if not myarr[0][m][5] in myarr[0][i][5] and myarr[0][m][5]!="_" :
                                               myarr[0][i][5]=myarr[0][i][5]+myarr[0][m][5]+'/'

                                        myarr[0][i][6]=name+"\t_\n"
                                        myarr[0][i][0]=str(int(myarr[0][i][0])+int(myarr[0][m][0]))
                                        myarr[0][m][0]="del"

                if len(myarr[0][i])>6:
                        if "PREV" in myarr[0][i][6] or "NEXT" in myarr[0][i][6]:
                                tmp.append(myarr[0][i])

######################################################################

def read_and_exec(name):
        arr_temp=[]
        arr_t=[]
        f=open(name+".txt","r",encoding="utf-8")
        for line in f:
                row=line.split('	')
                if row==['}\n']:
                        arr_t.append(arr_temp)
                        arr_temp=[]
                        continue
                
                arr_temp.append(row)

        f.close()

        subprocess.call('python main.py template_corp 300 4 '+name, shell=True)
        return arr_t

def change(arr_t,param,mode,name):
        tm=[]

        if mode==0:##удаляем редко встречающиеся
                for j in range(len(arr_t[0])):
                        if arr_t[0][j][0]==name or arr_t[0][j]==['}\n'] or arr_t[0][j]==['{\n']:
                                continue

                        if int(arr_t[0][j][0])>param and len(arr_t[0][j])>4:
                                tm.append(arr_t[0][j])
                                
                        #if len(arr_t[0][j-1])>3 and len(arr_t[0][j])>4 and (arr_t[0][j-1][1]!=arr_t[0][j][1] and arr_t[0][j-1][3]!=arr_t[0][j][3]):
                                #tm.append(arr_t[0][j])

                f=open(name+".txt","w",encoding="utf-8")
                f.write(name+"\n")
                f.write("{\n")

                for k in range(len(tm)):
                        for m in range(len(tm[k])):
                                if m==0:
                                        f.write(tm[k][m])
                                else:
                                        f.write('\t'+tm[k][m])

                f.write('}\n')
                f.close()

        if mode==1:
                 for j in range(2,len(arr_t[0])):
                        if arr_t[0][j][0]==name or arr_t[0][j]==['}\n'] or arr_t[0][j]==['{\n']:
                                continue

                        flag=1
                        
                        if int(arr_t[0][j][0])>param and len(arr_t[0][j])>4:
                                r=j+1
                                while(r<len(arr_t[0])-1):
                                        if arr_t[0][r][2]==arr_t[0][j][2] and arr_t[0][r][3]==arr_t[0][j][3]:
                                                flag=0
                                                break
                                        r=r+1


                                if flag==0:        
                                        arr_t[0][j][2]="_"
                                        
                                arr_t[0][j][2]="_"
                                arr_t[0][j][5]="_"
                        

        if mode==2:
                 for j in range(2,len(arr_t[0])):
                        if arr_t[0][j][0]==name or arr_t[0][j]==['}\n'] or arr_t[0][j]==['{\n']:
                                continue

                        if int(arr_t[0][j][0])>param and len(arr_t[0][j])>4:
                                if arr_t[0][j][6]=="next":
                                        arr_t[0][j][6]="right"
                                
                                if arr_t[0][j][6]=="prev":
                                        arr_t[0][j][6]="left"

                        
        if mode!=0:
                f=open(name+".txt","w",encoding="utf-8")

                for k in range(len(arr_t[0])):
                        for m in range(len(arr_t[0][k])):
                                if m==0:
                                        f.write(arr_t[0][k][m])
                                else:
                                        f.write('\t'+arr_t[0][k][m])

                f.write('}\n')
                f.close()


def verdict(arr,best,acc):
        f=open("result.txt","r",encoding="utf-8")
        res=[]

        for line in f:
                row=line.split('	')
                res.append(row)
        f.close()

        print(res)
		
        if float(res[0][0])<acc:
                #print(str(arr[0][0])+' '+str(res[0][0])+' '+str(arr[1][0])+' '+str(res[1][0]))
                best=float(res[1][0])
                acc=float(res[0][0])
                return 1,best,acc
        else:
                #print(str(arr[0][0])+' '+str(res[0][0])+' '+str(arr[1][0])+' '+str(res[1][0]))
                return 0,best,acc




########### Первый прогон ##############

def progon(name):
        v=0
        m=0
        k=10
        best=100
        acc=1500
        ans=[]

        f=open("result.txt","w",encoding="utf-8") ### очистка
        f.close()

        generate(0,300,name) ###генерация
        a=read_and_exec(name)
        f=open("result.txt","r",encoding="utf-8")
        res=[]

        for line in f:
                row=line.split('	')
                res.append(row)
        f.close()


        while(m<10 or v==1):
                f=open("result.txt","w",encoding="utf-8") ### очистка
                f.close()
                r=a.copy()

                for mode in range(2):
                        if mode==0:
                                change(r,k,mode,name)
                                b=read_and_exec(name)
                                v,best,acc=verdict(res,best,acc)##best разница между точностью работы acc--количество неверных срабатываний

                        if mode!=0:
                                change(b,k,1,name)
                                b=read_and_exec(name)
                                v,best,acc=verdict(res,best,acc)
                                
        
                        if (v==1):
                                ans=b.copy()
                                break
                
                
                if m==9 and ans==[]:
                        ans=b.copy()

                
                f=open(name+".txt","w",encoding="utf-8") ### очистка
                f.close()
                f=open("result.txt","w",encoding="utf-8") ### очистка
                f.close()

                k=k+10
                m=m+1

        
        f=open(name+".txt","w",encoding="utf-8")
        for k in range(len(ans[0])):
                for m in range(len(ans[0][k])):
                        if m==0:
                                f.write(ans[0][k][m])
                        else:
                                f.write('\t'+ans[0][k][m])

        f.write('}\n')
        f.close()
        

##################

if __name__ == '__main__':
        if len(sys.argv)<2:
            name="opred"
        else:
            name=sys.argv[1]

        progon(name)

        


#skleika(arr_t,"NUM","S","left","prev","right","next","NEXT")
#skleika(arr_t,"PARTCP","S","left","prev","right","next","NEXT")
#skleika(list(arr_t),"A","S","right","next","left","prev","PREV")

        


