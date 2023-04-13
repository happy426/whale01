import json
text = """
{"data": {"errno": 10000, "errmsg": "success", "data": {"entities": [{"timestamp": 1679803200, "count": 232}, {"timestamp": 1679806800, "count": 287}, {"timestamp": 1679810400, "count": 278}, {"timestamp": 1679814000, "count": 398}, {"timestamp": 1679817600, "count": 317}, {"timestamp": 1679821200, "count": 448}, {"timestamp": 1679824800, "count": 284}, {"timestamp": 1679828400, "count": 276}, {"timestamp": 1679832000, "count": 241}, {"timestamp": 1679835600, "count": 415}, {"timestamp": 1679839200, "count": 308}, {"timestamp": 1679842800, "count": 356}]}}, "profile": {"transportRttEstimate": 24, "domainLookUpStart": 1679994642182, "responseEnd": 1679994642248, "sendBytesCount": 766, "redirectStart": 0, "connectEnd": 1679994642182, "protocol": "http/1.1", "peerIP": "47.103.138.166", "requestStart": 1679994642180, "socketReused": true, "fetchStart": 1679994642180, "SSLconnectionStart": 1679994642182, "estimate_nettype": 5, "httpRttEstimate": 72, "throughputKbps": 0, "SSLconnectionEnd": 1679994642182, "downstreamThroughputKbpsEstimate": 1961, "domainLookUpEnd": 1679994642182, "responseStart": 1679994642245, "redirectEnd": 0, "rtt": 44, "connectStart": 1679994642182, "port": 443, "receivedBytedCount": 564, "requestEnd": 1679994642247}, "header": {"Transfer-Encoding": "chunked", "Strict-Transport-Security": "max-age=15724800; includeSubDomains", "Cache-Control": "no-store", "Server": "openresty/1.15.8.1", "Access-Control-Allow-Origin": "*", "Connection": "keep-alive", "Content-Encoding": "gzip", "Vary": "Accept-Encoding", "Pragma": "no-cache", "Date": "Tue, 28 Mar 2023 09:10:40 GMT", "Content-Type": "application/json;charset=UTF-8"}, "statusCode": 200, "cookies": [], "errMsg": "request:ok"}
"""
json_text = json.loads(text)
j_list = json_text['data']['data']['entities']
num = 0
for i in j_list:
    num += int(i['count'])
print(num)


