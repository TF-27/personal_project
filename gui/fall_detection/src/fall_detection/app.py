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
        self.main_box = toga.Box(style=toga.style.Pack(direction=COLUMN))
        self.alarm_box = toga.Box(style=toga.style.Pack(direction=COLUMN))


        # Creating buttons
        activate_button = toga.Button(
            "Activate App!",
            on_press=self.run_detect,
            margin=5
        )

        call_112_button = toga.Button(
            "Bel 112!",
            on_press= self.call_112
        )

        call_ec_button = toga.Button(
            "Bel NAAM!",
            on_press= self.call_ec
        )

        safe_button = toga.Button(
            "Geen hulp nodig",
            on_press= self.safe_response
        )

        self.alarm_box.add(call_112_button)
        self.alarm_box.add(call_ec_button)
        self.alarm_box.add(safe_button)

        self.main_box.add(activate_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


# UPGRADE THIS TO ACTUALLY RESPOND TO A FALL WITHIN THE DATASET!
    async def run_detect(self, widget):
        await self.main_window.dialog(
            toga.InfoDialog(
                f"Running cvs testset: {detect_fall()}",
                "Run completed",
            )
        )
        self.main_box.add(self.alarm_box) # To be moved to an actual detection later!
        self.alarm_box.style.height = 300
        self.main_box.refresh()

    async def call_112(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("Bel 112!","Call 112 function succesful\nStuur GPS locatie")
        )

    async def call_ec(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("Bel NAAM!","Bericht NAAM function succesful\nStuur alarm bericht en GPS locatie")
        )

    async def safe_response(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("Ik ben veilig","Niets ondernomen, app detecteert weer")
        )




def main():
    return FallDetection()
