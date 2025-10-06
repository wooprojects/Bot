from flask import Flask, render_template, request, jsonify
import os
import logging

app = Flask(__name__)

# تنظیمات
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def index():
    """صفحه اصلی مینی اپ"""
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """API برای دریافت داده"""
    sample_data = {
        "message": "سلام از مینی اپ!",
        "features": ["امکان ۱", "امکان ۲", "امکان ۳"],
        "status": "active"
    }
    return jsonify(sample_data)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    """API برای دریافت داده از کاربر"""
    data = request.json
    user_input = data.get('text', '')
    
    # پردازش داده (اینجا می‌توانید به ربات ارسال کنید)
    response = {
        "status": "success",
        "message": f"داده دریافت شد: {user_input}",
        "processed": user_input.upper()
    }
    
    return jsonify(response)

@app.route('/health')
def health_check():
    """بررسی سلامت سرور"""
    return jsonify({"status": "healthy", "service": "telegram-miniapp"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
