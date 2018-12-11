
def link(greater,rule,name,leng):
        morph=greater
        show=1
       
        for j in range(len(greater)):
                if len(greater[j])<3:
                        continue
                if greater[j][3]==rule[0]:
                         if rule[1]!="_":
                             row=rule[1].split('/')
                             for t in range(len(row)):
                                 if not row[t] in greater[j][4]: ##проверили морфологию
                                     continue

                         if rule[2]=="_":
                                 fl=1
                                 if rule[1]!="_":
                                        row=rule[1].split('/')
                                        for t in range(len(row)):  
                                                 if not row[t] in greater[j][4]: ##проверили морфологию
                                                     fl=0 
                                                     continue
                                 if rule[3]=="if":
                                         for m in range(len(greater)):
                                                 if greater[m][2]!=rule[4]:
                                                         fl=0
                                                 if greater[m][2]==rule[4] and j!=m:
                                                         if rule[4]!="-":
                                                                 if j<m:
                                                                         fl=0
                                                                 else:
                                                                         fl=1
                                                                 continue

                                         if rule[4]=="pos":
                                                if j==int(rule[5])-1:
                                                        row=rule[6].split('/')
                                                        for t in range(len(row)):  
                                                                 if row[t]==greater[j][2]:
                                                                         if morph[j][6]=="_":
                                                                            morph[j][6]="0"
                                                                            #morph[j][7]=name
                                                                            #return morph
                                                                         if show==1:
                                                                            if name in morph[j][7]:
                                                                                   return morph
                                                                            morph[j][6]= morph[j][6]+":"+"0"
                                                                            #morph[j][7]=morph[j][7]+":"+name
                                                                            #return morph
                                                                                

                                                        fl=0
                                                        
                                                                        
                                                
                                 if fl==1:
                                         if morph[j][6]=="_":
                                                 morph[j][6]="0"
                                                 #morph[j][7]=name
                                                 #return morph
                                                
                                         if show==1:
                                                if name in morph[j][7]:
                                                        return morph
                                                morph[j][6]= morph[j][6]+":"+"0"
                                                #morph[j][7]=morph[j][7]+":"+name
                                                #return morph

                         if rule[5]=="prev":
                             if len(greater[j-1])>3 and (greater[j-1][3]==rule[2] or greater[j-1][2]==rule[2]):
                                 if rule[3]!="_":
                                     if not rule[3] in greater[j-1][2]:
                                         continue
                                 if rule[4]!="_":
                                     if not rule[4] in greater[j-1][4]:
                                         continue

                                 if morph[j][6]=="_":
                                        morph[j][6]=greater[j-1][0]
                                        morph[j][7]=name
                                 if show==1:
                                        if name in morph[j][7]:
                                                return morph
                                        morph[j][6]=morph[j][6]+":"+greater[j-1][0]
                                        #morph[j][7]=morph[j][7]+":"+name
                                     
                                    
                         if rule[5]=="next":
                                 if len(greater[j+1])>3 and greater[j+1][3]==rule[2] or greater[j+1][2]==rule[2] :
                                     if rule[3]!="_":
                                         if not rule[3] in greater[j+1][2]:
                                                 continue
                                     if rule[4]!="_":
                                        if not rule[4] in greater[j+1][4]:
                                                continue
                                            
                                     if morph[j][6]=="_":
                                        morph[j][6]=greater[j+1][0]
                                        #morph[j][7]=name
                                     if morph==1:
                                        if name in morph[j][7]:
                                               return morph
                                        morph[j][6]=morph[j][6]+":"+greater[j+1][0]
                                        #morph[j][7]=morph[j][7]+":"+name
                                    

                         if rule[5]=="left":
                                 t=j-1
                                 while(t>0):
                                      if greater[t]==['', '\n']:
                                          t=t-1
                                          continue
                                      if greater[t][3]==rule[2] or greater[t][2]==rule[2] :
                                             if rule[3]!="_":
                                                 if not rule[3] in greater[j-1][2]:
                                                         t=t-1
                                                         continue
                                            
                                             if rule[4]!="_":
                                                 row=rule[4].split('/')
                                                 for y in range(len(row)):
                                                     if not row[y] in greater[j][4]: ##проверили морфологию
                                                        continue
                                                        
                                                 if y==len(row)-1:
                                                     if morph[j][6]=="_":
                                                             morph[j][6]=greater[t][0]
                                                             #morph[j][7]=name
                                                     if show==1:
                                                             if name in morph[j][7]:
                                                                     return morph
                                                             morph[j][6]=morph[j][6]+":"+greater[j+1][0]
                                                             #morph[j][7]=morph[j][7]+":"+name
                                                     break
                                 

                                      t=t-1
                                         
                                     

                         if rule[5]=="right":
                                 t=j+1
                                 while(0<1):
                                      if greater[t]==['', '\n']:
                                          t=t+1
                                          continue

                                      if greater[t][3]=="SENT":
                                              break
                                      if greater[t][3]==rule[2] or greater[t][2]==rule[2] :
                                             if rule[3]!="_":
                                                 if not rule[3] in greater[j+1][2]:
                                                     break
                                            
                                             if rule[4]!="_":
                                                 row=rule[4].split('/')
                                                 for y in range(len(row)):
                                                     if not row[y] in greater[j][4]: ##проверили морфологию
                                                         continue
                                                        
                                                 if y==len(row)-1:
                                                     if morph[j][6]=="_":
                                                             morph[j][6]=greater[t][0]
                                                             #morph[j][7]=name
                                                     if show==1:
                                                             if name in morph[j][7]:
                                                                     return morph
                                                             morph[j][6]=morph[j][6]+":"+greater[j+1][0]
                                                             #morph[j][7]=morph[j][7]+":"+name
                                                     break

                                 
                                      t=t+1

        return morph    
               
            
def link_(morph,arr,name):
      res=[]
      
      for m in range(len(arr)):
          for s in range(len(arr[m])):
              if arr[m][s][0]==name or "{" in arr[m][s][0] or "}" in arr[m][s][0]:
                    continue
              if arr[m][s]==['', '\n']:
                    continue

              res=link(morph,arr[m][s],name,len(arr[m]))

              for p in range(len(res)):
                      if name=="root" and res[p][7]==name:
                              return res


      #for i in range(len(res)):
              #if ":" in res[i][6]:
                      #row=res[i][6].split(":")
                     
                      #if row[0]==row[1]:
                              #res[i][6]=row[0]
                      #row=res[i][7].split(":")
                      #if row[0]==row[1]:
                              #res[i][7]=row[0]
                              

      return res

        

