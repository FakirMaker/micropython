import machine
import ubinascii
from ucryptolib import aes

def generate_key():
    id_str = ubinascii.hexlify(machine.unique_id()).decode('utf-8') 
    id_str = id_str *5                                              
    id_str = id_str[:32] 
    return id_str

def encode(text):
    key=generate_key()
    cipher = aes(key, 1)
    pad = 16 - len(text) % 16
    text = text + " "*pad
    encrypted = cipher.encrypt(text)
    return encrypted
    
def decode(text):
    key = generate_key()
    cipher = aes(key, 1)
    decrypted = cipher.decrypt(text)
    return str(decrypted.rstrip(),'utf-8')