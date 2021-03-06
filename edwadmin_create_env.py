import sys
from string import Template
from config_database_setup_ini import DatabaseSetupIni


def main(db_env: str, db_perm: str):
    global g_read_template_path, g_write_bteq_path
    tmp_fn = g_read_template_path + '/' + 'edwadmin_create_env.template'
    out_fn = g_write_bteq_path + '/' + 'edwadmin_create_env.' + db_env.lower() + '.btq'

    # build dictionary for template substitution
    dct2 = {}
    dct2['env'] = db_env.upper()
    dct2['perm_space'] = db_perm

    with open(tmp_fn, 'r') as f, open(out_fn, "w") as ofn:
        for ln in f:
            ln_tmpl = Template(ln)
            ln_subst = ln_tmpl.safe_substitute(dct2)  # safe_substitute: skips other ${...} without error
            print(ln_subst, end='', file=ofn)


if __name__ == '__main__':
    _this_script = sys.argv[0]
    if len(sys.argv) == 4:
        _td_sys = sys.argv[1]  # DEV
        _db_env = sys.argv[2]  # DEV99
        _db_perm = sys.argv[3]  # 10e6

        dbs = DatabaseSetupIni()
        g_read_template_path = dbs.get_read_template_path()
        g_write_bteq_path = dbs.get_write_bteq_path()

        main(_db_env, _db_perm)
    else:
        print('usage error in <script> = {}'.format(_this_script))
        print('to fix:        <script> [ DEV | TEST | PROD ] DB_ENV_Prefix')
        quit(1)
