import sass
import os
import shutil

sass.compile(dirname=('static/scss', 'static/css'), output_style='compressed')

output_dir = 'docs'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

shutil.copytree('static', os.path.join(output_dir, 'static'))

shutil.copy('templates/index.html', output_dir)
