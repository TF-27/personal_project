"""
6-phase fall detection with accelerometer and gyoscope [Tseng, Huang and Kau, 2025]
"""

import toga
from toga.style.pack import COLUMN, ROW, CENTER
from .fall_detection import detect_fall
from .contact_info import ContactInfo


class FallDetection(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.contact_object = ContactInfo("No name given", "No number given") 
        #This will be replaced once we store the info on a file ofcourse
        self.main_box = toga.Box(style=toga.style.Pack(direction=COLUMN))
        self.alarm_box = toga.Box(style=toga.style.Pack(direction=COLUMN, align_items=CENTER, flex=1))
        self.alarm_box.add(toga.Box(style=toga.style.Pack(flex=1)))

        # Creating buttons
        activate_button = toga.Button(
            "Run test on csv dataset",
            on_press=self.run_detect,
            margin=5
        )

        settings_button = toga.Button(
            "Open settings",
            on_press=self.open_settings
        )


        call_112_button = toga.Button(
            "Bel 112!",
            on_press= self.call_112,
            style=toga.style.Pack(background_color="red", color="black", margin=5)
        )

        call_ec_button = toga.Button(
            f"Message {self.contact_object.name}!",
            on_press= self.call_ec,
            style=toga.style.Pack(background_color="orange", color="black", margin=5)
        )

        safe_button = toga.Button(
            "Geen hulp nodig",
            on_press= self.safe_response,
            style=toga.style.Pack(background_color="green", color="black", margin=5)
        )
#need to reset the window after the buttons are pressed!
        self.alarm_box.add(call_112_button)
        self.alarm_box.add(call_ec_button)
        self.alarm_box.add(safe_button)
        self.alarm_box.add(toga.Box(style=toga.style.Pack(flex=1)))

        self.main_box.add(activate_button)
        self.main_box.add(settings_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.settings_window = None
        self.main_window.show()


# UPGRADE THIS TO ACTUALLY RESPOND TO A FALL WITHIN THE DATASET!
    async def run_detect(self, widget):
        await self.main_window.dialog(
            toga.InfoDialog(
                "Fall Detection","Running cvs testset"
            )
        )
        if detect_fall():
            self.main_box.add(self.alarm_box) # To be moved to an actual detection later!
            self.alarm_box.style.height = 300
            self.main_box.refresh()
        else:
            await self.main_window.dialog(
                toga.InfoDialog(
                    "Finished detection","No fall detected"
                )
            )           
#working on integration now!!!!

    async def call_112(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("Calling 112!",f"Also sending message to inform {self.contact_object.name} of the call and your GPS location")
        )

    async def call_ec(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog(f"Messaging {self.contact_object.name}!",f"GPS coordinates attached to message")
        )

    async def safe_response(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("I'm safe!'","No calls made or messages sent, fall detection is active"), #currently not true
        )


    def open_settings(self, widget):
        if self.settings_window is None:
            self.settings_window = toga.Window(title="Settings")
            self.settings_box = toga.Box(style=toga.style.Pack(direction=COLUMN))

            namec_label = toga.Label(
                "Contact name: ",
                margin=(0, 5),
            )
            numberc_label = toga.Label(
                "Contact number: ",
                margin=(0, 5),
            )

            self.show_info = toga.Label(
                f"\n\nCurrent contact details:\n\nName: {self.contact_object.name}\nNumber: {self.contact_object.number}",
                margin=(0, 5),
            )

            self.name_contact = toga.TextInput(flex=1)
            self.number_contact = toga.TextInput(flex=1)
            
            namec_box = toga.Box(direction=ROW, margin=5)
            namec_box.add(self.name_contact)

            numberc_box = toga.Box(direction=ROW, margin=5)
            numberc_box.add(self.number_contact)

            contact_button = toga.Button(
                "Add contact (will overwrite existing!)",
                on_press=self.add_contact,
                margin=5,
            )

            self.settings_box.add(namec_label)
            self.settings_box.add(namec_box)
            self.settings_box.add(numberc_label)
            self.settings_box.add(numberc_box)
            self.settings_box.add(contact_button)
            self.settings_box.add(self.show_info)
                 
            self.settings_window.content = self.settings_box     
            self.settings_window.on_close = self.cleanup_settings
            self.settings_window.show()
        else:
            self.settings_window.show()

    def cleanup_settings(self, window):
        self.settings_window = None
        return True

    async def add_contact(self, widget): #no object generated at this point. Need to add the class as well.

        self.contact_object.name = self.name_contact.value
        self.contact_object.number = self.number_contact.value

        self.show_info.text = f"\n\nCurrent contact details:\n\nName: {self.contact_object.name}\nNumber: {self.contact_object.number}"
        await self.settings_window.dialog(
            toga.InfoDialog("Contact changed!",f"Name: {self.contact_object.name}\nNumber: {self.contact_object.number}")
        )



def main():
    return FallDetection()
