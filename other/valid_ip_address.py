def valid_ip_address(self, query_ip: str) -> str:
    length = 0
    for _ in query_ip:
        if length > 39:
            return "Neither"
        length += 1

    ipv4 = query_ip.split(".")
    ipv6 = query_ip.split(":")

    if len(ipv4) < 4 and len(ipv6) < 8:
        return "Neither"
    elif len(ipv4) == 4:
        for ip in ipv4:
            if (len(ip) > 1 and ip.startswith("0")) or not ip.isdigit():
                return "Neither"
            intIp = int(ip)
            if intIp < 0 or intIp > 255:
                return "Neither"

        return "IPv4"
    elif len(ipv6) == 8:
        for ip in ipv6:
            if len(ip) < 1 or len(ip) > 4:
                return "Neither"
            for char in ip:
                if not char.isdigit() and (char.lower() < 'a' or char.lower() > 'f'):
                    return "Neither"

        return "IPv6"

    return "Neither"
