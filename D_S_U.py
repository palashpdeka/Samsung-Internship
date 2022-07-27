class DSU:
    def __init__(self,n):
        self.rank=[1]*(n+1)
        self.par=[-1]*(n+1)
        
    def parent(self,a):
        if self.par[a]==-1:
            return a
        else:
           self.par[a]=self.parent(self.par[a])
           return self.par[a]
            
        
    def merge(self,a,b):
        x=self.parent(a)
        y=self.parent(b)
        if(x==y): 
            return
        elif self.rank[x]>self.rank[y]:
            self.rank[x]+=self.rank[y]
            self.par[y]=x
        else:
            self.rank[y]+=self.rank[x]
            self.par[x]=y