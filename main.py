#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""a_short_module_description"""
# ---------------------------------------------------------------------------

import time
from log_server import LogServer
import logging

HOST = "127.0.0.1"
PORT = 9000

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)


# Function to run the server
def run_server():
    log_server = LogServer(host=HOST, port=PORT, log_file="/var/log/log_server_0.log")
    log_server.start()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    run_server()
