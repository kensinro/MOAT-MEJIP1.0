import subprocess, sys, json, pathlib
root=pathlib.Path(__file__).resolve().parent
r=subprocess.run([sys.executable,str(root/'mejip_mvp.py'),'self-test'],capture_output=True,text=True)
assert r.returncode==0, r.stderr or r.stdout
out=json.loads(r.stdout)
assert out['pass'] is True
