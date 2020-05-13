import shutil

source = 'default_template'
target = '/usr/share/jupyter/voila/templates'

shutil.copytree(source, target)
