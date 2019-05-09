import sys
from string import Template
from config_database_setup_ini import DatabaseSetupIni


def main(db_perm: str):
    global g_read_template_path, g_write_bteq_path
    tmp_fn = g_read_template_path + '/' + 'dbc_create_edwadmin.template'
    out_fn = g_write_bteq_path + '/' + 'dbc_create_edwadmin.btq'

    # build dictionary for template substitution
    dct2 = {}
    dct2['perm_space'] = db_perm

    with open(tmp_fn, 'r') as f, open(out_fn, "w") as ofn:
        for ln in f:
            lntmpl = Template(ln)
            lnsubst = lntmpl.safe_substitute(dct2)  # safe_substitute: skips other ${...} without error
            print(lnsubst, end='', file=ofn)


if __name__ == '__main__':
    _this_script = sys.argv[0]
    if len(sys.argv) == 2:
        _db_perm = sys.argv[1]  # 1e9

        dbs = DatabaseSetupIni()
        g_read_template_path = dbs.get_read_template_path()
        g_write_bteq_path = dbs.get_write_bteq_path()

        main(_db_perm)
    else:
        print('usage error in <script> = {}'.format(_this_script))
        print('to fix:        <script> PERM_SPACE')
        quit(1)
