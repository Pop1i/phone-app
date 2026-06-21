from textual.app import App, ComposeResult
from textual.widgets import Button, Static


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Press the button")
        button =  Button("Click Me", id="click_btn")
        button.styles.height = 20
        button.styles.width = 50
        yield button

        button2 =  Button("Click Me", id="click_btn2")
        button2.styles.height = 20
        button2.styles.width = 50
        yield button2


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "click_btn":
            self.my_function()
        elif event.button.id == "click_btn2":
            self.notify("YEAH!!!")

    def my_function(self) -> None:
        self.notify("Button clicked!")
        print("Function called")


if __name__ == "__main__":
    MyApp().run()
