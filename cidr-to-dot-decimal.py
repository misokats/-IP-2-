#サブネットマスク変換
#CIDR:Classless Inter-Domain Routing

def cidr_to_netmask(cidr_num):
    # 1. 全体で32ビットの「1」と「0」の文字列を作る
    binary_str = '1' *cidr_num + '0' * (32 - cidr_num)
    
    # 2. 8ビットずつに分割する
    # リスト内包表記
    octets_binary = [binary_str[i:i+8] for i in range(0, 32, 8) ]
    
    # 3. 2進数の文字列を10進数の数値に変換する : binary => decimal
    # int(文字列, 2) を使うと2進数として解釈してくれます
    # リスト内包表記
    octets_decimal = [str(int(b, 2)) for b in octets_binary]
        
    # 4. ドットで繋いで返す
    return ".".join(octets_decimal)

# --- 実行テスト ---
prefix = 24
print(f"/{prefix} のサブネットマスクは: {cidr_to_netmask(prefix)}")

prefix_custom = 18
print(f"/{prefix_custom} のサブネットマスクは: {cidr_to_netmask(prefix_custom)}")