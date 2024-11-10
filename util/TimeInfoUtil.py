import os
import time
import datetime
import psutil

class TimeInfoUtil:
    """ 
    时间信息工具类。
    
    方法：
    >>> get_current_time() -- 获取当前时间。
    >>> get_boot_time() -- 获取 Windows、Unix、Linux、macOS 系统的开机时间(会自主判断系统类型来获取时间)。
    """

    @staticmethod
    def get_current_time():
        """
        获取当前时间。

        返回值：
        str -- 当前时间的字符串表示。
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_boot_time():
        """ 
        获取 Windows、Unix、Linux、macOS 系统的开机时间(会自主判断系统类型来获取时间)。

        返回值：
        str -- 开机时间的字符串表示。
        """
        if os.name == 'posix':  # Unix/Linux/macOS
            try:
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                boot_time = time.time() - uptime_seconds
                return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(boot_time))
            except Exception as e:
                return f"获取开机时间失败: {e}"

        elif os.name == 'nt':  # Windows
            try:
                boot_time = psutil.boot_time()
                return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(boot_time))
            except Exception as e:
                return f"获取开机时间失败: {e}"

        else:
            return "此平台不支持获取开机时间"

    @staticmethod
    def calculate_uptime():
        """计算开机时长"""
        boot_time_str = TimeInfoUtil.get_boot_time()

        # 如果获取的开机时间是错误信息，直接返回
        if "失败" in boot_time_str or "不支持" in boot_time_str:
            return boot_time_str
        
        # 将开机时间字符串转换为时间戳
        boot_time = time.mktime(datetime.datetime.strptime(boot_time_str, '%Y-%m-%d %H:%M:%S').timetuple())
        
        # 计算当前时间与开机时间的时间差
        uptime_seconds = time.time() - boot_time
        # 格式化为天、小时、分钟和秒
        days = int(uptime_seconds // (24 * 3600))
        hours = int((uptime_seconds % (24 * 3600)) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        return f"{days}天 {hours}小时 {minutes}分钟 {seconds}秒"


# 测试
# print("当前时间:", TimeInfoUtil.get_current_time())
# print("开机时间:", TimeInfoUtil.get_boot_time())
# print("系统开机时长:", TimeInfoUtil.calculate_uptime())
