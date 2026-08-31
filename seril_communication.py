import serial

def connect_device():
    port = input("Enter COM port (example COM3): ")
    baudrate = int(input("Enter baud rate (example 115200): "))

    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"\nConnected to {port} at {baudrate} baud.")
        return ser

    except serial.SerialException as e:
        print(f"\nConnection failed: {e}")
        return None


def main():
    print("================================")
    print("   # EMBEDDED SERIAL TOOL #     ")
    print("================================")

    ser = connect_device()

    if ser is None:
        return

    while True:
        print("\n1. Read Data")
        print("2. Send Command")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            data = ser.readline().decode("utf-8", errors="ignore").strip()

            if data:
                print("Device:", data)
            else:
                print("No data received.")

        elif choice == "2":
            command = input("Enter command: ")
            ser.write((command + "\r\n").encode())

            print("Command sent.")

        elif choice == "3":
            ser.close()
            print("Disconnected.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()