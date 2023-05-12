import open3d as o3d
import pandas as pd
from scipy.spatial import Delaunay
import numpy as np
from copy import deepcopy as copy
import settings
from tqdm import tqdm

query_pc = pd.read_csv(settings.query, usecols = ["x", "y", "z"])
query_pc_pts = query_pc.values
query_pcd = o3d.geometry.PointCloud()
query_pcd.points = o3d.utility.Vector3dVector(query_pc_pts)
query_pcd.paint_uniform_color([0, 0, 1.0])

shortest_distances = np.zeros((len(list(settings.targets.keys())), len(query_pc_pts)))
for idx, key in enumerate(settings.targets.keys()):
    target_pc_pts = pd.read_csv(key, usecols = ["x", "y", "z"]).values
    # print("target_pc_pts", target_pc_pts.shape)
    target_pcd = o3d.geometry.PointCloud()
    target_pcd.points = o3d.utility.Vector3dVector(target_pc_pts)
    distances = np.asarray(query_pcd.compute_point_cloud_distance(target_pcd))
    shortest_distances[idx] = distances
two_min = np.argsort(shortest_distances, axis = 0)[:2]
shortest_distances = np.sort(shortest_distances,axis = 0)
valid_distances = np.sum(shortest_distances[:2], axis = 0) <= settings.y_dist

def in_hull(p, hull):
        if not isinstance(hull,Delaunay):
            hull = Delaunay(hull)

        return hull.find_simplex(p)>=0

lies_or_not = {}
for idx, key in enumerate(settings.targets.keys()):
    for jdx, jkey in enumerate(settings.targets.keys()):
        if idx != jdx:
            hull_points = np.vstack((pd.read_csv(key, usecols = ["x", "y", "z"]).values, \
                                    pd.read_csv(jkey, usecols = ["x", "y", "z"]).values))
            lies_or_not[str(idx)+str(jdx)] = in_hull(query_pc_pts,hull_points)

total_ans = np.zeros(len(query_pc_pts))
geometries = []
keys = list(settings.targets.keys())
for key in tqdm(settings.targets.keys()):
    target_pc_pts = pd.read_csv(key, usecols = ["x", "y", "z"]).values
    target_pcd = o3d.geometry.PointCloud()
    target_pcd.points = o3d.utility.Vector3dVector(target_pc_pts)
    target_pcd.paint_uniform_color([1.0, 0, 0])

    settings.targets[key]+=0.01
    sphere_mesh = o3d.geometry.TriangleMesh.create_sphere(settings.targets[key],10)
    sphere_pts = np.asarray(np.asarray(sphere_mesh.vertices))
    sphere = o3d.geometry.PointCloud()
    sphere.points = o3d.utility.Vector3dVector(sphere_pts)

    to_expand_pcd = copy(target_pcd)
    to_expand_pcd_pts = np.asarray(to_expand_pcd.points)
    expanded_pts = np.array([[to_expand_pcd_pts[0][0],to_expand_pcd_pts[0][1],to_expand_pcd_pts[0][2]]])
    for i in to_expand_pcd_pts:
        expanded_pts = np.vstack((expanded_pts, i+sphere_pts))

    expanded_pcd = o3d.geometry.PointCloud()
    expanded_pcd.points = o3d.utility.Vector3dVector(expanded_pts)

    hull, _ = expanded_pcd.compute_convex_hull()
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
    hull_ls.paint_uniform_color((0, 1, 1)) #looseboundgraphicCYAN

    hull_hard, _ = target_pcd.compute_convex_hull()
    hull_ls_hard = o3d.geometry.LineSet.create_from_triangle_mesh(hull_hard)
    hull_ls_hard.paint_uniform_color((1, 0, 0)) #rigidboundRED

    def in_hull(p, hull):
        if not isinstance(hull,Delaunay):
            hull = Delaunay(hull)

        return hull.find_simplex(p)>=0

    ans_losen = in_hull(query_pc_pts,expanded_pts)
    ans_hard = in_hull(query_pc_pts,target_pc_pts)

    for i in range(len(total_ans)):
        # hull_points = np.vstack((pd.read_csv(keys[two_min[0][i]], usecols = ["x", "y", "z"]).values, \
        #                         pd.read_csv(keys[two_min[1][i]], usecols = ["x", "y", "z"]).values))
        # print(hull_points.shape)
        if valid_distances[i] == True and total_ans[i] != 1 and lies_or_not[str(two_min[0][i])+str(two_min[1][i])][i]:
            total_ans[i] = 2
        if ans_hard[i] == True:
            total_ans[i] = 1
        if ans_hard[i] == False and ans_losen[i] == True and total_ans[i] != 1:
            total_ans[i] = 3
        if ans_hard[i] == False and ans_losen[i] == False and query_pc_pts[i][-1] > 0 and total_ans[i] != 1:
            total_ans[i] = 5
    if settings.targets[key] != 0.01:
        geometries.append(hull_ls)
    geometries.append(hull_ls_hard)

query_pcd_true = o3d.geometry.PointCloud()
query_pcd_true.points = o3d.utility.Vector3dVector(query_pc_pts[total_ans == 1])
query_pcd_false = o3d.geometry.PointCloud()
query_pcd_false.points = o3d.utility.Vector3dVector(query_pc_pts[total_ans == 0])
query_pcd_losen = o3d.geometry.PointCloud()
query_pcd_losen.points = o3d.utility.Vector3dVector(query_pc_pts[total_ans == 3])
query_pcd_false_zpos = o3d.geometry.PointCloud()
query_pcd_false_zpos.points = o3d.utility.Vector3dVector(query_pc_pts[total_ans == 5])
query_pcd_y = o3d.geometry.PointCloud()
query_pcd_y.points = o3d.utility.Vector3dVector(query_pc_pts[total_ans == 2])

query_pcd_true.paint_uniform_color([0, 1, 0])   #inside_tun&oc/1
query_pcd_false.paint_uniform_color([0.698, 0.133, 0.133])  #outside_tun&oc/0
query_pcd_false_zpos.paint_uniform_color([0.5, 0.5, 0.5])  #outsideposz/5
query_pcd_losen.paint_uniform_color([1, 0, 1])  #within100/2
query_pcd_y.paint_uniform_color([0, 0, 1])  #within_y
geometries.append(query_pcd_true)
geometries.append(query_pcd_false)
geometries.append(query_pcd_losen)
geometries.append(query_pcd_y)
geometries.append(query_pcd_false_zpos)

o3d.visualization.draw_geometries(geometries)
o3d.visualization.draw_geometries([query_pcd_true, query_pcd_false, query_pcd_false_zpos, query_pcd_losen, query_pcd_y])

query_pc_add = pd.read_csv(settings.query)
query_pc_add['Answers'] = total_ans
query_pc_add.to_csv("level_1to5.csv")
df = pd.read_csv('level_1to5.csv')


level_1 = df[df['Answers']==1]
level_2 = df[df['Answers']==2]
level_3 = df[df['Answers']==3]
level_4 = df[df['Answers']==0]
level_5 = df[df['Answers']==5]

level_1.to_csv('level_1.csv', index=False)
level_2.to_csv('level_2.csv', index=False)
level_3.to_csv('level_3.csv', index=False)
level_4.to_csv('level_4.csv', index=False)
level_5.to_csv('level_5.csv', index=False)