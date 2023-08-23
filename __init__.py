# https://github.com/yunkezengren/Blender-align-node
bl_info = {
    "name" : "Node Align",
    "author" : "原作者:Kuldeep Singh; 修改:一尘不染 云可赠人",
    "description" : "align node  Shift Q | Ctrl Q",
    "blender" : (2, 83, 0),
    "version" : (0, 0, 1),
    "location": "Nodes Editor",
    "category": "Node",
    "warning":  "This version is still in development."
}

from . import auto_load

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
