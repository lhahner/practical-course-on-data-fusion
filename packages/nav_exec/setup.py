from setuptools import find_packages, setup

package_name = 'nav_exec'

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
    maintainer='w',
    maintainer_email='w@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'navigation_executor = nav_exec.navigation_executor:main',
        'straight_path_pub = nav_exec.straight_path_pub:main',
        ],
    },
)
