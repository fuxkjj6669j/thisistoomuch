
# coding: utf-8

# In[20]:


classmate = [("林威豪","台北市"),("黃安安","高雄市"),("林湘琦","台中市"),("陳遠見","台南市"),("林萊萱","台中市"),("許志祥","台北市"),("呂姍姍","嘉義市"),("張柏凱","桃園市")]
new = classmate.copy();
pick = list();
print("(Q1):請顯示出該list變數內容")
print("(A1):")
print(classmate)

print("----------------------------------------------------------------------------------")
print("(Q2):請將全部台北市的同學資料挑出，放入list變數pick裡，同時也將之自原本的list變數刪除。請最後挑出的結果顯示出來")

for j in range(0,len(classmate)):
  if(classmate[j][1] == "台北市"):
    del new[j];
    pick.append(classmate[j])
print(pick)
print("(A2):")

for l in range(0,len(pick)):
  print(pick[l][0],pick[l][1])

print("123")
print(new)

print("----------------------------------------------------------------------------------")
print("(Q3):請利用迴圈指令，一一將原本list變數內的同學顯示出來如下")
print("(A3):")
for k in range(0,len(classmate)):
  print("第",k+1,"位同學",classmate[k][0],"：家住",classmate[k][1])


# In[9]:


classmate = [("林威豪","台北市"),("黃安安","高雄市"),("林湘琦","台中市"),("陳遠見","台南市"),("林萊萱","台中市"),("許志祥","台北市"),("呂姍姍","嘉義市"),("張柏凱","桃園市")]
pick=[]

for mem in classmate:
    if mem[1]=="台北市":
        temp=classmate.pop(classmate.index(mem))
        pick.append(temp)
print(pick)
print(classmate)

