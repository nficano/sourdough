#!/bin/bash

# Setup script for devcontainer post-creation

# Create iPython profile directory and copy config
mkdir -p /home/vscode/.ipython/profile_default
cp .ipython/profile_default/ipython_config.py /home/vscode/.ipython/profile_default/ipython_config.py

# Install Python dependencies
pipenv install

# Setup direnv
direnv allow
direnv reload

echo "Setup complete!"
