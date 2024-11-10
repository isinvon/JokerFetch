import psutil
import socket
import platform
import subprocess


class NetworkCardInfoUtil:
    """
    获取系统的网卡信息
    """

    @staticmethod
    def get_network_cards():
        """获取所有网卡的信息"""
        net_info = psutil.net_if_addrs()  # 获取网卡信息
        cards_info = {}
        for card, addresses in net_info.items():
            card_info = {}
            for address in addresses:
                # 获取IPv4地址、IPv6地址和MAC地址等信息
                if address.family == socket.AF_INET:  # IPv4
                    card_info['IPv4'] = address.address
                elif address.family == socket.AF_INET6:  # IPv6
                    card_info['IPv6'] = address.address
                elif address.family == psutil.AF_LINK:  # MAC地址
                    card_info['MAC'] = address.address

            cards_info[card] = card_info
        return cards_info

    @staticmethod
    def get_ip_addresses():
        """获取所有网卡的 IP 地址"""
        net_info = psutil.net_if_addrs()  # 获取网卡信息
        ip_addresses = {}
        for card, addresses in net_info.items():
            for address in addresses:
                if address.family == socket.AF_INET:  # IPv4
                    ip_addresses[card] = address.address
        return ip_addresses

    @staticmethod
    def get_mac_addresses():
        """获取所有网卡的 MAC 地址"""
        net_info = psutil.net_if_addrs()  # 获取网卡信息
        mac_addresses = {}
        for card, addresses in net_info.items():
            for address in addresses:
                if address.family == psutil.AF_LINK:  # MAC地址
                    mac_addresses[card] = address.address
        return mac_addresses

    @staticmethod
    def get_network_card_names():
        """获取所有网卡的名称"""
        net_info = psutil.net_if_addrs()  # 获取网卡信息
        return list(net_info.keys())

    @staticmethod
    def get_default_gateway():
        """获取默认网关"""
        # 通过 psutil 获取路由表来获取默认网关
        default_gateway = None
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED':
                # 获取默认网关的连接信息，假设常见网关为外网连接
                if conn.laddr and conn.raddr:
                    default_gateway = conn.raddr
                    break
        return default_gateway

    @staticmethod
    def get_netmask_addresses():
        """获取所有网卡的子网掩码"""
        net_info = psutil.net_if_addrs()  # 获取网卡信息
        netmasks = {}
        for card, addresses in net_info.items():
            for address in addresses:
                if address.family == socket.AF_INET:  # IPv4
                    netmasks[card] = address.netmask
        return netmasks


    
    @staticmethod
    def get_network_card_hardware_names():
        """获取网卡的硬件名称 (例如：Intel(R) Wi-Fi 6 AX201 160MHz)"""
        system_platform = platform.system().lower()
        card_names = []

        if system_platform == "windows":
            # 在 Windows 上使用 wmic 获取网卡信息
            try:
                # 使用wmic命令获取网络适配器产品名称
                result = subprocess.check_output('wmic nic where "NetEnabled=true" get ProductName', shell=True)
                result = result.decode('utf-8').strip().split('\n')[1:]  # 跳过第一行标题
                for line in result:
                    name = line.strip()
                    if name:
                        card_names.append(name)
            except Exception as e:
                print(f"Error getting network card names on Windows: {e}")

        elif system_platform == "linux":
            # 在 Linux 上使用 ethtool 获取网卡硬件信息
            try:
                # 使用 ethtool 获取网卡硬件信息
                result = subprocess.check_output("ethtool -i eth0", shell=True)
                result = result.decode('utf-8').strip().split('\n')
                for line in result:
                    if 'driver' in line:
                        driver_name = line.split(":")[1].strip()
                        card_names.append(driver_name)
            except Exception as e:
                print(f"Error getting network card names on Linux: {e}")
        else:
            print("Unsupported platform")

        # 去除重复的名称
        return list(set(card_names))


# 示例使用：直接通过类调用方法
# if __name__ == "__main__":
#     # 获取所有网卡信息
#     network_cards = NetworkCardInfoUtil.get_network_cards()
#     print("所有网卡信息：")
#     for card, info in network_cards.items():
#         print(f"{card}: {info}")

#     # 获取所有网卡的 IP 地址
#     ip_addresses = NetworkCardInfoUtil.get_ip_addresses()
#     print("\n网卡的 IP 地址：")
#     for card, ip in ip_addresses.items():
#         print(f"{card}: {ip}")

#     # 获取所有网卡的 MAC 地址
#     mac_addresses = NetworkCardInfoUtil.get_mac_addresses()
#     print("\n网卡的 MAC 地址：")
#     for card, mac in mac_addresses.items():
#         print(f"{card}: {mac}")

#     # 获取默认网关
#     default_gateway = NetworkCardInfoUtil.get_default_gateway()
#     print(f"\n默认网关: {default_gateway}")

#     # 获取子网掩码
#     netmasks = NetworkCardInfoUtil.get_netmask_addresses()
#     print("\n网卡的子网掩码：")
#     for card, netmask in netmasks.items():
#         print(f"{card}: {netmask}")

#     # 获取网卡的硬件名称
#     hardware_names = NetworkCardInfoUtil.get_network_card_hardware_names()
#     print("\n网卡硬件名称：")
#     for card, name in hardware_names.items():
#         print(f"{card}: {name}")
