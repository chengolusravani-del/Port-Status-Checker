import socket

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            result = s.connect_ex((host, port))

            if result == 0:
                print(f"Port {port} is OPEN on {host}.")
            else:
                print(f"Port {port} is CLOSED or FILTERED on {host}.")

    except socket.gaierror:
        print("Invalid hostname.")
    except OSError as error:
        print(f"Network error: {error}")


if __name__ == "__main__":
    host = input("Enter target hostname or IP: ").strip()

    try:
        port = int(input("Enter port number (1-65535): "))

        if not 1 <= port <= 65535:
            print("Please enter a port between 1 and 65535.")
        else:
            check_port(host, port)

    except ValueError:
        print("Please enter a valid port number.")