
def dictionairy():  
 
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_value['a'] = '56'       
    key_value['b'] = '2' 
    key_value[5] = '12' 
    key_value[4] = '24'
    key_value[6] = '18'      
    key_value[3] = '323' 
    for key in key_value:
        key_value[key] = int(key_value[key])
 
    print ("按值(value)排序:")   
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))     
   
def main(): 
    dictionairy()             
      
if __name__=="__main__":       
    main()