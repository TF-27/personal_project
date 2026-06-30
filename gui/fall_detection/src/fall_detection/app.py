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
        #self.alarm_box = toga.Box(style=toga.style.Pack(direction=COLUMN, align_items=CENTER, flex=1))
        #self.alarm_box.add(toga.Box(style=toga.style.Pack(flex=1)))
        #self.alarm_box.style.height = 0 # boots suggested fix to the pop-up issue

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



#need to reset the window after the buttons are pressed!


        self.main_box.add(activate_button)
        self.main_box.add(settings_button)
        #self.main_box.add(self.alarm_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.settings_window = None
        self.alarm_window = None
        self.main_window.show()


# UPGRADE THIS TO ACTUALLY RESPOND TO A FALL WITHIN THE DATASET!
    async def run_detect(self, widget):
        await self.main_window.dialog(
            toga.InfoDialog(
                "Fall Detection","Running cvs testset"
            )
        )
        if detect_fall():
            await self.show_alarm()
            #self.main_box.add(self.alarm_box) # Boots made me remove this for the popup issue
            ##self.alarm_box.style.height = 300 == second solution remove
            #self.main_box.refresh()
            ##self.main_window.content.refresh() #boots solution to the popup issue == second solution remove
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
        self.alarm_window.close()
        self.alarm_window = None

    async def call_ec(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog(f"Messaging {self.contact_object.name}!",f"GPS coordinates attached to message")
        )
        self.alarm_window.close()
        self.alarm_window = None

    async def safe_response(self, widget):

        await self.main_window.dialog(
            toga.InfoDialog("I'm safe!","No calls made or messages sent, fall detection is active"), #currently not true
        )
        self.alarm_window.close()
        self.alarm_window = None


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
            
            namec_box = toga.Box(style=toga.style.Pack(direction=ROW), margin=5) # before pop-up issue boots corection: namec_box = toga.Box(direction=ROW, margin=5)
            namec_box.add(self.name_contact)

            numberc_box = toga.Box(style=toga.style.Pack(direction=ROW), margin=5) # before pop-up issue boots correction: numberc_box = toga.Box(direction=ROW, margin=5)
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

    async def show_alarm(self):
        if self.alarm_window is not None:
            self.alarm_window.show()
            return
        
        
        self.alarm_window = toga.Window(title="Fall Detected!")
        alarm_box = toga.Box(style=toga.style.Pack(direction=COLUMN, align_items=CENTER))

        call_112_button = toga.Button(
            "Call 112!",
            on_press= self.call_112,
            style=toga.style.Pack(background_color="red", color="black", margin=5)
        )

        call_ec_button = toga.Button(
            f"Message {self.contact_object.name}!",
            on_press= self.call_ec,
            style=toga.style.Pack(background_color="orange", color="black", margin=5)
        )

        safe_button = toga.Button(
            "No help needed - I'm safe!",
            on_press= self.safe_response,
            style=toga.style.Pack(background_color="green", color="black", margin=5)
        )        
        
        alarm_box.add(call_112_button)
        alarm_box.add(call_ec_button)
        alarm_box.add(safe_button)
        alarm_box.add(toga.Box(style=toga.style.Pack(flex=1)))
        
        self.alarm_window.content = alarm_box
        self.alarm_window.show()

def main():
    return FallDetection()
