# Vault Server by Docker Compose
By using this repository, you can start Hashicorp Vault server and make be ready to store secret immediately. Instead of you, `unseal` container will unseal your Vault server.

## Usage
The only following procedure!

```
sudo docker-compose up -d
```

After the above command, you will get the `secrets.yaml` in the `secrets` directory. Contents of this file;

* some shard keys
* root token
* unseal threshold

*** IMPORTANT *** : you MUST NOT contain `secrets.yaml` and the contents in the git repository!!
