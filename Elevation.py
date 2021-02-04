from pythonosc.udp_client import SimpleUDPClient

def send_message(message):
    ip = "192.168.17.116" # IP Will change dependiing upon target computer
    port = 6788

    client = SimpleUDPClient(ip, port) # Creating the OSC UDP Client

    client.send_message(":", message)
    
send_message(0.75)
