import toga

def send_telemetrydata(widget):
    # Send telemetry data to Google Cloud
    print("Sending telemetry data")

def build(app):
    s_box = toga.Box()
    main_box = toga.Box()

    s_label = toga.Label('Trackersweb')
    s_switch = toga.Switch('Start Tracking', id='com.trackersweb.trackit.slider', on_toggle=send_telemetrydata, is_on=False)

    s_box.add(s_label)
    s_box.add(s_switch)

    main_box.add(s_box)

    return main_box

def main():
    return toga.App('Trackersweb', 'com.trackersweb.trackit', startup=build)

if __name__ == '__main__':
    main().main_loop()
