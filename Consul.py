import consul

consul_server = consul.Consul(host='localhost', port=8500)
consul_kv = consul_server.kv.get(key='', recurse=True)
# print(consul_kv)
for item in consul_kv[1]:
    print(f"Key is {item['Key']} and value is {item['Value']}")
