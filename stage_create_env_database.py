
from string import Template

tmp_fn = 'stage_create_env_database.template'

db_env = 'DEV99'
dct2 = {}
dct2['env'] = db_env


out_fn = 'stage_create_env_database.' + db_env + '.btq'


x = ''
with open(tmp_fn, 'r') as f, open(out_fn, "w") as ofn:
    for txt in f:
        s = Template(txt)
        x = s.safe_substitute(dct2)   # safe_substitute: skips other ${...} without error
        print(x, end='', file=ofn)

