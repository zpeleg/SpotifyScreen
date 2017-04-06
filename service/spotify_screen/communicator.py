import serial
from serial.tools.list_ports import comports
from typing import Union, List
from spotify_screen.keyboard_proxy import LinuxKeyboardProxy, KeyboardProxy
from spotify_screen.screen_controller import ScreenViewModel
from time import sleep


class SerialCommand:
    def __init__(self, name: str, parameters: List[str]):
        self.name = name
        self.parameters = parameters

    def __repr__(self):
        return "{}: {}".format(self.name, self.parameters)


class SerialCommunicator:
    def __init__(self, keyboard_proxy: Union[KeyboardProxy, LinuxKeyboardProxy]):
        self._keyboard_proxy = keyboard_proxy
        self._screen_to_send = None  # type: ScreenViewModel
        self._connection = None  # type: serial.Serial

    def connect(self):
        print("connecting")
        all_ports = comports()
        connections = []
        for port in all_ports:
            connection = serial.Serial(port.device, 115200, timeout=2)
            # Wait for device to wake up
            sleep(3)
            # Send Ahla message
            print(" * Sending Ahla to {}".format(port.device))
            connection.write("004Ahla")
            connections.append(connection)
        sleep(1)

        for connection in connections:
            print(" * reading from port")
            if connection.in_waiting > 0:
                # Receive response
                message_size = connection.read(3)
                message = connection.read(int(message_size))
                if message != "Ahla":
                    raise Exception("Weird error occurred! message: {}".format(message))
                else:
                    print(" * Got Ahla")
                    # Close other connections
                    self._close_all_connections_but_chosen(connection, connections)
                    self._connection = connection

    def _close_all_connections_but_chosen(self, chosen, connections):
        for c in connections:
            if c is not chosen:
                c.close()

    def send_new_screen(self, vm):
        print(" * Got new screen for song {}".format(vm.title))
        self._screen_to_send = vm

    def listen(self):
        print(" * listen cycle")
        if self._connection.in_waiting > 0:
            command = self._read_command()
            print(" * Got {} message with parameters {}".format(command.name, command.parameters))
            self._execute_command(command)
        if self._screen_to_send is not None:
            print(" * Sending screen")
            self._send_screen()

    def _read_command(self):
        while self._connection.in_waiting < 3:
            sleep(0.1)
        num_chars = int(self._connection.read(3))
        message = self._connection.read(num_chars)
        splitted = message.split(b";;")
        return SerialCommand(splitted[0], splitted[1:])

    def _execute_command(self, command):
        if command.name.lower() == "key":
            if command.parameters[0] == "play":
                self._keyboard_proxy.play()
            elif command.parameters[0] == "next":
                self._keyboard_proxy.next()

    def _send_screen(self):
        message = self._screen_to_send.to_serial_format()
        message = ";;SCREEN;;" + message
        length = len(message.encode("utf8"))
        message = str(length).zfill(3) + message
        print(" * Sent message \"{}\"".format(message))
        self._connection.write(message.encode("utf8"))
        self._screen_to_send = None
