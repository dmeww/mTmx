
import os
import requests


def get_v6() -> str:
    ipv6 = requests.get('http://6.ipw.cn')
    return ipv6.text


cmd = "curl -X PUT 'https://api.cloudflare.com/client/v4/zones/5bd802101fe174f295d4aa657d2fecfa/dns_records/a2fbe600e56299fa7bc8e4ac6d21f5a4' -H 'X-Auth-Email: dygticky@gmail.com' -H 'X-Auth-Key: 0960b0600d5c64b24cc2e41db0eeb2ca94426' -H 'Content-Type: application/json' --data '{\"type\":\"AAAA\",\"name\":\"dygticky.cf\",\"content\":\""+get_v6(
)+"\",\"ttl\":120,\"proxied\":false}'"


os.system(cmd)