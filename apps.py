import os
import subprocess
from pathlib import Path

def open_folder(folder_name):

    home = Path.home()

    folders = {
        "desktop": home / "OneDrive" / "Desktop",
        "downloads": home / "Downloads",
        "documents": home / "Documents",
        "pictures": home / "Pictures",
        "videos": home / "Videos",
        "music": home / "Music",
        "onedrive": home / "OneDrive",
        "project": home / "OneDrive" / "Desktop" / "pt",
        "my project": home / "OneDrive" / "Desktop" / "pt",
    }

    folder_name = folder_name.lower().strip()

    # Known folder name
    if folder_name in folders:
        path = folders[folder_name]

    else:
        # Search common locations for a folder with that name
        search_locations = [
            home / "Desktop",
            home / "OneDrive" / "Desktop",
            home / "Documents",
            home / "Downloads",
            home / "OneDrive",
        ]

        path = None

        for location in search_locations:
            candidate = location / folder_name

            if candidate.is_dir():
                path = candidate
                break

    if path and path.is_dir():
        os.startfile(str(path))
        return True

    return False
def open_application(app_name):

    apps = {
        # Windows apps
        "calculator": ["calc.exe"],
        "notepad": ["notepad.exe"],
        "paint": ["mspaint.exe"],
        "file explorer": ["explorer.exe"],
        "command prompt": ["cmd.exe"],
        "task manager": ["taskmgr.exe"],
        "settings": ["cmd", "/c", "start", "ms-settings:"],
        "control panel": ["control.exe"],
        "snipping tool": ["SnippingTool.exe"],
        "wordpad": ["write.exe"],

        # Microsoft Office (if installed)
        "word": ["cmd", "/c", "start", "", "winword"],
        "excel": ["cmd", "/c", "start", "", "excel"],
        "powerpoint": ["cmd", "/c", "start", "", "powerpnt"],
        "outlook": ["cmd", "/c", "start", "", "outlook"],

        # Other common apps (if installed and available)
        "vlc": ["cmd", "/c", "start", "", "vlc"],
        "spotify": ["cmd", "/c", "start", "", "spotify"],
        "discord": ["cmd", "/c", "start", "", "discord"],
        "whatsApp": ["cmd", "/c", "start", "", "whatsApp"],
    }

    try:
        if app_name in apps:
            subprocess.Popen(apps[app_name], shell=False)

        elif app_name in ["vscode", "visual studio code"]:
            subprocess.Popen(["code"])

        elif app_name == "chrome":
            # Chrome ko Windows ke registered app command se open karne ki koshish
            subprocess.Popen(
                ["cmd", "/c", "start", "", "chrome"],
                shell=False
            )

        elif app_name == "edge":
            subprocess.Popen(
                ["cmd", "/c", "start", "", "msedge"],
                shell=False
            )

        elif app_name == "firefox":
            subprocess.Popen(
                ["cmd", "/c", "start", "", "firefox"],
                shell=False
            )

        else:
            return False

        return True

    except (OSError, subprocess.SubprocessError):
        return False