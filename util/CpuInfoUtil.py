# 需要安装 py-cpuinfo 库
from cpuinfo import get_cpu_info
import psutil


class CpuInfoUtil:
    @staticmethod
    def get_all_cpu_info():
        """ 
        获取cpu所有信息
        <br/>
        :return: cpu信息
        <br/>
        :rtype: dict
        """
        info = get_cpu_info()
        return info

    @staticmethod
    def get_cpu_name():
        """
        获取cpu名称
        
        例如：AMD Ryzen 7 5800X 8-Core Processor
    
        """
        info = get_cpu_info()
        return info['brand_raw']

    @staticmethod
    def get_cpu_arch():
        """
        获取cpu架构

        例如：X86_64
        """
        info = get_cpu_info()
        return info['arch']

    @staticmethod
    def get_cpu_bits():
        """
        获取cpu位数

        例如：64
        """
        info = get_cpu_info()
        return info['bits']

    @staticmethod
    def get_cpu_family():
        """
        获取cpu系列

        例如：6
        """
        info = get_cpu_info()
        return info['family']

    @staticmethod
    def get_cpu_model():
        """
        获取cpu型号

        例如：158
        """
        info = get_cpu_info()
        return info['model']

    @staticmethod
    def get_cpu_stepping():
        """
        获取cpu步进

        例如：9
        """
        info = get_cpu_info()
        return info['stepping']

    # @staticmethod
    # def get_cpu_count():
    #     """
    #     获取cpu核心数
    #     """
    #     info = get_cpu_info()
    #     return info['count']
    
    @staticmethod
    def get_cpu_count():
        """
        返回操作系统的cpu核心数量：

        例如：8
        """
        return psutil.cpu_count(logical=False).__str__()

    @staticmethod
    def get_cpu_count_logical():
        """
        返回操作系统的cpu线程数量：
        
        例如：16
        """
        return psutil.cpu_count(logical=True).__str__()


    # @staticmethod
    # def get_cpu_thread_count():
    #     """
    #     获取cpu线程数
    #     """
    #     info = get_cpu_info()
    #     return info['hz_actual_friendly'].__str__()


        
    @staticmethod
    def get_cpu_usage():
        """
        返回操作系统的cpu使用率：

        例如：10.0%
        """
        return psutil.cpu_percent().__str__() + "%"

    @staticmethod
    def get_cpu_flags():
        """
        获取cpu标志

        例如：['fpu', 'vme', 'de', 'pse', 'tsc','msr', 'pae','mce', 'cx8', 'apic','sep','mtrr', 'pge','mca', 'cmov', 'pat', 'pse36', 'clflush','mmx', 'fxsr','sse','sse2',
        """
        info = get_cpu_info()
        return info['flags']
    
    @staticmethod
    def get_cpu_arch_string_raw():
        """ 
        获取cpu架构字符串

        例如：AMD64 Family 15 Model 158 Stepping 9, AuthenticAMD
        """
        info = get_cpu_info()
        return info['arch_string_raw']
