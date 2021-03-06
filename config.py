class Config:
    server_list = {
        "LocalDevice": "127.0.0.1",
        "vagrant-ubuntu": "192.168.56.2",
    }

    decision_algorithm = {
        "default": "select_random_server",
        "minimum_ping_delay": "select_min_ping_server",
    }

    DEFAULT_THROUGHPUT_PERIOD = 1

    # User expected throughput in local device, which means that
    # this is max number of requests per second processed on local device,
    # if more than this, offload requests to remote servers.
    EXPECTED_THROUGHPUT = 25


class FlaskTestConfig(Config):
    server_list = {
        "LocalDevice": "127.0.0.1",
        "vagrant-ubuntu1": "192.168.56.2",
        "vagrant-ubuntu2": "192.168.56.3",
    }

    port = 5000


class SmartContractConfig(Config):
    # This is a dict containing pairs of <function name: string, offloading or not: bool>
    # Engine will search in this dict to determine whether to offload or not.
    # Example:
    # offloadingFlag = {
    #                   "getRemoteInfo": True,
    #                   "listNodes": False,
    #                   }
    offloadingFlag = dict()

    server_list = {
        "ubuntu2004": "192.168.0.106",
        "manjaro": "192.168.0.102",
    }

    port = 18000


config = {
    "default": Config,
    "FlaskTestConfig": FlaskTestConfig,
    "SmartContractConfig": SmartContractConfig,
}
