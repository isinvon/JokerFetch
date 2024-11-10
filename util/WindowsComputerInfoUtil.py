import subprocess

class WindowsComputerInfoUtil:
    """ 
    
    计算机信息工具类，用于获取计算机的各种信息。
    该类使用 systeminfo 命令来获取系统信息，并将其存储在一个字典中。
    该类还提供了一些方法来获取特定的系统信息。

    注意：这个工具类获取速度非常慢,不建议使用!!!

    """
    # 定义类变量来存储系统信息
    system_info_cache = {}

    @classmethod
    def load_system_info(cls):
        """使用 systeminfo 命令加载所有系统信息并存储到类变量字典中"""
        try:
            result = subprocess.run("systeminfo", stdout=subprocess.PIPE, text=True)
            output = result.stdout

            for line in output.splitlines():
                if ":" in line:
                    # 使用 key-value 形式存储到字典
                    key, value = line.split(":", 1)
                    cls.system_info_cache[key.strip()] = value.strip()
        except Exception as e:
            print(f"获取系统信息时出错: {e}")

    @classmethod
    def get_cached_info(cls, key_name):
        """从缓存的系统信息中获取指定的值"""
        return cls.system_info_cache.get(key_name, f"无法找到 {key_name} 信息")

    @classmethod
    def get_host_name(cls):
        return cls.get_cached_info("主机名")  # 英文系统为 "Host Name"

    @classmethod
    def get_os_name(cls):
        return cls.get_cached_info("OS 名称")  # 英文系统为 "OS Name"

    @classmethod
    def get_os_version(cls):
        return cls.get_cached_info("OS 版本")  # 英文系统为 "OS Version"

    @classmethod
    def get_os_manufacturer(cls):
        return cls.get_cached_info("OS 制造商")  # 英文系统为 "OS Manufacturer"

    @classmethod
    def get_registered_owner(cls):
        return cls.get_cached_info("注册的所有人")  # 英文系统为 "Registered Owner"

    @classmethod
    def get_product_id(cls):
        return cls.get_cached_info("产品 ID")  # 英文系统为 "Product ID"

    @classmethod
    def get_network_adapter(cls):
        adapter_info = []
        capture = False

        # 从缓存中查找与“网卡”相关的所有行
        for key, value in cls.system_info_cache.items():
            if "网卡" in key:  # 英文系统为 "Network Adapter"
                capture = True
            if capture:
                if not value:
                    break
                adapter_info.append(f"{key}: {value}")

        return "\n".join(adapter_info) if adapter_info else "无法获取网卡信息"


# # 加载系统信息一次
WindowsComputerInfoUtil.load_system_info()

# # 测试
# print("主机名:", ComputerInfoUtil.get_host_name())
# print("OS 名称:", ComputerInfoUtil.get_os_name())
# print("OS 版本:", ComputerInfoUtil.get_os_version())
# print("OS 制造商:", ComputerInfoUtil.get_os_manufacturer())
# print("注册的所有人:", ComputerInfoUtil.get_registered_owner())
# print("产品 ID:", ComputerInfoUtil.get_product_id())
# print("网卡信息:\n", ComputerInfoUtil.get_network_adapter())
