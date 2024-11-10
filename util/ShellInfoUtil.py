import os


class ShellInfoUtil:
    """
    获取shell的信息
    """
    @staticmethod

    def get_shell_type():
        """
        获取当前 shell 类型

        返回值：
        str -- 当前 shell 类型（例如 'bash', 'zsh', 'cmd', 'powershell' 等）
        """
        # 检查 Unix/Linux 系统上的 SHELL 环境变量
        shell_path = os.environ.get('SHELL')
        if shell_path:
            return shell_path.split('/')[-1]

        # 检查 Windows 系统的环境变量
        if os.name == 'nt':
            # 检查 PowerShell 的标识
            if 'PSModulePath' in os.environ:
                return 'powershell'
            # 检查 COMSPEC 变量 (通常是 'cmd.exe')
            comspec = os.environ.get('COMSPEC')
            if comspec:
                return comspec.split('\\')[-1].replace('.exe', '')

        return "无法识别 shell 类型"


# 测试
# print("当前 shell 类型:", ShellInfoUtil.get_shell_type())
