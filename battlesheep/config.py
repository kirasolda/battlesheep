import socket

from battlesheep.logger import Logger

logger = Logger(__name__)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

logger.info(f"Hostname: {hostname}, IP Address: {ip_address}")
