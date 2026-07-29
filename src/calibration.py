from screeninfo import get_monitors


class Calibration:

    def __init__(self, margin=100):

        monitor = get_monitors()[0]

        self.screen_width = monitor.width
        self.screen_height = monitor.height

        self.margin = margin

    def map_point(self, x, y, frame_width, frame_height):

        usable_width = frame_width - (2 * self.margin)
        usable_height = frame_height - (2 * self.margin)

        x = max(self.margin, min(frame_width - self.margin, x))
        y = max(self.margin, min(frame_height - self.margin, y))

        x = (x - self.margin) / usable_width
        y = (y - self.margin) / usable_height

        screen_x = int(x * self.screen_width)
        screen_y = int(y * self.screen_height)

        return screen_x, screen_y