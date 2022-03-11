import requests
from  requests import ConnectionError,HTTPError,Timeout

def download_youbike_data():
    try:
        youbikeurl = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
        response = requests.get(youbikeurl)
        response.raise_for_status()
    except ConnectionError as e:
        print("網路連線有問題")
        print(e)
        return
    except HTTPError as e:
        print("statusCode不是200，連線取得資料有問題")
        print(e)
        return
    except Timeout as e:
        print("伺服器忙線中")
        print(e)
        return
    except:
        print("非預期中的錯誤")
        return

    allData = response.json()
    return list(allData["retVal"].values())