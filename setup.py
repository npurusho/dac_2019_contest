from setuptools import setup, find_packages
from distutils.dir_util import copy_tree
import os
import shutil

# global variables
overlay_folder = f'overlay/pynquser'
images_folder = f'images'
results_folder = f'result'
notebooks_folder = f'pynquse'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
hw_data_files = []


# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(overlay_folder, '')
    dst_ol_dir = os.path.join('pynquser', 'bitstream')
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])


# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(notebooks_folder, '')
    dst_nb_dir = os.path.join(board_notebooks_dir, 'pynquser')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)
    
# copy images
def copy_images():
    src_ol_dir = os.path.join(images_folder, '')
    dst_ol_dir = os.path.join('pynquser', 'images')
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

# copy results folder
def copy_results():
    src_ol_dir = os.path.join(results_folder, '')
    dst_ol_dir = os.path.join('pynquser', 'result')
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

copy_overlays()
copy_notebooks()
copy_images()
copy_results()

setup(
    name="dac_2019_contest",
    version='1.0',
    install_requires=['pynq>=2.3'],
    url='',
    license='BSD 3-Clause License',
    author=" ",
    author_email="",
    packages=find_packages(),
    package_data={
        '': hw_data_files,
    },
    description="Base design example for DAC 2019 SDC"
)
