import sys
from string import Template
from database_setup_ini import DatabaseSetupIni


def main(db_env: str):
    global g_read_template_path, g_write_bteq_path, g_td_sys_name
    tmp_fn = g_read_template_path + '/' + 'edw_create_env_user.template'
    out_fn = g_write_bteq_path + '/' + 'edw_create_env_user.' + db_env.lower() + '.btq'

    # build dictionary for template substitution
    dct2 = {}
    dct2['env'] = db_env.upper()
    dct2['logon_file'] = 'logon_file_edw_admin.btq'

    with open(tmp_fn, 'r') as f, open(out_fn, "w") as ofn:
        for ln in f:
            lnTmpl = Template(ln)
            lnSubst = lnTmpl.safe_substitute(dct2)  # safe_substitute: skips other ${...} without error
            print(lnSubst, end='', file=ofn)


if __name__ == '__main__':
    _this_script = sys.argv[0]
    if len(sys.argv) == 33:
        _run_env = sys.argv[1]  # DEV
        _db_env = sys.argv[2]  # DEV99

        dbs = DatabaseSetupIni()
        g_read_template_path = dbs.get_read_template_path()
        g_write_bteq_path = dbs.get_write_bteq_path()
        g_td_sys_name = dbs.get_td_sys_name(_run_env)

        main(_db_env)
    else:
        print('usage error in <script> = {}'.format(_this_script))
        print('to fix:        <script> [ DEV | TEST | PROD ] DB_ENV_Prefix')
        quit(1)

