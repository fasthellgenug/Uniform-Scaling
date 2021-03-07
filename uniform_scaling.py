import bpy

class OBJECT_OT_uniform_scaling(bpy.types.Operator):
    """Scaling an object uniformly on all axes based on one axis."""
    bl_idname = "transform.uniform_scaling"
    bl_label = "Uniform Scaling"
    bl_options = {"REGISTER","UNDO"}
    
    axis: bpy.props.EnumProperty(
        items = [('0','X','x-axis'), 
                 ('1','Y','y-axis'),
                 ('2','Z','z-axis')],
        name="Axis",
        description="Base axis for scaling"
    )
    size: bpy.props.FloatProperty(
        name = "New size",
        description = "New object size in the set dimension",
        default = 0
    )
    apply_scale: bpy.props.BoolProperty(
        name = "Apply scale",
        description = "Apply scale automatically",
        default = True
    )


    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        bpy.context.view_layer.update()
        
        obj = bpy.context.object
        print(obj)
        ax = int(self.axis)

        if (self.size==0):
            self.size = obj.dimensions[ax]    

        newSize = self.size
        oldSize = context.object.dimensions[ax]
        scale = newSize / oldSize
        obj.scale.xyz = (scale)
        if(self.apply_scale):
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        return {'FINISHED'}

def object_tansform_menu_draw(self, context):
    self.layout.operator("transform.uniform_scaling")


def register():
    bpy.utils.register_class(OBJECT_OT_uniform_scaling)
    bpy.types.VIEW3D_MT_transform_object.append(object_tansform_menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_uniform_scaling)
    bpy.types.VIEW3D_MT_transform_object.remove(object_tansform_menu_draw)


if __name__ == "__main__":
    register()

    #test call
    #bpy.ops.transform.uniform_scaling()

