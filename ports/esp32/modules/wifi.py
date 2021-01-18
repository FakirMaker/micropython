def connect(ssid,password):
    import network
    print('\033[35m',"\n\n     KABLOSUZ AĞ HAZIRLANIYOR     \n\n",'\033[0m')
    wifi = network.WLAN(network.STA_IF)
    if wifi.isconnected() == True:
        print("Ağ zaten bağlı durumda")
        return
    wifi.active(True)
    wifi.connect(ssid,password)
    while wifi.isconnected() == False:
        pass
    print("*************************************************\nKablosuz ağ bağlandı\n")
    print("IP Adresi:{}\nModem Adresi:{}\nSub Mask:{}".format(wifi.ifconfig()[0],wifi.ifconfig()[2],wifi.ifconfig()[1]))
    print("\n*************************************************")
