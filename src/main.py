# Initialize the LibreOffice extension.

import uno
from src.ui.config_ui import show_config_modal

def start_extension():
    ctx = uno.getComponentContext()
    desktop = ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", ctx)
    doc = desktop.getCurrentComponent()
    show_config_modal(doc)

if __name__ == "__main__":
    start_extension()
