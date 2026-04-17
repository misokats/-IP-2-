#サブネットマスク変換
#CIDR:Classless Inter-Domain Routing

def cidr_to_netmask(cidr_num):
    # 1. 全体で32ビットの「1」と「0」の文字列を作る
    # 例: /24 なら 1が24個、0が8個
    ones = '1' * cidr_num
    zeros = '0' * (32 - cidr_num)
    binary_str = ones + zeros
    
    # 2. 8ビットずつに分割する
    # 0-8文字目, 8-16文字目...と切り分ける => リスト
    octets_binary = [
        binary_str[0:8],
        binary_str[8:16],
        binary_str[16:24],
        binary_str[24:32]
    ]
    
    # 3. 2進数の文字列を10進数の数値に変換する : binary => decimal
    # int(文字列, 2) を使うと2進数として解釈してくれます
    octets_decimal = []
    for b in octets_binary:
        decimal_val = int(b, 2)
        octets_decimal.append(str(decimal_val))
    
    # 4. ドットで繋いで返す
    return ".".join(octets_decimal)

# --- 実行テスト ---
prefix = 24
print(f"/{prefix} のサブネットマスクは: {cidr_to_netmask(prefix)}")

prefix_custom = 18
print(f"/{prefix_custom} のサブネットマスクは: {cidr_to_netmask(prefix_custom)}")