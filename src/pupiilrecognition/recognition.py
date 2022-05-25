# USAGE
# python recognition.py --cascade haarcascade.xml --encodings encodings.pickle

# import the necessary packages
import pupiilcommon
import traceback
import selectors
import socket

sel = selectors.DefaultSelector()


def create_request(action):
    return dict(
        type="text/json",
        encoding="utf-8",
        content=dict(
            action=action,
            value=pupiilcommon.MacAuxClass.MacAux().get_machine_info(),
        ),
    )


def start_connection(host, port, request, client):
    addr = (host, port)
    print(f"[RECOGNITION::RECOGNITION] Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((client[0], client[1]))
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = pupiilcommon.LibRecognition.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def main():

    config = {
        "client_ip": "127.46.75.34",
        "client_port": 6049,
        "recognition_ip": "127.51.64.12",
        "recognition_port": 5235,
        "action": "stream",
        "value": "",
    }

    start_connection(
        config["client_ip"],
        config["client_port"],
        create_request(config["action"]),
        (config["recognition_ip"], config["recognition_port"]),
    )

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


if __name__ == "__main__":
    main()
