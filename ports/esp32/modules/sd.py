import machine
import sys
from machine import SPI,Pin
import sdcard
import uos
print('\033[35m', "\n\n     SD KART HAZIRLANIYOR     \n\n", '\033[0m')
spi =SPI(1,baudrate=500000,polarity=0,phase=0,sck=Pin(18),mosi=Pin(5),miso=Pin(19))
sd = sdcard.SDCard(spi,Pin(23))
uos.mount(sd,"/sd")
sys.path.append('/sd')
sys.path.remove("/lib")
sys.path.append('/sd/lib')
uos.chdir("/sd")
print("*************************************************\n\n SD Kart Hazır \n\n*************************************************")
