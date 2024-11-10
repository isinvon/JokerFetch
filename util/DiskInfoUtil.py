import psutil


class DiskInfoUtil:
    """
    硬盘信息工具类。
    """

    @staticmethod
    def get_disk_info():
        """ 
        获取硬盘每个分区容量信息。
        """
        disk_info = {}
        for partition in psutil.disk_partitions():
            if 'cdrom' in partition.opts or partition.fstype == '':
                # 跳过没有文件系统类型的CD-ROM驱动器和分区
                continue
            disk_info[partition.device] = psutil.disk_usage(
                partition.mountpoint)

        # for循环拼接分区信息
        disk_info_str = ""
        disk_info_str_G = ""
        for partition, usage in disk_info.items():
            disk_total = usage.total
            # 换算成单位GB,保留一位小数
            disk_total_G = round(usage.total / (1024 * 1024 * 1024), 1)

            disk_used = usage.used
            # 换算成单位GB,保留一位小数
            disk_used_G = round(usage.used / (1024 * 1024 * 1024), 1)

            disk_free = usage.free
            # 换算成单位GB,保留一位小数
            disk_free_G = round(usage.free / (1024 * 1024 * 1024), 1)

            disk_used_percent = usage.percent

            # 拼接分区信息(单位:Byte)
            disk_info_str += f"{partition}: total: {disk_total}Byte | used: {disk_used}Byte | free: {disk_free}Byte | used_percent: {disk_used_percent}% | "
            # 拼接分区信息(单位:GB)
            disk_info_str_G += f"{partition}: total:{disk_total_G}G | used: {disk_used_G}G | used_percent: {disk_used_percent}% | "

        return disk_info_str_G
    
    @staticmethod
    def get_disk_info_sum():
        """
        获取所有硬盘、所有分区容量信息的总和。
        """
        disk_info = {}
        for partition in psutil.disk_partitions():
            if 'cdrom' in partition.opts or partition.fstype == '':
                # 跳过没有文件系统类型的CD-ROM驱动器和分区
                continue
            disk_info[partition.device] = psutil.disk_usage(
                partition.mountpoint)

        all_disk_total = 0
        all_disk_used = 0
        all_disk_free = 0

        all_disk_total_G = 0
        all_disk_used_G = 0
        all_disk_free_G = 0

        for partition, usage in disk_info.items():
            # partition就是分区名,usage就是分区信息
            all_disk_total += usage.total
            all_disk_used += usage.used
            all_disk_free += usage.free
        # 计算总百分比
        all_disk_used_percent = round(all_disk_used / all_disk_total * 100, 1)

        # 换算成单位GB,保留一位小数
        all_disk_total_G = round(all_disk_total / (1024 * 1024 * 1024), 1)
        all_disk_used_G = round(all_disk_used / (1024 * 1024 * 1024), 1)
        all_disk_free_G = round(all_disk_free / (1024 * 1024 * 1024), 1)

        # 换算成TB,保留一位小数
        all_disk_total_T = round(
            all_disk_total / (1024 * 1024 * 1024 * 1024), 1)
        all_disk_used_T = round(all_disk_used / (1024 * 1024 * 1024 * 1024), 1)
        all_disk_free_T = round(all_disk_free / (1024 * 1024 * 1024 * 1024), 1)

        # 字符串形式返回(单位:GB)(完全返回)
        # return f"total: {all_disk_total_G}G ({all_disk_total_T}T) | used: {all_disk_used_G}G ({all_disk_used_T}T) | free: {all_disk_free_G}G ({all_disk_free_T}T) | used_percent: {all_disk_used_percent}%"
        # 只返回total、used，used_percent
        return f"total: {all_disk_total_G}G | used: {all_disk_used_G}G | used_percent: {all_disk_used_percent}%"
