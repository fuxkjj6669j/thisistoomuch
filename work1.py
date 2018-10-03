#!/usr/bin/env python
# coding: utf-8

# In[20]:


fruit=["水果1","水果2","水果3","水果4","水果5","水果6","水果7","水果8","水果9","水果10"]

print("(1)顯示出所有水果名稱")
print(fruit)
print("(2)顯示出第5種水果名稱")
print(fruit[4])
print("(3)顯示出最後1種水果名稱")
print(fruit[-1])
print("(4)顯示出第3種至第6種水果名稱")
print(fruit[2:6])
print("(5)利用一個指令將第3種水果放入變數PickFruit內後，同時也自原變數刪除。顯示出PickFruit並另外顯示出原本list變數")
PickFruit=fruit.pop(2)
print(PickFruit)
print(fruit)
print("(6)請把「蜜桃」放在第二個位置，並顯示該list變數")
fruit.insert(1,"蜜桃")
print(fruit)
print("(7)請把「非洲甜橙」附加在最後，並顯示該list變數")
fruit.append("非洲甜橙")
print(fruit)
print("(8)請建立另一個list變數，內含三個地區的名稱：亞洲、非洲、美洲")
country=["亞洲","非洲","美洲"]
print("(9)請把新的list附加在舊的list的後面，成為舊list變數的另外三個元素。顯示出附加後的list內容。")
fruit.extend(country)
print(fruit)


# In[ ]:




