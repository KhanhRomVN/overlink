#!/bin/bash

set -e  # Lỗi sẽ dừng script

echo "🔄 Đang xóa các thư mục build cũ..."
rm -rf dist build *.egg-info

echo "🛠️  Đang build lại package..."
python setup.py sdist bdist_wheel

echo "Kiểm tra bản build..."
twine check dist/*

echo "🚀 Đang upload lên PyPI (dán API token khi được hỏi)..."
twine upload dist/*


