import srdata

# 単一のデータセットを取得
data_single = srdata.get_dataset("ds1.csv")
print(data_single)

# 複数のデータセットを取得
data_multiple = srdata.get_dataset(["ds1.csv", "ds2.csv"])
for data in data_multiple:
    print(data)

# データセットのツリー構造を表示
srdata.display_dataset_tree()