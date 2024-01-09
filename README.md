# srdata について
製作者: Wataru Zama

**srdata**(Software reliability dataset)は，python でソフトウェアフォールト発見数データやソフトウェアフォールト発見時間間隔データといった，ソフトウェア信頼性に関連するデータを簡単にインポートすることができるライブラリです．


# インストール方法
コマンドラインで
```
pip install git+https://github.com/W-Zama/srdata.git
```
と打ち込んでインストールできます．

# データセットについて

## データセット情報
気が向いたら書きます．

## データセットの形式
1番左にindexとなるカラムをおいてください（csvをpandas.Dataframeに変換するときに，そのように処理されます）．

## データセットの保存場所
データセットは`/srdata/dataset/`に入っています．また，コマンドラインで，
```
pip show srdata
```
と打ち込むことにより，ローカルの環境でのsrdataのロケーションが確認できます．

# 使い方

## インポートする
```python
import srdata
```

## 単一のデータセットを取得する
```python
data_single = srdata.get_dataset("Lyu/J1.csv")
print(data_single)
```

<details>
<summary>出力（クリックで開きます）</summary>

```
    time_interval  number_of_failures
0               1                   6
1               2                   1
2               3                   1
3               4                   0
4               5                   1
..            ...                 ...
57             58                   1
58             59                   0
59             60                   1
60             61                   0
61             62                   2

[62 rows x 2 columns]
```
</details>

## 複数のデータセットを取得する
```python
data_multiple = srdata.get_dataset(["Lyu/J1.csv", "Lyu/J2.csv"])
print(data_multiple[0])
print(data_multiple[1])
```
<details>
<summary>出力（クリックで開きます）</summary>

```
    time_interval  number_of_failures
0               1                   6
1               2                   1
2               3                   1
3               4                   0
4               5                   1
..            ...                 ...
57             58                   1
58             59                   0
59             60                   1
60             61                   0
61             62                   2

[62 rows x 2 columns]
     time_interval  number_of_failures
0                1                   0
1                2                   0
2                3                   0
3                4                   1
4                5                   1
..             ...                 ...
176            177                   0
177            178                   0
178            179                   0
179            180                   0
180            181                   1

[181 rows x 2 columns]
```
</details>


# データセットのツリー構造を表示する

```python
srdata.display_dataset_tree()
```

<details>
<summary>出力（クリックで開きます）</summary>

```
Dataset
├─ Cumulative Time to Failure
│  ├─ ds1.dat
│  ├─ ds10.dat
│  ├─ ds11.dat
│  ├─ ds12.dat
│  ├─ ds13.dat
│  ├─ ds14.dat
│  ├─ ds15.dat
│  ├─ ds16.dat
│  ├─ ds17.dat
│  ├─ ds18.dat
│  ├─ ds19.dat
│  ├─ ds2.dat
│  ├─ ds20.dat
│  ├─ ds21.dat
│  ├─ ds22.dat
│  ├─ ds23.dat
│  ├─ ds24.dat
│  ├─ ds25.dat
│  ├─ ds3.dat
│  ├─ ds4.dat
│  ├─ ds5.dat
│  ├─ ds6.dat
│  ├─ ds7.dat
│  ├─ ds8.dat
│  └─ ds9.dat
├─ Lyu
│  ├─ J1.csv
│  ├─ J2.csv
│  ├─ J3.csv
│  ├─ J4.csv
│  └─ J5.csv
├─ Time to Failure
│  ├─ ds1.dat
│  ├─ ds10.dat
│  ├─ ds11.dat
│  ├─ ds12.dat
│  ├─ ds13.dat
│  ├─ ds14.dat
│  ├─ ds15.dat
│  ├─ ds16.dat
│  ├─ ds17.dat
│  ├─ ds18.dat
│  ├─ ds19.dat
│  ├─ ds2.dat
│  ├─ ds20.dat
│  ├─ ds21.dat
│  ├─ ds22.dat
│  ├─ ds23.dat
│  ├─ ds24.dat
│  ├─ ds25.dat
│  ├─ ds3.dat
│  ├─ ds4.dat
│  ├─ ds5.dat
│  ├─ ds6.dat
│  ├─ ds7.dat
│  ├─ ds8.dat
│  └─ ds9.dat
├─ ds1.csv
├─ ds2.csv
├─ ds3.csv
├─ ds4.csv
├─ ds5.csv
├─ ds6.csv
├─ musa
│  ├─ ss1a.csv
│  ├─ ss1ag.csv
│  ├─ ss1b.csv
│  ├─ ss1bg.csv
│  ├─ ss1c.csv
│  ├─ ss1cg.csv
│  ├─ ss2.csv
│  ├─ ss2g.csv
│  ├─ ss3.csv
│  ├─ ss3g.csv
│  ├─ ss4.csv
│  ├─ ss4g.csv
│  ├─ sys1.csv
│  ├─ sys14c.csv
│  ├─ sys14cg.csv
│  ├─ sys17.csv
│  ├─ sys17g.csv
│  ├─ sys1g.csv
│  ├─ sys2.csv
│  ├─ sys27.csv
│  ├─ sys27g.csv
│  ├─ sys2g.csv
│  ├─ sys3.csv
│  ├─ sys3g.csv
│  ├─ sys4.csv
│  ├─ sys40.csv
│  ├─ sys40g.csv
│  ├─ sys4g.csv
│  ├─ sys5.csv
│  ├─ sys5g.csv
│  ├─ sys6.csv
│  └─ sys6g.csv
├─ ohba
│  └─ ohba_PLI.csv
└─ tohma
   └─ tohma.csv
```
</details>
