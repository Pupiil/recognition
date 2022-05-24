# USAGE
# python recognition.py --cascade haarcascade.xml --encodings encodings.pickle

# import the necessary packages
import pupiilcommon
import traceback
import selectors
import socket

sel = selectors.DefaultSelector()

def create_request(value):
    return dict(
        type="binary/custom-client-binary-type",
        encoding="binary",
        content=bytes(value, encoding="utf-8"),
    )

def start_connection(host, port, request):
    addr = (host, port)
    print(f"Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = pupiilcommon.LibRecognition.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def main():

    config = {
        "client_ip": "127.1.1.1",
        "client_port": 6005,
        "value": "stream"
    }
    
    start_connection(config["client_ip"], config["client_port"], create_request(config["value"]))

    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                        f"{traceback.format_exc()}"
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()    



if __name__ == '__main__':
    main()
