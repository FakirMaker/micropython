import uos
from flashbdev import bdev


def check_bootsec():
    buf = bytearray(bdev.ioctl(5, 0))  # 5 is SEC_SIZE
    bdev.readblocks(0, buf)
    empty = True
    for b in buf:
        if b != 0xFF:
            empty = False
            break
    if empty:
        return True
    fs_corrupted()


def fs_corrupted():
    import time

    while 1:
        print(
            """\
The filesystem appears to be corrupted. If you had important data there, you
may want to make a flash snapshot to try to recover it. Otherwise, perform
factory reprogramming of MicroPython firmware (completely erase flash, followed
by firmware programming).
"""
        )
        time.sleep(3)


def setup():
    check_bootsec()
    print("Performing initial setup")
    uos.VfsLfs2.mkfs(bdev)
    vfs = uos.VfsLfs2(bdev)
    uos.mount(vfs, "/")
    with open("boot.py", "w") as f:
        f.write(
            """\
# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()
print('\033[35m', "\n\n     SD KART HAZIRLANIYOR     \n\n", '\033[0m')
import machine
import sys
from machine import SPI,Pin
import sdcard
import uos
spi = SPI(baudrate=100000,polarity=1,phase=0,sck=Pin(18),mosi=Pin(5),miso=Pin(19))
sd = sdcard.SDCard(spi,Pin(23))
uos.mount(sd,"/sd")
sys.path.append('/sd')
sys.path.remove("/lib")
sys.path.append('/sd/lib')
uos.chdir("/sd")
print("*************************************************\n\n SD Kart Hazır \n\n*************************************************")
import wifi
wifi.connect("SSR2265852","19nisan2016")
import uftpd
import mtime
"""
        )
    return vfs
