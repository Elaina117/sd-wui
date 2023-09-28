import os
from pathlib import Path

from modules.paths_internal import script_path


def is_restartable() -> bool:
    """
    Return True if the wui is restartable (i.e. there is something watching to restart it with)
    """
    return bool(os.environ.get('SD_wui_RESTART'))


def restart_program() -> None:
    """creates file tmp/restart and immediately stops the process, which wui.bat/wui.sh interpret as a command to start wui again"""

    (Path(script_path) / "tmp" / "restart").touch()

    stop_program()


def stop_program() -> None:
    os._exit(0)
