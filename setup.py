import os

from setuptools import setup

redis_dirname = 'redis'

base_dir = os.path.dirname(os.path.abspath(__file__))
redis_dir = os.path.join(base_dir, redis_dirname)

setup(
    name='redis-bin',
    version='4.0.14',  # redis version
    url='https://github.com/alexsilva/redis',
    license='MIT',
    author='alex',
    author_email='alex@fabricadigital.com.br',
    description='redis executable.',
    data_files=[(
        redis_dirname, [
            os.path.join(redis_dir, "redis-cli.exe"),
            os.path.join(redis_dir, "redis-server.exe"),
            os.path.join(redis_dir, "github.txt")
        ]
    )]
)
