import glfw

from src.Engine.Graphics import Eszett_graphics
from src.Engine.Input import Eszett_keyboard


class ESZETT_ENGINE_ENGINE:
    def __init__(
        self,
        width: int,
        height: int,
        fullscreen: bool,
        title: str,
        monitor,
        share,
        icon,
    ):

        # GLFW INIT
        glfw.init()

        # VAR
        self.ESZETT_WINDOW = None
        self.ESZETT_WINDOW_TITLE = title
        self.FPS_LAST_TIME = glfw.get_time()
        self.FPS_CURRENT_TIME = glfw.get_time()
        self.FPS_NUM_FRAMES = 0
        self.FPS_FRAME_TIME = 0

        self.build_glfw_window(
            width=width,
            height=height,
            fullscreen=fullscreen,
            title=title,
            monitor=monitor,
            share=share,
            icon=icon,
        )

        self.render()

    def build_glfw_window(
        self,
        width: int,
        height: int,
        fullscreen: bool,
        title: str,
        monitor,
        share,
        icon,
    ):
        if fullscreen:
            self.ESZETT_WINDOW = glfw.create_window(
                width=glfw.get_video_mode(glfw.get_primary_monitor()).size.width,
                height=glfw.get_video_mode(glfw.get_primary_monitor()).size.height,
                title=title,
                monitor=glfw.get_primary_monitor(),
                share=share,
            )
        else:
            self.ESZETT_WINDOW = glfw.create_window(
                width=width,
                height=height,
                title=title,
                monitor=monitor,
                share=share,
            )
        if icon is not None:
            glfw.set_window_icon(window=self.ESZETT_WINDOW, count=1, images=icon)

        glfw.make_context_current(window=self.ESZETT_WINDOW)

        if self.ESZETT_WINDOW is not None:
            print(f"ESZETT_WINDOW created. width={width}, height={height}")
        else:
            print("ESZETT_WINDOW failed to create.")

    def render(self):
        while not glfw.window_should_close(window=self.ESZETT_WINDOW):
            glfw.poll_events()
            Eszett_graphics.render()

            if Eszett_keyboard.is_pressed("esc"):
                self.close()

            self.calculate_framerate()
            glfw.swap_buffers(window=self.ESZETT_WINDOW)

    def calculate_framerate(self):
        self.FPS_CURRENT_TIME = glfw.get_time()
        delta = self.FPS_CURRENT_TIME - self.FPS_LAST_TIME

        if delta >= 1:
            framerate = max(1, int(self.FPS_NUM_FRAMES // delta))
            glfw.set_window_title(
                window=self.ESZETT_WINDOW,
                title=f"{self.ESZETT_WINDOW_TITLE}_____Running at {framerate} fps.",
            )
            self.FPS_LAST_TIME = self.FPS_CURRENT_TIME
            self.FPS_NUM_FRAMES = -1
            self.FPS_FRAME_TIME = 1000.0 / framerate

        self.FPS_NUM_FRAMES += 1

    def close(self):
        glfw.destroy_window(window=self.ESZETT_WINDOW)
        glfw.terminate()
