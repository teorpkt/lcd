import drivers
from time import sleep
display = drivers.Lcd()

try:
    while True:
        print("Writing to display")

        display.lcd_display_string("CECI N'EST PAS", 1)
        display.lcd_display_string("DE L'ART.", 2)
        sleep(2)
        display.lcd_clear()
        sleep(1)

        display.lcd_display_string("C'EST TOUJOURS", 1)
        display.lcd_display_string("PAS DE L'ART.", 2)
        sleep(2)
        display.lcd_clear()
        sleep(1)

        display.lcd_display_string("ALLEZ, ARRETEZ", 1)
        display.lcd_display_string("DE ME REGARDER !", 2)
        sleep(2)
        display.lcd_clear()
        sleep(1)

        display.lcd_display_string("CE N'EST PAS DE", 1)
        display.lcd_display_string("L'ART.", 2)
        sleep(2)
        display.lcd_clear()
        sleep(1)

        display.lcd_display_string("DEGAGEZ !", 1)
        sleep(2)
        display.lcd_clear()
        sleep(1)


except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
