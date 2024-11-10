import platform
import sys
import locale


class PythonEnviromentInfoUtil:
    """
    开发环境信息工具类。

    方法：
    >>> get_python_version() -- 获取 Python 版本。
    >>> get_system_locale() -- 获取系统语言环境。
    >>> get_python_info() -- 获取 Python 版本和语言环境。
    """
    

    def _get_python_version():
        """
        获取 Python 版本

        返回值：
        str -- Python 版本的字符串表示。

        例如：3.10.12
        """
        return platform.python_version()

    def _get_system_locale():
        """
        获取系统语言环境

        返回值：
        tuple -- 包含语言环境和编码的元组。

        例如：('en_US', 'UTF-8')
        """
        # 获取当前的语言环境（例如 'en_US.UTF-8'）
        return locale.getdefaultlocale()

    @staticmethod
    def get_python_info():
        """获取 Python 版本和语言环境"""
        python_version = PythonEnviromentInfoUtil._get_python_version()
        system_locale = PythonEnviromentInfoUtil._get_system_locale()
        # return f"Python 版本: {python_version}, 系统语言环境: {system_locale}"
        return f"{python_version} {system_locale}"


# 测试
# print(DevEnviromentInfoUtil.get_python_info())
