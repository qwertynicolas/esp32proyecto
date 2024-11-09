def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'key') # variables del wifi 
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))
