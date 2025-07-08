# Django 留言板練習專案

這是在 macOS 上用 Django 建立的留言板網站，使用 MVT 架構，並且以 Django REST Framework（DRF）將原本的留言板網站擴充為支援 RESTful API 的版本，包括：
- 留言 Model
- 表單輸入與 CSRF 防護
- HTML Template 顯示所有留言
- 使用 SQLite 資料庫
- 使用 Token 新增與查詢留言



## 如何啟動
```bash
python manage.py runserver
