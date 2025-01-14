# yuvalı sözlükler
soz1 = {
    "iklim1":{
        "ad":"yağmurlu",
        "süre":"2 ay"
        },
    "iklim2":{
        "ad":"karlı",
        "süre":"3 ay"
        }
    }
for i in soz1:
    print(i, "::", soz1[i]["ad"], " ", soz1[i]["süre"])
