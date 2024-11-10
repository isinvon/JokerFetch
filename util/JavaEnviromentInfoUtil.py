import platform
import subprocess


class JavaEnviromentInfoUtil:
    """ 
    Java 环境信息工具类。
    
    方法：
    - get_java_version() -- 获取 Java 版本。
    - get_os_info() -- 获取操作系统信息。
    - get_cpu_info() -- 获取 CPU 信息。
    - get_jvm_memory_info() -- 获取 JVM 内存信息。
    - get_java_env_info() -- 获取 Java 环境的所有信息。
    
    注意：
    - 此工具类依赖于 subprocess 模块来执行命令行命令，因此在使用时需要确保系统中已安装 Java 环境。
    
    示例：
    >>>java_info = JavaEnviromentInfoUtil.get_java_env_info()
    >>>print(java_info)
    """
    @staticmethod
    def get_java_version():
        """
        获取 Java 版本
        """
        try:
            result = subprocess.run(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                # Java 版本信息通常在 stderr 中输出
                version_info = result.stderr.strip().splitlines()[0]
                return version_info.split('"')[1]  # 提取版本号
            return "Java not found"
        except FileNotFoundError:
            return "Java not installed"

    @staticmethod
    def get_os_info():
        """
        获取操作系统信息
        """
        return platform.system() + " " + platform.release() + " " + platform.machine()

    @staticmethod
    def get_cpu_info():
        """
        获取 CPU 信息
        """
        try:
            cpu_info = subprocess.check_output("wmic cpu get caption", shell=True, text=True).strip().splitlines()
            return cpu_info[1] if len(cpu_info) > 1 else "CPU info not available"
        except Exception as e:
            return f"Error fetching CPU info: {e}"

    @staticmethod
    def get_jvm_memory_info():
        """
        获取 JVM 内存信息
        """
        try:
            # 获取 Java 的堆内存大小
            result = subprocess.run(['java', '-XX:+PrintFlagsFinal', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                flags_output = result.stdout
                heap_size = next((line for line in flags_output.splitlines() if 'MaxHeapSize' in line), None)
                non_heap_size = next((line for line in flags_output.splitlines() if 'MaxPermSize' in line), None)
                return f"Heap Size: {heap_size}, Non-Heap Size: {non_heap_size}"
            return "Unable to retrieve JVM memory info"
        except FileNotFoundError:
            return "Java not installed"
        except Exception as e:
            return f"Error fetching JVM memory info: {e}"

    @staticmethod
    def get_java_env_info():
        """
        获取 Java 环境的所有信息
        """
        java_version = JavaEnviromentInfoUtil.get_java_version()
        os_info = JavaEnviromentInfoUtil.get_os_info()
        cpu_info = JavaEnviromentInfoUtil.get_cpu_info()
        jvm_memory_info = JavaEnviromentInfoUtil.get_jvm_memory_info()

        return f"Java Version: {java_version}\n" \
               f"OS Info: {os_info}\n" \
               f"CPU Info: {cpu_info}\n" \
               f"JVM Memory Info: {jvm_memory_info}"

# if __name__ == "__main__":
    # print(JavaEnviromentInfoUtil.get_java_env_info())
