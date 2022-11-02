import navis
import pandas as pd
#from meshparty import trimesh_io

swc=pd.read_csv('swc342wd5r.csv')
tn = navis.TreeNeuron(swc)
print(type(tn))
#.nodes is a dataframe, .edges is an array
#print("V/E", type(treeneuron.nodes), type(treeneuron.edges))

edges = tn.edges #np.ndarrays
edges.astype('float32').tofile('navisedges.dat')

verts = tn.nodes #df
verts.to_csv('navisverts.csv')
