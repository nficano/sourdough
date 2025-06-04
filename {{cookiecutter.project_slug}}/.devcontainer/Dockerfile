FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Copy custom bashrc
COPY bashrc /home/vscode/.bashrc

# Set proper ownership
RUN chown -R vscode:vscode /home/vscode/.bashrc

# Switch to vscode user
USER vscode
