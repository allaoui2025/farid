#!/bin/bash

echo "🔧 نشر التطبيق..."

# مثال: تشغيل Flask app
export FLASK_APP=app.py
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=5000
chmod +x deploy.sh
