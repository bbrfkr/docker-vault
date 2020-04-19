import socket
import time

import hvac

secrets_path = "/secrets/secrets.yaml"


def wait_for_port(port=8200, host="vault", timeout=60.0):
    """Wait until a port starts accepting TCP connections.
    Args:
        port (int): Port number.
        host (str):
          Host address on which the port should exist.
        timeout (float):
          In seconds.
          How long to wait before raising errors.
    Raises:
        TimeoutError:
          The port isn't accepting connection
          after time specified in `timeout`.
    """
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except OSError as ex:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError(
                    "Waited too long for the port {} on host {}"
                    "to start accepting connections.".format(port, host)
                ) from ex


def create_client(scheme="http", host="vault", port=8200):
    """Create Vault Client"""

    wait_for_port(host=host, port=port)
    return hvac.Client(url=f"{scheme}://{host}:{port}")
