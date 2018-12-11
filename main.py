import sys
from v1_3 import pravilo_primenitel
from templat import temp
from tester import test_process
from generator import generate
from link_template import link_

greater=[]
template=[]

def isfloat(value):
        try:
                float(value)
                return True
        except ValueError:
                return False

def reader(name):
    arr=[]
    arr_temp=[]
    
    f=open(name+".txt","r",encoding="utf-8")
    for line in f:
            row=line.split('	')
            if row==['}\n']:
                    arr.append(arr_temp)
                    arr_temp=[]
                    continue
                
            if isfloat(row[0]):
                row.pop(0)
                
            arr_temp.append(row)

    f.close()
    return arr

        
def workspace(name,amount,mode,towrite,test):
    tmp_template=[]
    tmp=[]
    arr=[]
    final=[]
    rules=[]
    pr=[]
    tmp_arr=[]

    f=open("morph.txt","r",encoding="utf-8")
    
    for line in f:
        if line=='\n':
            greater.append(tmp)
            tmp=[]
        else:
            row=line.split('	')
            tmp.append(row)

    f.close()


    f=open(name+".txt","r",encoding="utf-8")
    for line in f:
        row=line.split('\t')
        if row==['\n']:
            continue
        if row==['end\n']:
            tmp_template.append(row)
            template.append(tmp_template)
            tmp_template=[]
            continue
        
        tmp_template.append(row)
        
    f.close()
    
    f=open("rules.txt","r",encoding="utf-8")
    for line in f:
        row=line.split('	')
        rules.append(row)
    
    f.close()

    f=open("predlogipadeji.txt","r",encoding="utf-8")
    for line in f: #считали данные предлогов в массив pr
        row=line.split('	')
        pr.append(row)

    f.close()

    ##################
    predl=[]
    opred=[]
    kompl=[]
    kvaziagent=[]
    root=[]
    predic=[]
    
    predl=reader("predl")
    opred=reader("opred")
    kompl=reader("1-kompl")
    kvaziagent=reader("kvaziagent")
    root=reader("root")
    predic=reader("predic")
    atrib=reader("atrib")
    vspom=reader("vspom")
    kolichest=reader("kolichest")

    ###################

    f=open(towrite,"w",encoding="utf-8")
    f.close()

    for j in range(int(amount)):
        try:
            if mode=="1":
                arr,work=temp(greater[j],template)
                tmp_arr=pravilo_primenitel(arr,rules,pr)
                final.append(tmp_arr)
                arr=[]
                tmp_arr=[]
        
            if mode=="2":
                arr,work=temp(greater[j],template)
                final.append(arr)
                arr=[]
       
            if mode=="3":
                arr=pravilo_primenitel(greater[j],rules,pr)
                final.append(arr)
                arr=[]

            if mode=="4":
                if test=="predl":
                        arr=link_(greater[j],predl,"predl")
                        
                if test=="opred":
                        arr=link_(greater[j],opred,"opred")

                if test=="kvaziagent":
                        arr=link_(greater[j],kvaziagent,"kvaziagent")

                if test=="1-kompl":
                        arr=link_(greater[j],kompl,"1-kompl")
                        
                if test=="all":
                        arr=link_(greater[j],predl,"predl")
                        arr=link_(arr,opred,"opred")
                        arr=link_(arr,kompl,"1-kompl")
                        arr=link_(arr,kvaziagent,"kvaziagent")
                        arr=link_(arr,predic,"predic")
                        arr=link_(arr,root,"root")
                        arr=link_(arr,atrib,"atrib")
                        arr=link_(arr,vspom,"vspom")
                        arr=link_(arr,kolichest,"kolichest")

                final.append(arr)
                arr=[]

            if mode=="5":
                arr=link_(greater[j],predl,"predl")
                arr=link_(arr,opred,"opred")
                arr=link_(arr,kvaziagent,"kvaziagent")
                arr=link_(arr,kompl,"1-kompl")
                arr,work=temp(arr,template)
                final.append(arr)
                arr=[]

            if mode=="6":
                arr=link_(greater[j],predl,"predl")
                #arr=link_(arr,root,"root")
                arr=link_(arr,opred,"opred")
               
                arr=link_(arr,kompl,"1-kompl")
                arr=link_(arr,kvaziagent,"kvaziagent")
                #arr=link_(arr,predic,"predic")
                #arr=link_(arr,root,"root")
                arr,work=temp(arr,template)
                arr=pravilo_primenitel(arr,rules,pr)
                final.append(arr)
                arr=[]
        
        except:
                final.append(greater[j])
                arr=[]
        
   
    f=open(towrite,"a",encoding="utf-8")
    for i in range(len(final)):
        if final[i]==['\n']:
            f.write('\n')
            continue

        try:
            for j in range(len(final[i])):
                f.write(final[i][j][0]+'\t'+final[i][j][1]+'\t'+final[i][j][2]+'\t'+final[i][j][3]+'\t'+final[i][j][4]+'\t'+final[i][j][5]+'\t'+final[i][j][6]+'\t'
                    +final[i][j][7]+'\t'+final[i][j][8]+'\n')

        except:
            0

        f.write('\n')

    f.close()

    #f=open("stat.txt","w",encoding="utf-8")
    #for i in range(len(work)):
            #for j in range(len(work[i])):
                    #for k in range(len(work[i][j])):
                            #f.write(work[i][j][k]+'\t')
                    
            #f.write('\n')
    #f.close()



if __name__ == '__main__':
        #print('Первый параметр. Название файла с шаблонами :\n template(правила написанные вручную) \n template_corp (правила полученные из корпуса)')
        #print('Второй параметр. Количество предложений ')
        #print('Третий параметр. Режим работы программы: \n 1.Шаблоны+правила (вручн.) \n 2.Только шаблон \n 3.Только правила (вручную) \n 4.Только правила(генер.) \n'+
              #' 5.Шаблоны+правила (генер.) \n 6 Метод с наилучшим результатом \n')

        p=0 ###включить типы связей в шаблон при генерации

        name=''
        amount=''
        mode=''
        
        if len(sys.argv)<4:
            name="template_corp"
            amount="300"
            mode="6"
            test='all'
        else:
                name = sys.argv[1]
                amount = sys.argv[2]
                mode=sys.argv[3]
                test=sys.argv[4]
                    
        #name="template_corp"
        #amount="300"
        #mode="4"
        #test="opred"
        #generate(p,int(amount),'1-kompl')
        
        if test=="all":
            print('Генерация правил из фрагмента корпуса.')
            generate(p,int(amount),'all')
            print('Завершено\n')
        
        #############################################
            
        test_gl=[]
        f=open("my_test.txt","r",encoding="utf-8")
        i=0;
        for line in f:
           row=line.split('	')
           test_gl.append(row)
           
        f.close()

        #tt=[]
        #ttt=[]
        #for y in range(len(test_gl)):
            #if test_gl[y]==['\n']:
                #ttt.append(tt)
                #tt=[]
            #else:
                #tt.append(test_gl[y])

        ############################################
                
        workspace(name,amount,mode,"syntax.txt",test)
        #print('Тестирование (syntax -- результат работы программы и my_test -- фрагмент корпуса) \n')
        test_process(test)
        #print('Результат работы в файле result\n')
        

       






