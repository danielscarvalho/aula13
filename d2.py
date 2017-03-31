#dicionário com listas

mdici={"x":[2,3,4],
       "y":[5,6,7],
       "z":{"a":[8,9,10],
            "b":[11,12]}}

dc=mdici["z"]["b"]
dc[0]=888
print(dc)

print(mdici["z"]["b"][0])

print(mdici["y"][1])

print(mdici)