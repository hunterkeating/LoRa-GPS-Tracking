from pythonosc.udp_client import SimpleUDPClient

def send_angle(message):
    ip = "192.168.17.116"
    port = 6789

    client = SimpleUDPClient(ip, port) # Creating the OSC UDP Client

    client.send_message(":", message)
