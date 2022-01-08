import open3d as o3d
import open3d_proccess

if __name__ == "__main__":
    voxel_size = 0.005  # means 5cm for the dataset
    source = o3d.io.read_point_cloud("./bun045.ply")
    target = o3d.io.read_point_cloud("./bun000.ply")

    source, target, source_down, target_down, source_fpfh, target_fpfh = \
        open3d_proccess.prepare_dataset(voxel_size=voxel_size, source=source, target=target)

    result_ransac = open3d_proccess.execute_global_registration(source_down, target_down,
                                                                source_fpfh, target_fpfh,
                                                                voxel_size)
    print(result_ransac)
    open3d_proccess.draw_registration_result(source_down, target_down,
                                             result_ransac.transformation)

    result_icp = open3d_proccess.refine_registration(source_down, target_down, voxel_size, result_ransac)
    print(result_icp)
    open3d_proccess.draw_registration_result(source, target, result_icp.transformation)
