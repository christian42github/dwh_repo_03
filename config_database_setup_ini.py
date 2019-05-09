import configparser


class DatabaseSetupIni(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config_database_setup.ini')

    def get_read_template_path(self):
        return self.config['DEFAULT']['read_template_path']

    def get_write_bteq_path(self):
        return self.config['DEFAULT']['write_bteq_path']

    def get_td_sys_name(self, _run_env: str):
        _sys = self.config['RUN_ENV_TO_SYS'][_run_env]
        return self.config[_sys]['td_sys_name']


if __name__ == '__main__':
    dbs = DatabaseSetupIni()

    print(dbs.get_read_template_path())
    print(dbs.get_write_bteq_path())

    print(dbs.get_td_sys_name('DEV'))
    print(dbs.get_td_sys_name('TEST1'))
    print(dbs.get_td_sys_name('TEST2'))
    print(dbs.get_td_sys_name('PROD'))
