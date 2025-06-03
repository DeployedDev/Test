import tkinter as tk
import ctypes
import ctypes.wintypes as wintypes
import win32api
import win32gui

# Constants from Windows Shell API
ABM_NEW = 0x00000000       # Register a new AppBar
ABM_SETPOS = 0x00000003    # Set the AppBar position
ABE_TOP = 1                # Dock the AppBar to the top of the screen


# Define the APPBARDATA structure for use with SHAppBarMessage
class APPBARDATA(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),            # Size of the structure
        ("hWnd", ctypes.c_void_p),            # Handle to the window being registered
        ("uCallbackMessage", ctypes.c_uint),  # Not used in this case
        ("uEdge", ctypes.c_uint),             # Which edge of the screen to dock to
        ("rc", wintypes.RECT),                # Rectangle of the AppBar's position
        ("lParam", ctypes.c_int),             # Not used
    ]


# Makes the banner behave like a taskbar by docking it to the top of the screen
def register_appbar(hwnd: int, height: int) -> None:
    screen_width = win32api.GetSystemMetrics(0)  # Get screen width in pixels
    rect = wintypes.RECT(0, 0, screen_width, height)  # Define AppBar rectangle

    # Set up the APPBARDATA structure
    data = APPBARDATA()
    data.cbSize = ctypes.sizeof(APPBARDATA)
    data.hWnd = hwnd
    data.uEdge = ABE_TOP
    data.rc = rect

    # Register and position the AppBar
    ctypes.windll.shell32.SHAppBarMessage(ABM_NEW, ctypes.byref(data))
    ctypes.windll.shell32.SHAppBarMessage(ABM_SETPOS, ctypes.byref(data))

    # Physically move the window to the top of the screen
    win32gui.MoveWindow(hwnd, rect.left, rect.top, rect.right, rect.bottom, True)


# Creates and displays the top banner
def create_banner() -> None:
    root = tk.Tk()  # Initialize main Tkinter window
    root.title("Classification Banner")

    screen_width = root.winfo_screenwidth()  # Get screen width
    height = 15  # Height of the banner in pixels

    # Set the window geometry to be full-width and fixed height
    root.geometry(f"{screen_width}x{height}+0+0")

    # Remove window borders and keep on top of all other windows
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="green")

    # Get native window handle and register it as an AppBar
    hwnd = root.winfo_id()
    register_appbar(hwnd, height)

    # Create a label for the classification text
    label = tk.Label(
        root,
        text="Restricted",
        fg="white",
        bg="green",
        font=("Segoe UI", 12, "bold")
    )
    label.pack(fill=tk.BOTH, expand=True)

    clicked = False  # Track whether the banner was clicked

    # Update clicked flag when label is clicked
    def on_click(_: tk.Event) -> None:
        nonlocal clicked
        clicked = True

    # Close the window if Escape is pressed after clicking the label
    def on_escape(_: tk.Event) -> None:
        if clicked:
            root.destroy()

    # Bind events
    label.bind("<Button-1>", on_click)
    root.bind("<Escape>", on_escape)

    # Start the Tkinter main loop
    root.mainloop()


# Run the banner if this script is executed directly
if __name__ == "__main__":
    create_banner()
