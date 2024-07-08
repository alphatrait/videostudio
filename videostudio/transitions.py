# videostudio/transitions.py

class Transition:
    def __init__(self, canvas, start_asset, end_asset, effect='crossfade', duration=1):
        self.start_asset = start_asset
        self.end_asset = end_asset
        self.effect = effect
        self.duration = duration

        canvas.add_transition(self)

    def apply_transition(self, clips):
        if self.effect == 'crossfade':
            start_index = self._find_clip_index(clips, self.start_asset)
            end_index = self._find_clip_index(clips, self.end_asset)

            if start_index is not None and end_index is not None:
                start_clip = clips[start_index].crossfadeout(self.duration)
                end_clip = clips[end_index].crossfadein(self.duration)
                clips[start_index] = start_clip
                clips[end_index] = end_clip

        return clips

    def _find_clip_index(self, clips, asset):
        for index, clip in enumerate(clips):
            if hasattr(clip, 'start') and clip.start == asset.start_time:
                return index
        return None

