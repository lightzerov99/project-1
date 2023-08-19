

PowerRated = 60000
NumberMPPT = 6
IMPMAX = 21
VOC = 550
VMP = 500
ISC = 22

IMP = round(PowerRated/NumberMPPT/VMP,1) 

## pip install kivy==1.11.0
##pip install Cython==0.29.9

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Variables
        self.variables = ['PowerRated', 'NumberMPPT', 'IMPMAX', 'VOC', 'VMP', 'ISC']
        self.inputs = {}

        for var in self.variables:
            box = BoxLayout()
            label = Label(text=var)
            text_input = TextInput(hint_text=f"Enter {var}")
            box.add_widget(label)
            box.add_widget(text_input)
            self.inputs[var] = text_input
            layout.add_widget(box)

        # Buttons
        start_btn = Button(text="Start", on_press=self.start_action)
        stop_btn = Button(text="Stop", on_press=self.stop_action)
        
        layout.add_widget(start_btn)
        layout.add_widget(stop_btn)

        return layout

    def start_action(self, instance):
        for var, input in self.inputs.items():
            print(f"{var}: {input.text}")
        print("Started!")

    def stop_action(self, instance):
        print("Stopped!")

if __name__ == '__main__':
    MyApp().run()