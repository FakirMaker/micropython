import network
import time
import crypto
    
def connect(ssid,password,timeout=5000):
    print('\033[32m',"\n\n     KABLOSUZ AĞ HAZIRLANIYOR     \n\n",'\033[0m')
    wifi = network.WLAN(network.STA_IF)
    if wifi.isconnected() == True:
        print('\033[37m',"Ağ zaten bağlı durumda")
        return True
    wifi.active(True)
    wifi.connect(ssid,password)
    t = time.ticks_ms()
    while wifi.isconnected() == False:
        if time.ticks_diff(time.ticks_ms(), t) > timeout:
            wifi.disconnect()
            return False
    print("*************************************************\nKablosuz ağ bağlandı\n")
    print("IP Adresi:{}\nModem Adresi:{}\nSub Mask:{}".format(wifi.ifconfig()[0],wifi.ifconfig()[2],wifi.ifconfig()[1]))
    print("\n*************************************************")
    return True
    
def config():
    mwifi = network.WLAN(network.STA_IF)
    mwifi.active(True)
    print('\033[37m'"Kullanılabilir ağlar bulunuyor...")
    print("---------------------------------")
    wifi_list = mwifi.scan()
    for x in range(len(wifi_list)):
        print("{}.{}".format(x+1,str(wifi_list[x][0],'utf-8')))
    print("---------------------------------")
    try:
        ssidn = int(input("Ağ numarasını girin: "))
    except ValueError:
        ssidn = len(wifi_list)+1
    if ssidn > len(wifi_list) or ssidn < 1:
        while ssidn>len(wifi_list) or ssidn < 1:
            try:
                ssidn = int(input("Lütfen {} ile {} arasında bir numara girin: ".format(1,len(wifi_list))))
            except ValueError:
                ssidn = len(wifi_list)+1
    ssid = str(wifi_list[ssidn-1][0],'utf-8')
    psw = input("Lütfen [{}] isimli ağın parolasını girin: ".format(ssid))
    if connect(ssid,psw)==True:
        try:
            file = open("wifi_config","w")
            file.write(crypto.encode(ssid+"."+psw))
        except OSError:
            print("Kayıt hatası.")
        finally:
            file.close()   
    else:
        print('\033[31m',"Wifi bağlanamadı lütfen Ağ adı ve parolayı yeniden girin")
        config()
    
        
try:
    file = open("wifi_config","r")
    credidentials = crypto.decode(file.read());
    crd = credidentials.split(".")
    file.close()
    if connect(crd[0],crd[1])==False:
        print('\033[31m',"Wifi bağlanamadı lütfen Ağ adı ve parolayı yeniden girin")
        config()
    
except OSError:
    print('\033[31m',"Wifi ağ adı ve parola kayıtlı değil kayıt için lütfen aşağıdaki ağlardan birisini seçin")    
    config()       
 