def defang_ip_addr(self, address: str) -> str:
    return address.replace('.', '[.]')