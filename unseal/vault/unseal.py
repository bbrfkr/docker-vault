import yaml

from vault import utils


def unseal(secret_path=utils.secrets_path):
    client = utils.create_client()

    if client.sys.is_sealed():
        with open(secret_path, "r") as file:
            secrets = yaml.safe_load(file)
            threshold = secrets["threshold"]
            unseal_keys = secrets["keys"]
            for index in range(int(threshold)):
                client.sys.submit_unseal_key(unseal_keys[index])
