from enum import Enum
import json
import sys

class Packets(str, Enum):
	HANDSHAKE = "HANDSHAKE"
	REQ_SPACE = "REQ_SPACE"
	RESP_SPACE = "RESP_SPACE"
	REQ_TRANSFER = "REQ_TRANSFER"
	RESP_TRANSFER = "RESP_TRANSFER"

def fetchReqPacket(packetType):
	if (isinstance(packetType, Packets)):
		return json.dumps([packetType])
	else:
		print("[PACKETS] Packets type mismatch.")

def fetchSmallPacket(packetType, data):
	if (isinstance(packetType, Packets)):
		if (sys.getsizeof(data) + sys.getsizeof(packetType)) > 256:
			print("[PACKETS] The amount of data has exceeded the maximum of 256 bytes")
		else:
			return json.dumps([packetType, data])
	else:
		print("[PACKETS] Packets type mismatch.")