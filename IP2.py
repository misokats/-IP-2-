# def ip_to_binary(ip_address):
#     #octets:10進数のIPアドレスを.で分割してリスト化
#     #octet:octetsの要素
#     #binary_octets:
    
#     # 1. splitで分割
#     octets = ip_adress.split('.')
#     #
#     # 2. 各数値を2進数に変換し、8文字になるよう0で埋める
#     # 3. リストに格納して、最後に "." で結合する
    
#     return binary_ip

# # テスト
# test_ip = "192.168.10.1"
# print(f"10進数: {test_ip}")
# print(f"2進数: {ip_to_binary(test_ip)}")

#######################################################

def ip_to_binary(ip_address):
    # 1. ipアドレスをドットで分割してリストにする (例: ["192", "168", "10", "1"])
    octets = ip_address.split('.')
    
    #8桁の2進数の要素4つのリスト
    binary_octets = []
    
    for octet in octets:
        #リストoctetsの各要素octetの文字列を数値(int)に変換
        num = int(octet)
        
        # 2進数の文字列に変換する関数：bin
        # bin(192) は '0b11000000' になるので、[2:] で先頭の '0b' をカット
        binary_num = bin(num)[2:]
        
        # 8桁になるように左側を '0' で埋める　=> binary_num_filled
        # これをやらないと '1' が '1' のままになり、IPアドレスとして読みにくくなります
        binary_num_filled = binary_num.zfill(8)
        
        # 5. リストbinary_octetsに追加
        binary_octets.append(binary_num_filled)
    
    # 6. リストの各要素をドットで繋いで1つの文字列にする:join
    return ".".join(binary_octets)

# --- 実行テスト ---
input_ip = "192.168.10.1"
result = ip_to_binary(input_ip)

print(f"入力（10進数）: {input_ip}")
print(f"出力（ 2進数 ）: {result}")
