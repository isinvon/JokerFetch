import platform


class PlatformUtil:
    """
    平台工具类。
    """

    def get_platform():
        """
        Windows: Windows
        
        Linux: Linux
        
        Mac: Darwin
        """
        # return system type
        return platform.system().__str__()

    def get_platform_bit():
        """ 
        返回操作系统的位数：
        
        32bit: ('32bit', 'WindowsPE')
        
        64bit: ('64bit', 'WindowsPE')
        """
        return platform.architecture().__str__()


# platform =  PlatformUtil.get_platform_bit()
# print(platform)