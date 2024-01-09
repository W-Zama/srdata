import pandas as pd
import pkgutil
import io
import os
from matplotlib import pyplot as plt

package_name = __name__.split('.')[0]

def get_dataset(file_names):
    # 単一の文字が入力された場合，リストに変換
    if isinstance(file_names, str):
        file_names = [file_names]

    datasets = []
    for file_name in file_names:
        data = pkgutil.get_data(package_name, 'Dataset' + '/' + file_name)
        data_str = data.decode('utf-8')
        data_io = io.StringIO(data_str)
        dataset = pd.read_csv(data_io, index_col=0)
        datasets.append(dataset)

    # 入力が単一の文字列だった場合、リストではなく単体のデータセットを返す
    if len(datasets) == 1:
        return datasets[0]
    else:
        return datasets

def display_dataset_tree(directory_path=os.path.dirname(os.path.abspath(__file__)) + '/' + 'Dataset', indent='', is_first_call=True):
    # 最初の呼び出しは"Dataset"と出力する
    if is_first_call:
        print('Dataset')

    items = sorted(os.listdir(directory_path))
    if '.DS_Store' in items:
        items.remove('.DS_Store')

    for index, item in enumerate(items):
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path):
            if index == len(items) - 1:
                print(f"{indent}└─ {item}")
                display_dataset_tree(item_path, indent + "   ", False)
            else:
                print(f"{indent}├─ {item}")
                display_dataset_tree(item_path, indent + "│  ", False)
        else:
            if index == len(items) - 1:
                print(f"{indent}└─ {item}")
            else:
                print(f"{indent}├─ {item}")

def show_graph(file_name, step=False, grid=True, **kwargs):
    data = get_dataset(file_name)
    plt.figure()

    if step:
        plt.step(data.index.values, data.iloc[:, 0].values, **kwargs)
    else:
        plt.plot(data.index.values, data.iloc[:, 0].values, **kwargs)

    if grid:
        plt.grid()
    plt.xlabel(data.index.name)
    plt.ylabel(data.columns[0])
    plt.show()

def show_cum_graph(file_name, step=False, grid=True, **kwargs):
    data = get_dataset(file_name)
    cum_data = data # copy
    new_row = pd.DataFrame({data.columns[0]: [0]}, pd.Index([0], name=data.index.name)) # 時刻0で発見数0
    cum_data = pd.concat([new_row, cum_data], axis=0)
    cum_data.iloc[:, 0] = cum_data.iloc[:, 0].cumsum()  # 累積和を計算

    plt.figure()

    if step:
        plt.step(cum_data.index.values, cum_data.iloc[:, 0].values, **kwargs)
    else:
        plt.plot(cum_data.index.values, cum_data.iloc[:, 0].values, **kwargs)

    if grid:
        plt.grid()
    plt.xlabel(cum_data.index.name)
    plt.ylabel("cumlative_" + cum_data.columns[0])
    plt.show()