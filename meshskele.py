from meshparty import trimesh_io
 
from meshparty import skeletonize

from meshparty import skeleton_io


mm = trimesh_io.MeshMeta(
    cv_path = 'graphene://https://prodv1.flywire-daf.com/segmentation/1.0/fly_v31',
    disk_cache_path = "/mnt/c/Users/luntzel",
    map_gs_to_https=True)

#load mesh
mesh = mm.mesh(filename = "720575940629522243.h5")
#mesh = mesh.fix_mesh()
# skeletonize the mesh using a 12 um invalidation radius
# assuming units of mesh.vertices is in nm
sk = skeletonize.skeletonize_mesh(mesh,
                      invalidation_d=12000)

#sk.write_to_file('plssempai.h5')
skeleton_io.write_skeleton_h5(sk, '110122test.h5', overwrite=True) #34skelfromwt.h5
