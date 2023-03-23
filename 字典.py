# 使用zip函数把两个列表进行合并 
#最后合成的字典 以最少的那个为标准
key_list= ['D',"w","D","Q","R"]
value_list = ['1','2']
dict1 =dict(zip(key_list,value_list))
dict2= dict((('a','5'),('b','2'),('w','10')))
dict3 = {'lilee':25, 'age':24, 'phone':12}
# print(dict1,dict2)
dict4 = {}
print(dict2)
for i in sorted(dict2) :
    #2、setdefault：向字典中添加键值对，如果这个键已经存在，不做修改；如果不存在，就添加到字典中
    dict4.setdefault(i,dict2[i])
print(dict4)
def dictionairy():  
  
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_list= ['D',"w","D","Q","R"]
    value_list = ['9','2']
    key_value =dict(zip(key_list,value_list))
    for j in key_value:
        key_value[j] = int(key_value[j])
 
    print ("按键(key)排序:")   
 
    # sorted(key_value) 返回重新排序的列表
    # 字典按键排序
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 
        # dict2.update(i,key_value[i])
  
def main(): 
    # 调用函数
    dictionairy()         
    # print(1)     
      
# 主函数
if __name__=="__main__":      
    main()
