import hashlib
import bisect

def	hash(key: str, salt: str = "") -> int:
	# 1. เขียนลอจิกแปลง SHA-256 เป็น 64-bit int ที่นี่
	sorce = key + salt
	data = sorce.encode("utf-8")
	hashed = hashlib.sha256(data)
	raw_bytes = hashed.digest()
	return hashed
	pass

class HashRing:
	def	__init__(self, v_nodes: int = 32, salt: str = ""):
		# 2. เตรียม Data Structures ที่นี่
		pass

	def	add_node(self, node_id: str) -> bool:
		# 3. ลอจิกเพิ่มตึก + ปัก Virtual Nodes ที่นี่
		pass

	def	remove_node(self, node_id: str) -> bool:
		# 4. ลอจิกถอนตึกออกจากวงแหวน ที่นี่
		pass

	def	get_node(self, guest_key: str) -> str | None:
		# 5. ลอจิกหาตึกให้แขก (bisect + wrap-around) ที่นี่
		pass

key = "helloworld"
print(hash(key))