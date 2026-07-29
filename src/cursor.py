import win32api
import win32con


class Cursor:

    def move(self, x, y):

        win32api.SetCursorPos(
            (x, y)
        )


    def left_click(self):

        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN,
            0,
            0,
            0,
            0
        )

        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTUP,
            0,
            0,
            0,
            0
        )


    def right_click(self):

        win32api.mouse_event(
            win32con.MOUSEEVENTF_RIGHTDOWN,
            0,
            0,
            0,
            0
        )

        win32api.mouse_event(
            win32con.MOUSEEVENTF_RIGHTUP,
            0,
            0,
            0,
            0
        )


    def press_down(self):

        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN,
            0,
            0,
            0,
            0
        )


    def press_up(self):

        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTUP,
            0,
            0,
            0,
            0
        )