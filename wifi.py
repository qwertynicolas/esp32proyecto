def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<ssid>', '<key>') # cambiar estas variables por las que correspondan
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))
