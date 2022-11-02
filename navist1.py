import navis
from meshparty import trimesh_io

mm = trimesh_io.MeshMeta(
    cv_path = 'graphene://https://prodv1.flywire-daf.com/segmentation/1.0/fly_v31',
    disk_cache_path = "/mnt/c/Users/luntzel",
    map_gs_to_https=True)

#mesh
#mesh = sk.example_mesh()
mesh = mm.mesh(filename = '720575940629522243.h5')

navis.heal_fragmented_neuron(mesh, inplace=True)

mesh.write_to_file('heal.ply')
