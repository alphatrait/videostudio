# videostudio/transitions.py

class Transition:
    def __init__(self, canvas, start_asset, end_asset, effect='crossfade', duration=1):
        self.start_asset = start_asset
        self.end_asset = end_asset
        self.effect = effect
        self.duration = duration
        canvas.add_transition(self)

    def apply_transition(self, clips):
        start_index = self._find_clip_index(clips, self.start_asset)
        end_index = self._find_clip_index(clips, self.end_asset)

        if start_index is not None and end_index is not None:
            if self.effect == 'crossfade':
                clips[start_index] = clips[start_index].crossfadeout(self.duration)
                clips[end_index] = clips[end_index].crossfadein(self.duration)
            elif self.effect == 'wipe':
                clips[end_index] = clips[end_index].set_mask(self._create_wipe_mask(clips[end_index], 'left'))
            elif self.effect == 'slide':
                clips[start_index] = clips[start_index].fl_time(lambda t: t if t < self.duration else t - self.duration)
                clips[end_index] = clips[end_index].fl_time(lambda t: t if t > clips[end_index].duration - self.duration else t + self.duration)

        return clips

    def _find_clip_index(self, clips, asset):
        for index, clip in enumerate(clips):
            if hasattr(clip, 'start') and clip.start == asset.start_time:
                return index
        return None

    def _create_wipe_mask(self, clip, direction):
        from moviepy.editor import ColorClip
        from moviepy.video.fx.all import crop

        mask = ColorClip(clip.size, color=1, duration=self.duration, is_mask=True)
        if direction == 'left':
            wipe_fx = lambda get_frame, t: crop(get_frame(t), x1=int(t / self.duration * clip.size[0]), width=clip.size[0])
        elif direction == 'right':
            wipe_fx = lambda get_frame, t: crop(get_frame(t), x2=int(t / self.duration * clip.size[0]))
        elif direction == 'top':
            wipe_fx = lambda get_frame, t: crop(get_frame(t), y1=int(t / self.duration * clip.size[1]))
        elif direction == 'bottom':
            wipe_fx = lambda get_frame, t: crop(get_frame(t), y2=int(t / self.duration * clip.size[1]))

        return mask.fl(wipe_fx)
