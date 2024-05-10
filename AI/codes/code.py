from queue import Queue
class Graph:
            n = None
            matrix = []
            dfs_list = []
            bfs_list = []
            def __init__(self, matrix:list, verbose:bool=False, n:int=0) -> None:
                if verbose:
                    for i in range(n):
                        row = []
                        for j in range(n):
                            connection = int(input("Enter 0 if no connection between " + str(i) + " and " + str(j) + " else enter 1: "))
                            row.append(connection)
                        self.matrix.append(row)
                else:
                    self.matrix = matrix
            def printGraph(self) -> None:
                for row in self.matrix:
                    print(row)
            
            def dfs(self, source:int, visited:list) -> list:
                self.dfs_list.append(source)
                visited[source] = True
                row = self.matrix[source]
                for node in range(len(row)):
                    if (visited[node] == False and self.matrix[source][node] != 0):
                        self.dfs(node, visited)
                return self.dfs_list
            
            def bfs(self, source:int, visited:list) -> list:
                queue = Queue()
                queue.put(source)
                visited[source] = True
                while (queue.empty() != True):
                    curr = queue.get()
                    self.bfs_list.append(curr)
                    row = self.matrix[curr]
                    for node in range(len(row)):
                        if (visited[node] == False and self.matrix[curr][node] != 0):
                            queue.put(node)
                            visited[node] = True
                return self.bfs_list
        