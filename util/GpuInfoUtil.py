import platform
import subprocess


class GpuInfoUtil:
    """
    GPU 信息工具类
    """

    @staticmethod
    def get_gpu_info():
        """
        获取显卡信息（兼容多种显卡和操作系统）

        返回类型:
        -- dict: 包含显卡名称和信息的字典。

        返回:
        - 如果成功获取显卡信息，则返回显卡名称和信息字典。
        - 如果获取失败，则返回错误信息。

        注意:
        - 此方法仅在 Windows、Linux 和 macOS 上进行了测试。
        - 对于其他操作系统，可能需要根据实际情况进行调整。 

        示例:
        >>> gpu_info = GpuInfoUtil.get_gpu_info()
        >>> if isinstance(gpu_info, dict):

        """
        if platform.system() == "Windows":
            return GpuInfoUtil._get_gpu_info_windows()
        elif platform.system() == "Linux":
            return GpuInfoUtil._get_gpu_info_linux()
        elif platform.system() == "Darwin":  # macOS
            return GpuInfoUtil._get_gpu_info_macos()
        else:
            return "不支持的操作系统"

    @staticmethod
    def _get_gpu_info_windows():
        """在 Windows 上使用 wmic 获取显卡信息"""
        try:
            cmd = "wmic path win32_VideoController get name"
            result = subprocess.run(
                cmd, capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                # 解析输出，去除空行和标题行
                gpu_info = [line.strip()
                            for line in result.stdout.splitlines() if line.strip()]
                return {"GPU Name": gpu_info[1:]}  # 忽略标题行
            else:
                return f"获取显卡信息失败，错误: {result.stderr}"
        except Exception as e:
            return f"获取显卡信息失败: {e}"

    @staticmethod
    def _get_gpu_info_linux():
        """在 Linux 上使用 lspci 获取显卡信息"""
        try:
            cmd = "lspci | grep -i 'vga\\|3d\\|display'"
            result = subprocess.run(
                cmd, capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                # 提取显卡相关信息
                return {"GPU Info": result.stdout.strip().splitlines()}
            else:
                return f"获取显卡信息失败，错误: {result.stderr}"
        except Exception as e:
            return f"获取显卡信息失败: {e}"

    @staticmethod
    def _get_gpu_info_macos():
        """在 macOS 上使用 system_profiler 获取显卡信息"""
        try:
            cmd = "system_profiler SPDisplaysDataType"
            result = subprocess.run(
                cmd, capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                # 解析显卡信息
                gpu_info = []
                capture = False
                for line in result.stdout.splitlines():
                    line = line.strip()
                    if line.startswith("Chipset Model:"):
                        gpu_info.append(line)
                    elif line.startswith("VRAM (Total):") or line.startswith("Vendor:"):
                        gpu_info.append(line)
                return {"GPU Info": gpu_info}
            else:
                return f"获取显卡信息失败，错误: {result.stderr}"
        except Exception as e:
            return f"获取显卡信息失败: {e}"


# 测试
# gpu_info = GpuInfoUtil.get_gpu_info()
# print("显卡信息:", gpu_info)  # 获取显卡信息(返回字典)
# print("显卡信息:", gpu_info.get("GPU Name"))  # 获取显卡信息(返回列表)
# print("显卡信息:", gpu_info.get("GPU Name")[0])  # 获取第一个显卡信息(返回字符串)
