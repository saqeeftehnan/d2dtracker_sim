import os
from glob import glob
from setuptools import setup

package_name = 'd2dtracker_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name), glob('rviz/*.rviz'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mohamed Abdelkader',
    maintainer_email='mohamedashraf123@gmail.com',
    description='ROS 2 simulation packge of the D2DTracker system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gz_sim = d2dtracker_sim.gz_sim:main',
            'tf_node = d2dtracker_sim.tf_node:main',
            'microdds = d2dtracker_sim.microdds:main',
        ],
    },
)
