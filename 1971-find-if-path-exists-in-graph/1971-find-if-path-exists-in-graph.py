import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=[False]*n
        queue=[]
        queue.append(source)
        visited[source]=True
        h=collections.defaultdict(list)
        for i in edges:
            h[i[0]].append(i[1])
            h[i[1]].append(i[0])
        while queue:
            s=queue.pop()
            for i in h[s]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
                    
        return visited[destination]
        