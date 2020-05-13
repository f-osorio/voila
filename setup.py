import shutil

source = 'default_template'
target = '/home/jovyan/.local/share/jupyter/voila/templates'

shutil.copytree(source, target)
