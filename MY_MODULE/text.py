import shutil

terminal_width = shutil.get_terminal_size().columns #terminal size

def heading(text):
    padding = (terminal_width - len(text)) // 2 #padding on the left
    centered_text = ' ' * padding + text +  padding * ' ' # align center
    center_bold = f"\033[1m{centered_text.upper()}\033[0m" #bold
    
    return center_bold

def center_text(text):
    padding = (terminal_width - len(text)) // 2 #padding on the left
    centered_text = ' ' * padding + text # align center
    
    return centered_text
def line_text():
    line_text = '-' * terminal_width 
    return line_text

def colored_bg_text(text, bg_color):
    bg_colors = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "reset": "\033[0m"
    }
    return f"{bg_colors[bg_color]}{text}{bg_colors['reset']}"

def colored_text(text, color):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

# using
# print(line_text())
# print(colored_bg_text(heading("hotem management syetm☕"),"blue"))
# print(line_text())