#Adjacency Matrix(인접행렬)

adjacency_matrix=[
                  [0,1,0,1],
                  [1,0,1,1],
                  [0,1,0,0],
                  [1,1,0,0]
                  ]

#Browsing the Nodes
for row in adjacency_matrix:
    print row


#Browsing the link information
for row in adjacency_matrix:
    for a_ij in row:
        print a_ij,
    print "\r"

#Directed Networks

#in the case of directed networks the adjacency matrix is not symetric, like for Food Webs.
#If a non zero element is present in row 2, column 3, this means there is an arc (directed edge)
#from node 2 toward node 3
adjacency_matrix_directed=[
                  [0,1,0,1],
                  [0,0,1,0],
                  [0,0,0,1],
                  [0,0,0,0]
                  ]