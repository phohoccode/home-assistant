# Home Assistant Project

## Giới thiệu
Dự án Home Assistant - Hệ thống nhà thông minh toàn diện.

## Yêu cầu hệ thống
- Python 3.9 trở lên
- pip (Python package manager)
- 2GB RAM tối thiểu
- Kết nối Internet

## Hướng dẫn cài đặt

### 1. Clone Repository
```bash
git clone https://github.com/phohoccode/home-assistant.git
cd home-assistant
```

### 2. Tạo và kích hoạt môi trường ảo
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### 4. Cấu hình Home Assistant
- Chỉnh sửa file `configuration.yaml` trong thư mục `homeassistant/` để phù hợp với hệ thống của bạn.

### 5. Chạy Home Assistant
```bash
python -m homeassistant --config ./homeassistant
```

### 6. Truy cập giao diện web
- Mở trình duyệt và truy cập: `http://localhost:8123`

## Ghi chú
- Đảm bảo rằng các dịch vụ cần thiết như MQTT và MariaDB đã được cấu hình đúng.
