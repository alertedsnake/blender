bl_info = {
    "name":         "Remove Empty Vertex Groups",
    "author":       "alertedsnake",
    "blender":      (2, 80, 0),
    "category":     "Object",
    "version":      (0,1,0),
    "description":  "Removes empty vertex groups from a mesh object",
}

import bpy

class RemoveEmptyVertexGroups(bpy.types.Operator):
    """Removes empty vertex groups on all selected objects owo"""
    bl_idname = "object.rm_vertexemptygroups"
    bl_label = "Remove Empty Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}


    def group_has_verts(self, obj, index):
        for v in obj.data.vertices:
            if index in [vg.group for vg in v.groups]:
                return True
        return False


    def execute(self, context):
        assert bpy.context.mode == 'OBJECT', "Must be in object mode!"

        for obj in bpy.context.selected_objects:
            if obj.type != 'MESH': continue

            for vg in obj.vertex_groups:
                if self.group_has_verts(obj, vg.index):
                    continue

                print(f"Deleting empty vertex group {vg.name}")
                obj.vertex_groups.remove(vg)

        # Lets Blender know the operator finished successfully.
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RemoveEmptyVertexGroups.bl_idname)


def register():
    bpy.utils.register_class(RemoveEmptyVertexGroups)

    # Adds the new operator to an existing menu
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(RemoveEmptyVertexGroups)


if __name__ == "__main__":
    register()
