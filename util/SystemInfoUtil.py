import os
import socket

class SystemInfoUtil:
    """
    系统信息工具类，获取用户名称和计算机名称
    """

    @staticmethod
    def get_username():
        """
        获取当前用户名称

        返回:
        str -- 当前登录的用户名
        """
        return os.getlogin()

    @staticmethod
    def get_computer_name():
        """
        获取计算机名称

        返回:
        str -- 当前计算机的名称
        """
        return socket.gethostname()

# 测试
# print("用户名称:", SystemInfoUtil.get_username())
# print("计算机名称:", SystemInfoUtil.get_computer_name())
