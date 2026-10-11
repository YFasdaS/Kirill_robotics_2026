from setuptools import find_packages, setup
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
package_name = 'study_pkg'

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
    maintainer='infinion',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },

    Username for 'https://github.com': YFasdaS
Password for 'https://YFasdaS@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/YFasdaS/ROS_labs.git/'

    entry_points={
        'console_scripts': [
            'first_node = solozobov_robots_2026_study.scripts.first_node:main',   # ← добавляем эту строку

        ],
    },
)
