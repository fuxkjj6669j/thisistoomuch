
# coding: utf-8

# In[1]:


bookshelf = ["1國文","2英文","3數學","4物理","5化學","6生物","7地科","8電子","9電路","10電磁"
             ,"11微分","12機率","13地理","14歷史","15公民"]
print("(Q1):請顯示出所有書籍名稱")
print("(A1):",bookshelf)

print("(Q2):顯示出第8本書籍名稱")
print("(A2):",bookshelf[7])

print("(Q3):顯示出第一本與最後一本書籍名稱")
print("(A3):",bookshelf[0],bookshelf[14])

print("(Q4):顯示出第10本至第12本書籍名稱")
print("(A4):",bookshelf[9:12])

print("(Q5):利用一個指令將最後兩本書籍放入變數SBook內後，同時也自原變數刪除。顯示出SBook並另外顯示出原本list變數")
sbook1 = bookshelf.pop();
sbook2 = bookshelf.pop();
sbook = sbook2+sbook1;
print("(A5):",sbook,bookshelf)

print("(Q6):請把書本「作業研究」放在第五個位置，並顯示該原list變數")
bookshelf.insert(4,"作業研究");
print("(A6):",bookshelf)

print("(Q7):請建立另一個list變數，內含五個國家的名稱(請自訂)")
list = ["台灣","日本","泰國","中國","韓國"]

print("(Q8):請把新的list附加在舊的list的後面，成為舊list變數的另外五個元素。請顯示出附加後的list內容。")
bookshelf.extend(list);
print("(A8):",bookshelf)

