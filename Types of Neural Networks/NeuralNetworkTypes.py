# -*- coding: utf-8 -*-
import pydot

# first create a new graph using pydot.Dot()
graph = pydot.Dot(graph_type='graph')

# code contains three levels i.e Root Node, first branch and leaf node

branch_nodes = ['Feed Forward', 'Radial Basis Network (RBN)', 'Deep Feed-forward',
                'Recurrent Neural Network', 'Long / Short Term Memory',
                'Gated Recurrent Unit'
                ]

leaf_nodes = ['Computer Vision', 'Handwritten Characters Recognition',
              'Timeseries Prediction', 'Classification',
              'Computer Vision', 'Financial Prediction',
              'Speech Recognition', 'Chatbots',
              'Speech Recognition', 'Writing Recognition',
              'Natural Language Processing', 'Speech Signal Modeling'
              ]

root_node = pydot.Node("Types of Neural Networks", style="filled", fillcolor="green")
# adding the root node to the graph
graph.add_node(root_node)

for i in range(len(branch_nodes)):
    edge = pydot.Edge(root_node, branch_nodes[i],
                      fontsize="10.0", color="blue"
                      )
    # add the edge to our graph
    graph.add_edge(edge)

for i in range(len(branch_nodes)):
	try:
	    for j in range(2):
	        edge = pydot.Edge(branch_nodes[i], leaf_nodes[j],
	                          fontsize="10.0", color="blue"
	                          )
	        graph.add_edge(edge)
	    # once the leaf nodes are added to branch nodes it is removed from the list    
	    leaf_nodes = leaf_nodes[2:]
	except:
		pass    

# output is written to the graph 
graph.write_png('deep_learning_models.png')
