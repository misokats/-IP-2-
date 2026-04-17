def ip_to_binary(ip_address):
    # ここにロジックを書いてください
    
    # 1. splitで分割
    # 2. 各数値を2進数に変換し、8文字になるよう0で埋める
    # 3. リストに格納して、最後に "." で結合する
    
    return binary_ip

# テスト
test_ip = "192.168.10.1"
print(f"10進数: {test_ip}")
print(f"2進数: {ip_to_binary(test_ip)}")
