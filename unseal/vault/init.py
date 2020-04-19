import yaml

from vault import utils


def init(shares=5, threshold=3):
    """Initialize Vault Server
     this function is idempotent"""

    client = utils.create_client()
    if not client.sys.is_initialized():
        result = client.sys.initialize(shares, threshold)
        with open(utils.secrets_path, "w") as file:
            secret_data = {
                "root_token": result["root_token"],
                "keys": result["keys"],
                "threshold": threshold,
            }
            file.write(yaml.dump(secret_data))
