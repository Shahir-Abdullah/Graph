from collections import deque 

class State(object):
    def __init__(self, state=None):
        
        if state == None:
            state = "0"
        self.__state = state 
    
    def generate_next_state(self):
        child_states = []

        if self.__state ==  "0":
            child_states.append("9") 
            ''' man with goat ''' 

        elif self.__state == "1":
            child_states.append("9") 
            ''' man alone '''
            child_states.append("13") 
            ''' man with wolf '''
            child_states.append("11") 
            ''' man with cabbage ''' 

        elif self.__state == "2":
            child_states.append("14") 
            ''' man with wolf '''
            child_states.append("11") 
            ''' man with goat ''' 

        elif self.__state == "4":
            child_states.append("14") 
            ''' man with cabbage ''' 
            child_states.append("13") 
            ''' man with goat ''' 

        elif self.__state == "6":
            child_states.append("14") 
            ''' man alone '''
            child_states.append("15") 
            ''' man with goat ''' 

        elif self.__state == "9":
            child_states.append("1") 
            ''' man alone '''
            child_states.append("0") 
            ''' man with goat ''' 

        elif self.__state == "11":
            child_states.append("3") 
            ''' man alone '''
            child_states.append("1") 
            ''' man with cabbage ''' 
            child_states.append("2") 
            ''' man with goat ''' 

        elif self.__state == "13":
            child_states.append("5") 
            ''' man alone '''
            child_states.append("4") 
            ''' man with goat ''' 
            child_states.append("1") 
            ''' man with wolf ''' 
        elif self.__state == "14":
            child_states.append("6") 
            ''' man alone '''
            child_states.append("4") 
            ''' man with cabbage ''' 
            child_states.append("2") 
            ''' man with wolf ''' 

        return child_states

class Node(object):
    def __init__(self, node_state=None, node_parent=None, node_action=None):
        if node_action == None:
            node_action = ' '
        if node_parent == None:
            node_parent = None 
        if node_state == None:
            node_state = State()
        
        self.__node_state = node_state 
        self.__node_action = node_action
        self.__node_parent = node_parent 
    
    def generate_child_nodes(self):

        child_states = self.__node_state.generate_next_state()
        child_nodes = []

        for child_state in child_states:
            child = Node(child_state, self)
            child_nodes.append(child)
        
        for child in child_nodes:
            print(child.__node_state)
            
            
        
        return child_nodes  
    

class Graph(object):
    def __init__(self, graph_dict=None, list_invalid=None):
        '''
        if no dictornary given, empty dictonary created
        '''
        if list_invalid == None:
            list_invalid = ["3", "5", "7", "8", "10", "12"]
        if graph_dict == None:
            s = State()
            child = s.generate_next_state()
            graph_dict = {}
            for c in child:
                if "0" in graph_dict:
                    graph_dict["0"].append(c) 
                else:
                    graph_dict["0"] = [c]
                if c in graph_dict:
                    graph_dict[c].append("0")
                else:
                    graph_dict[c] = ["0"]

           

        self.__graph_dict = graph_dict
        self.__list_invalid = list_invalid

    def vertices(self):
        '''
        returns the vertices of the graph
        '''
        return list(self.__graph_dict.keys())
    
    def edges(self):
        '''
        returns the edges of the graph
        '''
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        '''
        if vertex not present in graph, add, else do nothing
        '''
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge):
        '''
        assuming edge is of type set, tuple or list
        '''
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def __generate_edges(self): 
        '''
        class function
        represented as sets
        '''
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges 
    
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res 
    
    def find_path(self, start_vertex, end_vertex, path=None):
        graph = self.__graph_dict
        if path == None:
            path = []
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path 
        if start_vertex not in graph:
            return None 
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path
        return None 

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices =  self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

            
    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def BFS(self, start_vertex, goal_vertex):
        q = deque()
        q.append(start_vertex)
        visited = []
        explored = []
        graph = self.__graph_dict
        
        while q:
            v = q.popleft()

                
            starter_children = []
            starter_children = State(v).generate_next_state()
            for child in starter_children:
                if v not in graph:
                    graph[v] = child
                else:
                    graph[v].append(child)
                if child not in graph:
                    graph[child] = [v]
                else:
                    graph[child].append(v)

                visited.append(v)
                print("mother node " + v)
                print("\n")
                
               

            for neighbour in graph[v]:
                if neighbour not in visited and neighbour not in explored:
                    if neighbour not in self.__list_invalid:
                        q.append(neighbour)
                        explored.append(neighbour)
                        print("child nodes " + neighbour)
                    if neighbour == goal_vertex:
                        print("found ")
                        return explored
                    else:
                        pass 


            



if __name__ == "__main__":
   
    graph = Graph()

    explored = graph.BFS("0", "15")
    print(visited)
    

    
    







