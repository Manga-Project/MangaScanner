# 漫畫掃描工具
## 介紹
實驗室影印機設定
```
DPI = 600
檔案類型 = "單張 TIF"
雙面掃描 = "關閉"
自動 ADF 傾斜校正 = "關閉"
```

## 程式使用
當掃描單數頁的時候。  
```bash
python main.py -n MANGA_NAME -w CROP_WIDTH -he CROP_HEIGHT -x CROP_X -y CROP_Y -c 話數 -v 集數
```

當掃描雙數頁的時候，請由最後一張往前掃 (不用將個別漫畫翻面)。  
```bash
python main.py -n MANGA_NAME -w CROP_WIDTH -he CROP_HEIGHT -x CROP_X -y CROP_Y -c 話數 -v 集數 --reversed
```

* `--target_ext` : Input 目標檔案格式
* `--delete_scanned` : 刪除掃描過的檔案

## 作者
[ImRTon 阿湯](https://imRTon.github.io)