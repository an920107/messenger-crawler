# Messenger Crawler

## 這是什麼

一個偵測 Messenger 新訊息，並自動以 ChatGPT 回覆訊息，的 Messenger 爬蟲

## 使用方式

1. 於專案根目錄新建一個 `data` 的資料夾，底下新增兩個檔案：`cookies.json`、`gptconfig.json`，或是將 `example` 資料夾改名為 `data`

2. 複製已登入的 Messenger cookies 到 `cookies.json`
   > 取得 cookies 的插件：https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=zh-TW

3. 於 `gptconfig.json` 中修改 `key` 的值