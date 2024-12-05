#!/usr/bin/env python3
import os
import subprocess

def setup_submodules():
    """Initialize and update git submodules"""
    subprocess.run(['git', 'submodule', 'init'])
    subprocess.run(['git', 'submodule', 'update'])

def setup_frontend():
    """Setup Apollon frontend"""
    os.chdir('apollon')
    subprocess.run(['yarn', 'install'])
    os.chdir('..')

def setup_backend():
    """Setup BESSER backend"""
    os.chdir('besser')
    subprocess.run(['python', 'setup_environment.py'])
    os.chdir('..')

if __name__ == '__main__':
    setup_submodules()
    setup_frontend()
    setup_backend()
    print("Setup complete! Use 'docker-compose up' to start the platform") 