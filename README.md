# blender-random-building

This project generates a grid of randomly sized buildings using Blender and Python. Each building is a cube with a random height and one of four possible materials. The buildings are placed in a 10x10 grid with a specific spacing.

## Requirements

- Blender 2.8 or higher
- Basic understanding of Blender's Python API

## Usage

1. Open Blender.
2. Switch to the Scripting workspace.
3. Create a new text block.
4. Copy and paste the provided script into the text block.
5. Click the "Run Script" button.

## Script Explanation

The script performs the following steps:

1. Imports the necessary modules (`bpy` for Blender and `random` for random number generation).
2. Sets the spacing between the buildings to `2.2`.
3. Iterates over a 10x10 grid to create buildings at each grid point.
4. For each grid point:
   - Calculates a random height for the building.
   - Adds a cube primitive at the calculated location with the specified size and scale.
   - Assigns a random material to the building from four possible materials.

## Code

```python
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
```

## Customization

- **Grid Size:** Change the range values in the `for` loops to create a different grid size.
- **Building Spacing:** Modify the `spacing` variable to adjust the distance between buildings.
- **Building Size:** Adjust the `size` parameter in `bpy.ops.mesh.primitive_cube_add` to change the size of the buildings.
- **Material Probability:** Adjust the probabilities in the `if-elif-else` statements to change the likelihood of each material being applied.
