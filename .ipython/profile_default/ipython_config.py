# Standard library imports
from copy import deepcopy

# IPython imports
import IPython  # type: ignore
import IPython.terminal.prompts as prompts  # type: ignore
from IPython.utils.PyColorize import linux_theme, theme_table  # type: ignore

# Prompt toolkit imports
import prompt_toolkit  # type: ignore
from prompt_toolkit.styles.pygments import pygments_token_to_classname  # type: ignore
from prompt_toolkit.styles.style import Style  # type: ignore
from pygments.token import Token  # type: ignore

# =============================================================================
# Configuration Setup
# =============================================================================

c = get_config()  # type: ignore # noqa # pylint:disable=E0602

# Basic terminal options
c.TerminalInteractiveShell.true_color = True
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalIPythonApp.display_banner = False

# Suppress all tips and informational messages
c.InteractiveShell.banner1 = ''
c.InteractiveShell.banner2 = ''

# =============================================================================
# Common Development Extensions & Settings
# =============================================================================

# Auto-reload extension for development (very popular!)
c.InteractiveShellApp.extensions = ['autoreload']

# Editor configuration
# Change to 'vim', 'nano', etc. as preferred
c.TerminalInteractiveShell.editor = 'code'

# Enhanced completion settings
c.IPCompleter.greedy = True
c.IPCompleter.use_jedi = True
c.IPCompleter.backslash_combining_completions = True

# Better exception handling
c.InteractiveShell.xmode = 'Context'  # More detailed tracebacks
c.TerminalInteractiveShell.show_rewritten_input = True

# Performance settings
c.InteractiveShell.ast_node_interactivity = 'last_expr'
c.InteractiveShell.automagic = True
c.InteractiveShell.autocall = 0

# Useful command aliases
c.AliasManager.user_aliases = [
    ('ll', 'ls -la'),
    ('la', 'ls -A'),
    ('l', 'ls -CF'),
    ('cls', 'clear'),
    ('..', 'cd ..'),
    ('...', 'cd ../..'),
]

# =============================================================================
# Catppuccin Mocha Color Palette
# =============================================================================


class CatppuccinMocha:
    """Catppuccin Mocha color palette constants."""

    # Base colors
    BASE = '#1e1e2e'
    MANTLE = '#181825'
    CRUST = '#11111b'

    # Text colors
    WHITE = '#cdd6f4'
    SUBTEXT0 = '#a6adc8'
    SUBTEXT1 = '#bac2de'

    # Surface colors
    SURFACE0 = '#313244'
    SURFACE1 = '#45475a'
    SURFACE2 = '#585b70'

    # Overlay colors
    OVERLAY0 = '#6c7086'
    OVERLAY1 = '#7f849c'
    OVERLAY2 = '#9399b2'

    # Accent colors
    BLUE = '#89b4fa'
    LAVENDER = '#b4befe'
    SAPPHIRE = '#74c7ec'
    SKY = '#89dceb'
    TEAL = '#94e2d5'
    GREEN = '#a6e3a1'
    YELLOW = '#f9e2af'
    PEACH = '#fab387'
    MAROON = '#eba0ac'
    RED = '#f38ba8'
    MAUVE = '#cba6f7'
    PINK = '#f5c2e7'
    FLAMINGO = '#f2cdcd'
    ROSEWATER = '#f5e0dc'

# =============================================================================
# Monkey Patching for Completion Colors Fix
# =============================================================================


def fix_completion_colors():
    """
    Fix completion highlighting as per https://github.com/ipython/ipython/issues/11526

    This monkey patches prompt toolkit's style function to properly handle
    completion menu colors in IPython.
    """
    def style_from_pygments_dict(pygments_dict):
        """Patched version that fixes completion colors."""
        pygments_style = []
        for token, style in pygments_dict.items():
            if isinstance(token, str):
                pygments_style.append((token, style))
            else:
                pygments_style.append(
                    (pygments_token_to_classname(token), style))
        return Style(pygments_style)

    # Apply the monkey patch
    prompt_toolkit.styles.pygments.style_from_pygments_dict = style_from_pygments_dict
    IPython.terminal.interactiveshell.style_from_pygments_dict = style_from_pygments_dict

# =============================================================================
# Custom Prompt Class
# =============================================================================


class CatppuccinPrompt(prompts.Prompts):
    """Custom prompt class with consistent formatting."""

    def in_prompt_tokens(self, cli=None):
        """Input prompt tokens."""
        return [(Token.Prompt, f"[{self.shell.execution_count}]: ")]

    def out_prompt_tokens(self, cli=None):
        """Output prompt tokens."""
        return [(Token.OutPrompt, f"[{self.shell.execution_count}]: ")]

# =============================================================================
# Theme Configuration
# =============================================================================


def setup_catppuccin_theme():
    """Set up the Catppuccin Mocha theme for IPython."""
    # Create the theme based on linux_theme
    catppuccin_mocha = deepcopy(linux_theme)
    catppuccin_mocha.base = "catppuccin-mocha"

    # Register the theme
    theme_table["catppuccin-mocha"] = catppuccin_mocha

    return catppuccin_mocha


def get_completion_menu_styles():
    """Get the completion menu style overrides."""
    colors = CatppuccinMocha

    return {
        'completion-menu': f'bg:{colors.BASE} {colors.WHITE}',
        'completion-menu.completion.current': f'bg:{colors.LAVENDER} {colors.CRUST}',
        'completion-menu.completion': f'bg:{colors.BASE} {colors.WHITE}',
        'completion-menu.meta.completion.current': f'bg:{colors.LAVENDER} {colors.CRUST}',
        'completion-menu.meta.completion': f'bg:{colors.BASE} {colors.WHITE}',
        'completion-menu.multi-column-meta': f'bg:{colors.BASE} {colors.WHITE}',
    }

# =============================================================================
# Apply Configuration
# =============================================================================


# Fix completion colors
fix_completion_colors()

# Set custom prompt
c.TerminalInteractiveShell.prompts_class = CatppuccinPrompt

# Set up theme
setup_catppuccin_theme()
c.TerminalInteractiveShell.colors = "catppuccin-mocha"

# Apply completion menu styling
c.TerminalInteractiveShell.highlighting_style_overrides = get_completion_menu_styles()
