def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    serial.write_line("OKAY")
input.on_button_pressed(Button.A, on_button_pressed_a)
