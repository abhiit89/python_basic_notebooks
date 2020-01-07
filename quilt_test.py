import quilt3

p = quilt3.Package.browse('aleksey/hurdat', 's3://quilt-example')
print(p["requirements.txt"])
print(p["notebooks"])
p["notebooks"]["QuickStart.ipynb"].fetch()
