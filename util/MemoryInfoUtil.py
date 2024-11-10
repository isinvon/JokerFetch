import psutil


class MemoryInfoUtil:
    """
    内存信息工具类。
    """

    @staticmethod
    def get_memory_info():
        """
        获取内存容量和占用率信息。

        返回值：
        dict -- 包含内存容量和占用率信息的字典。
        """
        memory_info = psutil.virtual_memory()
        
        # 换成Mb，保留一位小数
        memory_total = round((memory_info.total / (1024 * 1024)), 1).__str__() + "Mb"
        memory_available = round((memory_info.available / (1024 * 1024)), 1).__str__() + "Mb"
        memory_used = round((memory_info.used / (1024 * 1024)), 1).__str__() + "Mb"
        memory_free = round((memory_info.free / (1024 * 1024)), 1).__str__() + "Mb"
        memory_percent = round(memory_info.percent, 1).__str__() + "%"

        # 换算成 G，保留一位小数
        # memory_total = round(
        #     (memory_info.total / (1024 * 1024 * 1024)), 1).__str__() + "G"
        # memory_available = round(
        #     (memory_info.available / (1024 * 1024 * 1024)), 1).__str__() + "G"
        # memory_used = round(
        #     (memory_info.used / (1024 * 1024 * 1024)), 1).__str__() + "G"
        # memory_free = round(
        #     (memory_info.free / (1024 * 1024 * 1024)), 1).__str__() + "G"
        # memory_percent = round(
        #     memory_info.percent, 1).__str__() + "%"

        # 字典形式返回
        # return {
        #     "total": memory_total,
        #     "available": memory_available,
        #     "used": memory_used,
        #     "free": memory_free,
        #     "used_percent": memory_percent
        # }

        # 完全返回
        # return f"total: {memory_total} | available: {memory_available} | used: {memory_used} | free: {memory_free} | used_percent: {memory_percent}"
        # 返回total、used，used_percent
        # return f"total: {memory_total} | used: {memory_used} | used_percent: {memory_percent}"
        # 返回Mb占比
        return f"{memory_used}/{memory_total} | used_percent: {memory_percent}"
