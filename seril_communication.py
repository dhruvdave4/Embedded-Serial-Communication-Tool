import serial
from datetime import datetime


def connect_device():
    port = input("Enter COM port (example COM3): ")
    baudrate = int(input("Enter baud rate (example 115200): "))

    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1
        )

        print(f"\nConnected to {port} at {baudrate} baud.")
        return ser

    except serial.SerialException as e:
        print(f"\nConnection failed: {e}")
        return None

    except ValueError:
        print("\nInvalid baud rate.")
        return None


def read_data(ser):
    data = ser.readline().decode(
        "utf-8",
        errors="ignore"
    ).strip()

    if data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Device: {data}")
    else:
        print("No data received.")


def send_command(ser):
    command = input("Enter command: ")

    if command:
        ser.write((command + "\r\n").encode())
        print("Command sent.")
    else:
        print("Command cannot be empty.")


def main():

    print("================================")
    print("    EMBEDDED SERIAL DEBUGGER")
    print("================================")

    ser = connect_device()

    if ser is None:
        return

    while True:

        print("\n----------- MENU -----------")
        print("1. Read Data")
        print("2. Send Command")
        print("3. Exit")
        print("----------------------------")

        choice = input("Select option: ")

        if choice == "1":
            read_data(ser)

        elif choice == "2":
            send_command(ser)

        elif choice == "3":
            ser.close()
            print("Disconnected.")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main() 