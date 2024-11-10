import subprocess
import platform

class PackageInfoUtil:
    """ 
    作用: 该工具类提供了获取包数量的方法，根据不同的操作系统使用不同的工具来获取包数量。
    
    注意: 这个工具检索时间较长，可能需要等待一段时间。  

    方法：
    >>> get_package_counts() -- 获取包数量。
    >>> _get_windows_package_count() -- 获取 Windows 系统的包数量。
    >>> _get_linux_package_count() -- 获取 Linux 系统的包数量。
    >>> _get_macos_package_count() -- 获取 macOS 系统的包数量。
    
    注意：
    1. 该工具类仅适用于 Windows、Linux 和 macOS 系统。
    2. 对于 Windows 系统，使用 winget 来获取包数量。
    3. 对于 Linux 系统，使用 dpkg 和 snap 来获取包数量。
    4. 对于 macOS 系统，使用 brew 和 pkgutil 来获取包数量。

    示例：
    >>> PackageInfoUtil.get_package_counts()
    'Packages: 100 (winget), 50 (dpkg), 30 (snap), 20 (brew), 10 (pkgutil)'
    
    """
    
    @staticmethod
    def get_package_counts():
        system = platform.system()

        if system == "Windows":
            return PackageInfoUtil._get_windows_package_count()
        elif system == "Linux":
            return PackageInfoUtil._get_linux_package_count()
        elif system == "Darwin":
            return PackageInfoUtil._get_macos_package_count()
        else:
            return "Unsupported platform"

    @staticmethod
    def _get_windows_package_count():
        """获取 Windows 系统的包数量（通过 winget）"""
        try:
            result = subprocess.run(
                ['winget', 'list'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            if result.returncode == 0:
                # 过滤掉标题行和动态生成的条目，确保输出稳定
                lines = result.stdout.strip().splitlines()
                # 忽略标题行
                filtered_lines = [line for line in lines[1:] if "动态进程" not in line and "系统组件" not in line]  # 示例过滤条件
                return f"Packages: {len(filtered_lines)} (winget)"
            return "Winget not available"
        except FileNotFoundError:
            return "Winget not installed"

    @staticmethod
    def _get_linux_package_count():
        dpkg_count = snap_count = "N/A"

        try:
            result = subprocess.run(['dpkg-query', '-f', '${binary:Package}\n', '-W'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                dpkg_count = len(result.stdout.strip().splitlines())
        except FileNotFoundError:
            dpkg_count = "dpkg not available"

        try:
            result = subprocess.run(['snap', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                snap_count = len(result.stdout.strip().splitlines()) - 1  # 减去表头行
        except FileNotFoundError:
            snap_count = "snap not available"

        return f"Packages: {dpkg_count} (dpkg), {snap_count} (snap)"

    @staticmethod
    def _get_macos_package_count():
        brew_count = pkgutil_count = "N/A"

        try:
            result = subprocess.run(['brew', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                brew_count = len(result.stdout.strip().splitlines())
        except FileNotFoundError:
            brew_count = "brew not available"

        try:
            result = subprocess.run(['pkgutil', '--pkgs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                pkgutil_count = len(result.stdout.strip().splitlines())
        except FileNotFoundError:
            pkgutil_count = "pkgutil not available"

        return f"Packages: {brew_count} (brew), {pkgutil_count} (pkgutil)"

# 测试
# if __name__ == "__main__":
    # print(PackageInfoUtil.get_package_counts())
