from setuptools import find_packages, setup

package_name = 'quadcopter_kestabilan'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phasya',
    maintainer_email='phasya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "imu_pub = quadcopter_kestabilan.imu_publisher:main",
            "attitude_monitor = quadcopter_kestabilan.attitude_monitor:main",
            "logger = quadcopter_kestabilan.logger_node:main"
        ],
    },
)
