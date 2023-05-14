import os
import subprocess
from .base.abstract_converter import FileConverter


class Mp4ToMp3(FileConverter):
    async def convert(from_path, to_path) -> None:
        subprocess.call(["ffmpeg", "-y", "-i", from_path, to_path],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
