import skeletor as sk
from meshparty import trimesh_io

mm = trimesh_io.MeshMeta(
    cv_path = 'graphene://https://prodv1.flywire-daf.com/segmentation/1.0/fly_v31',
    disk_cache_path = "/mnt/c/Users/luntzel",
    map_gs_to_https=True)

#mesh
#mesh = sk.example_mesh()
mesh = mm.mesh(filename = '720575940629522243.h5')

fixed = sk.pre.fix_mesh(mesh, remove_disconnected=5, inplace=False)
cont = sk.pre.contract(fixed, epsilon=0.2)
skel = sk.skeletonize.by_vertex_clusters(cont, sampling_dist=100)
skel.mesh = fixed
sk.post.clean_up(skel, inplace=True)
sk.post.radii(skel, method='knn')

#save skeleton info
array = skel.edges
array.astype('float32').tofile('sktor34e.dat')

array2 = skel.vertices
array2.astype('float32').tofile('sktor34v.dat')

array3 = skel.radius
array.astype('float32').tofile('sktor34r.dat')
