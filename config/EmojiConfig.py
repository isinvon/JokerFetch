from config.BaseConfig import BaseConfig


class EmojiConfig(BaseConfig):
    """
    图像配置类，继承自BaseConfig
    """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_jinx_emoji(self):
        """获取jinx的emoji"""
        return self.config.get('jinxFlag', 'emoji', fallback=None)

    def get_kun_emoji(self):
        """获取kun的emoji"""
        return self.config.get('kunFlag', 'emoji', fallback=None)

    def get_joker_emoji(self):
        """获取joker的emoji"""
        return self.config.get('jokerFlag', 'emoji', fallback=None)

    def get_nailong_emoji(self):
        """获取nailong的emoji"""
        return self.config.get('nailongFlag', 'emoji', fallback=None)
