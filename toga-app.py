import toga

def send_telemetrydata(widget):
    # Send telemetry data to Google Cloud
    print("Sending telemetry data")

def build(app):
    main_box = toga.Box()

    main_label = toga.Label('Trackersweb.. track anything, anyscale')
    main_button = toga.Button('Track me!', on_press=send_telemetrydata)

    main_box.add(main_label)
    main_box.add(main_button)

    return main_box

def main():
    return toga.App('Trackersweb', 'com.trackersweb.trackit', startup=build)

if __name__ == '__main__':
    main().main_loop()
