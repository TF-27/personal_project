"""
6-phase fall detection with accelerometer and gyoscope [Tseng, Huang and Kau, 2025]
"""

import toga
from toga.style.pack import COLUMN, ROW
from .fall_detection import detect_fall


class FallDetection(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        activate_button = toga.Button(
            "Activate App!",
            on_press=self.run_detect,
            margin=5
        )

        main_box.add(activate_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def run_detect(self, widget):
        await self.main_window.dialog(
            toga.InfoDialog(
                f"Running cvs testset: {detect_fall()}",
                "Run completed"
            )
        )


def main():
    return FallDetection()
