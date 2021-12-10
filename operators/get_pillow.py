import os
from subprocess import call
import sys

import bpy
from .. import globs

PYTHON_PATH = sys.executable


class InstallPIL(bpy.types.Operator):
    bl_idname = 'smc.get_pillow'
    bl_label = 'Install PIL'
    bl_description = 'Click to install Pillow. This could take a while and might require you to start Blender as admin'

    def execute(self, context):
        try:
            import pip
            try:
                from PIL import Image, ImageChops
            except ImportError:
                call([PYTHON_PATH, '-m', 'pip', 'install',
                      'Pillow', '--user', '--upgrade'], shell=True)
        except ImportError:
            call([PYTHON_PATH, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'get_pip.py'),
                  '--user'], shell=True)
            call([PYTHON_PATH, '-m', 'pip', 'install',
                  'Pillow', '--user', '--upgrade'], shell=True)
        globs.smc_pi = True
        self.report({'INFO'}, 'Installation complete')
        return {'FINISHED'}
