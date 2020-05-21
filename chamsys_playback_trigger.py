# Triggers a go on the specified playback


import sys, socket


destinationIP = "192.168.1.1"
destPort = 6553

playback = 7
message = str(playback) + "G"


# Main Function
if __name__ == "__main__":

    try:
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Failed to create UDP Socket")
        sys.exit()

    # allow broadcasts
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        udpSocket.sendto(bytes(message, "utf-8"), (destinationIP, destPort))
        print("GO!")
    except socket.error:
        print("Failed send UDP")

    sys.exit()
