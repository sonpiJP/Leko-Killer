import ctypes
import os

YES = 6
result = ctypes.windll.user32.MessageBoxW(
    None,
    "Custom text",
    "Shutdown?",
    0x24 | 0x100,
)

if result == YES:
    os.system("shutdown /s /t 0")