# framework/export.py

class Exporter:
    @staticmethod
    def save(video, output_path):
        video.write_videofile(output_path, codec='libx264')
