from textual.app import App, ComposeResult
from textual.widgets import Button, Static


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Press the button")
        button =  Button("Click Me", id="click_btn")
        button.styles.height = 20
        button.styles.width = 50
        yield button


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "click_btn":
            self.my_function()

    def my_function(self) -> None:
        self.notify("Button clicked!")
        print("Function called")


if __name__ == "__main__":
    MyApp().run()
