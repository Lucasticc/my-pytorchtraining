#三个容器
#根据题意创建散列表
n =12
edge=dict((i,{}) for i in range(n))
 
#例如edge[1]={2:12,3:14}表示1到2费用是12，1到3费用是14
 
vis=[False for i in range(n)]
 
d=[0 for i in range(n)]
 
def dfs(x):
    global vis,edge
    for i in edge[x]:
        if not vis[i]:
            d[i]=d[x]+edge[x][i]
            vis[i]=True
            dfs(i)
            vis[i]=False
 
#初始化
vis[0]=0
dfs(0)
 
 
Q=d.index(max(d))#一个端点
 
#接下来重复上述，重置
vis=[False for i in range(n)]
d=[0 for i in range(n)]
vis[Q]=True
dfs(Q)
 
W=d.index(max(d))
 
#QW为直径