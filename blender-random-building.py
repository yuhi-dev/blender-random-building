import bpy
import random

spacing = 2.2
for x in range(10):
    for y in range(10):
        location = (x * spacing, y * spacing, random.random() * 2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=(1, 1, 1))
        
        item = bpy.context.object
        if random.random() < 0.25:
            item.data.materials.append(bpy.data.materials["Material.001"])
        elif random.random() < 0.25:
            item.data.materials.append(bpy.data.materials["Material.002"])
        elif random.random() < 0.25:
            item.data.materials.append(bpy.data.materials["Material.003"])
        else:
            item.data.materials.append(bpy.data.materials["Material.004"])
