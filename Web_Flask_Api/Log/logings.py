import logging
import os

if os.path.exists('./Log'):
    pass
else:
    os.mkdir('./Log')
path = os.path.abspath('./Log')
file = 'system.log'
new_path = os.path.join(path, file)


format_base = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'
file_format = '[%(asctime)s][%(patname)s][line:%(lineno)d][%(levelname)s]-[%(message)s]'
date_format = "%Y-%m-%d %H:%M:%S"
config = {
    'debug': '\003[1;29m',
    'info': '\033[1;36m',
    'warning': '\033[1;33m',
    'error': '\033[1;31m',
    'critical': '\033[1;31m'
}


class Mylog(logging.Logger):
    def __init__(self):
        super().__init__(__name__)
        self._add_all_steam_handler()

    def callHandlers(self, record):
        # 重写方法，使屏幕输出模式不向上兼容，文件输出保留原样
        c = self
        while c:
            for hdir in c.handlers:
                if hdir.__class__.__name__ == 'StreamHandler' and record.levelno == hdir.level:
                    hdir.handle(record)
                if hdir.__class__.__name__ == 'FileHandler' and record.levelno == hdir.level:
                    hdir.handle(record)
            if not c.propagate:
                c = None
            else:
                c = c.parent

    def _add_all_steam_handler(self):
        # 添加所有steam——handler，每一个方法对应一个handler
        for method, color in config.items():
            fmt = '{} {} {}'.format(color, format_base, '\033[0m')
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter(fmt, datefmt=date_format))
            handler.setLevel(method.upper())
            self.addHandler(handler)

    def set_file_log(self, filename=new_path, _level=logging.WARNING):
        # 输出到文件
        file_handler = logging.FileHandler(
            filename=filename, mode='a', encoding='utf-8')
        file_handler.setLevel(_level)
        file_handler.setFormatter(logging.Formatter(
            file_format, datefmt=date_format))
        self.addHandler(file_handler)





