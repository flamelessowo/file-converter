import subprocess
from .base.abstract_converter import FileConverter


class Mp4ToCompress(FileConverter):
    async def convert(from_path, to_path) -> None:
        ffmpeg_cmd = [
        'ffmpeg',
        '-i', from_path,
        '-y',
        '-c:v', 'libx264',
        '-crf', '23',
        '-preset', 'medium',
        '-c:a', 'aac',
        '-b:a', '128k',
         to_path]
        try:
            subprocess.run(ffmpeg_cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {str(e)}")
