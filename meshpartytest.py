from meshparty import trimesh_io
from cloudvolume import CloudVolume

#cv = CloudVolume('graphene://https://prodv1.flywire-daf.com/segmentation/1.0/fly_v31', progress=True, use_https=True)
meshmeta = trimesh_io.MeshMeta(
    cv_path = 'graphene://https://prodv1.flywire-daf.com/segmentation/1.0/fly_v31',
    disk_cache_path = "/mnt/c/Users/luntzel",
    map_gs_to_https=True)

#meshmeta = trimesh_io.MeshMeta()
#mesh.fix_mesh()
mesh = meshmeta.mesh(seg_id = 720575940621039145) #720575940629522243, filename='110122test.h5') # mesh gets cached

#local_vertices = mesh.get_local_view(n_points, pc_align=True, method="kdtree")
