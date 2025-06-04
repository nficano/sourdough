<p align="center">
  <img src="https://assets.nickficano.com/sourdough.svg" alt="Sourdough Logo">
</p>

<style>
@media (prefers-color-scheme: dark) {
  img[alt="Sourdough Logo"] {
    filter: brightness(0) saturate(100%);
  }
}

@media (prefers-color-scheme: light) {
  img[alt="Sourdough Logo"] {
    filter: brightness(0) invert(1);
  }
}
</style>

# 🍞 Sourdough

A Python cookiecutter template for creating extremely minimal yet well-configured Python projects. Perfect for when you want to start lean but still have a great development experience.

## ✨ Features

### 🐍 Python Development Environment
- **Python 3.12** base environment
- **Pipenv** for dependency management and virtual environments
- **DevContainer** support for consistent development across machines

### 🎨 Code Quality & Formatting
- **Black** code formatter (80 character line length)
- **isort** import sorting
- **Flake8** linting
- **Pylint** static analysis
- **Ruff** fast Python linter

### 🧑‍💻 Enhanced Developer Experience
- **Custom IPython configuration** with Catppuccin Mocha theme
- **Auto-reload** extension for development
- **Enhanced completion** with Jedi
- **Better exception handling** with context mode
- **Custom prompt styling** and color schemes

### 🔧 VS Code Integration
Pre-configured extensions:
- Python language support with Pylance
- Docker integration
- Auto-docstring generation
- TOML syntax highlighting

## 🚀 Quick Start

### Prerequisites
Install cookiecutter if you haven't already:
```bash
pip install cookiecutter
```

### Create a New Project
```bash
cookiecutter https://github.com/your-username/sourdough
```

### Template Questions
The cookiecutter will ask you your project name and that's it!

## 🐳 Using the DevContainer

### In VS Code
1. Open the generated project in VS Code
2. Install the "Dev Containers" extension if you haven't already
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
4. Type "Dev Containers: Reopen in Container"
5. Select the command and wait for the container to build

The DevContainer will automatically:
- Set up Python 3.12 environment
- Install all development tools (Black, Flake8, isort, etc.)
- Configure VS Code with the right extensions and settings
- Set up Pipenv for dependency management
- Run any post-creation setup scripts

### What's Included in the Container
- **Base Image**: Python 3.12 on Debian Bullseye
- **Tools**: Black, Flake8, isort, Pipenv, direnv
- **Extensions**: Complete Python development suite

## 🎯 Key Customizations

### IPython Configuration
The template includes a heavily customized IPython setup featuring:
- **Catppuccin Mocha theme** for beautiful syntax highlighting
- **Auto-reload extension** for seamless development
- **Enhanced completion** with greedy matching
- **Better error handling** with context mode
- **Custom prompt styling** with execution counters
- **Useful aliases** (ll, la, cls, etc.)

### Code Style
- **Black formatter** with 80-character line length
- **isort** configured to work with Black
- **Consistent styling** across the entire project

### Development Workflow
- **Pipenv** manages dependencies and virtual environments
- **VS Code workspace** settings for Python development

## 📁 Project Structure

```
your-project/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   └── setup.sh
├── .ipython/
│   └── profile_default/
│       └── ipython_config.py
├── pyproject.toml
├── Pipfile
├── README.md
└── src/
    └── your_package/
        └── __init__.py
```

## 🛠️ Local Development (without DevContainer)

If you prefer to develop locally without the DevContainer:

1. Install Pipenv:
   ```bash
   pip install pipenv
   ```

2. Install dependencies:
   ```bash
   pipenv install --dev
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Start coding!
