config = []
import pathlib
for line in open("config.cfg").readlines():
    linem1 = line.replace(" = ", "-").replace("\n", "")
    linem2 = linem1.split("-")
    config.append({linem2[0]: linem2[1]})
version = config[0]['version']
root = config[1]['root']
addons = config[2]['addons']
if pathlib.Path(addons).exists():
    pass
else:
    pathlib.Path(addons).mkdir()
if pathlib.Path("root/logo.jpg").exists():
    from root.mmmm import run
    run()
else:
    input("Please insert the setup files press Enter when ready")
    from root.setup import setup
    setup()