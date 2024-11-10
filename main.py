
from config.EmojiConfig import EmojiConfig
from config.ImageAndEmojiConfig import ImageAndEmojiConfig
from config.ImageConfig import ImageConfig
from util import SystemColorUtil
from colorama import Fore
from util.CpuInfoUtil import CpuInfoUtil
from util.ImageToTxtArtConverterPlus import ImageToTxtArtConverterPlus
from util.JavaEnviromentInfoUtil import JavaEnviromentInfoUtil
from util.NetworkCardInfoUtil import NetworkCardInfoUtil
from util.PackageInfoUtil import PackageInfoUtil
from util.PythonEnviromentInfoUtil import PythonEnviromentInfoUtil
from util.DiskInfoUtil import DiskInfoUtil
from util.GpuInfoUtil import GpuInfoUtil
from util.ImageToAsciiConverter import ImageToTxtArtConverter
from util.MemoryInfoUtil import MemoryInfoUtil
from util.PlatformUtil import PlatformUtil
from util.ShellInfoUtil import ShellInfoUtil
from util.SystemInfoUtil import SystemInfoUtil
from util.TimeInfoUtil import TimeInfoUtil

# 获取系统信息
system_info = {
    "OS": PlatformUtil.get_platform() + " " + PlatformUtil.get_platform_bit(),
    "处理器": CpuInfoUtil.get_cpu_name(),
    "CPU核心数": CpuInfoUtil.get_cpu_count() + " 、" + "CPU线程数" + " : " + CpuInfoUtil.get_cpu_count_logical(),
    "CPU使用率": CpuInfoUtil.get_cpu_usage(),
    "所有GPU": GpuInfoUtil.get_gpu_info().get("GPU Name"),
    "上次启动": TimeInfoUtil.get_current_time(),
    "开机时长": TimeInfoUtil.calculate_uptime(),
    "内存信息": MemoryInfoUtil.get_memory_info(),
    # "分区信息": PlatformUtil.get_disk_info(), # warn：返回的字符较长，会导致ascii图像错位
    "硬盘信息": DiskInfoUtil.get_disk_info_sum(),
    # 只显示第一张网卡
    "网卡信息": NetworkCardInfoUtil.get_network_card_hardware_names()[0],
    "Python环境": PythonEnviromentInfoUtil.get_python_info(),
    "java环境": JavaEnviromentInfoUtil.get_java_version(),
    # "包": PackageInfoUtil.get_package_counts(), # warn：这条执行时间较长
    "Shell": ShellInfoUtil.get_shell_type(),
}


def get_ascii_art():
    """
    获取 ASCII 艺术图像。

    返回值：
    list -- 包含 ASCII 艺术图像的列表，每行一个元素。
    """

    image_and_emoji_config = ImageAndEmojiConfig()
    image_path = image_and_emoji_config.get_image_path()
    image_width = image_and_emoji_config.get_image_width()
    image_height = image_and_emoji_config.get_image_height()
    image_scale = image_and_emoji_config.get_image_scale()

    # 旧版
    # converter = ImageToTxtArtConverter()
    # colored_ascii_art = converter.convert_image_to_high_saturation_ascii(image_path, width=width, height=height).splitlines() # 获取彩色 ASCII 艺术, 并将其按行分割

    # 增强版
    converter = ImageToTxtArtConverterPlus(
        scale=image_scale, colored=True, width=image_width, height=image_height)
    colored_ascii_art = converter.get_image_ascii(
        image_path=image_path).splitlines()  # 获取彩色 ASCII 艺术, 并将其按行分割

    return colored_ascii_art


if __name__ == '__main__':
    # 获取emoji
    image_and_emoji_config = ImageAndEmojiConfig()
    emoji = image_and_emoji_config.get_emoji()

    # 获取talk
    talk = image_and_emoji_config.get_talk()

    # 系统信息转换为字符串格式
    system_info_lines = [
        f"{Fore.RED}{f'>>> {talk} >>>':<18}{Fore.RESET}"]

    # 拼接用户信息 和 当前时间
    system_info_lines.append(SystemInfoUtil.get_username(
    ) + "@" + SystemInfoUtil.get_computer_name() + " | " + TimeInfoUtil.get_current_time().__str__()) 

    # 拼接分割线
    system_info_lines.append("-"*25)

    for key, value in system_info.items():
        # system_info_lines.append(f"{key:<10}: {value}")
        system_info_lines.append(f"{emoji} {key}: {value}")

    # 拼接分割线
    system_info_lines.append("-"*25)

    # 拼接基本16色块(拼接两次是为了加高度)
    system_info_lines.append(SystemColorUtil.get_color_blocks())
    # system_info_lines.append(SystemColorUtil.get_color_blocks())

    # 获取 ASCII 艺术图像
    colored_ascii_art = get_ascii_art()

    # 获取最大行数
    max_lines = max(len(system_info_lines), len(colored_ascii_art))

    # 对齐并输出
    for i in range(max_lines):
        # 左侧 ASCII 艺术行
        left_text = colored_ascii_art[i] if i < len(
            colored_ascii_art) else " " * 60
        # 右侧系统信息行
        right_text = system_info_lines[i] if i < len(system_info_lines) else ""
        print(f"{left_text:<60}  {right_text}")
