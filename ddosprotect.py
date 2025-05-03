import time
from collections import defaultdict
from flask import Flask, request, jsonify

app = Flask(__name__)

# IP address এবং request এর timestamp গুলো স্টোর করার জন্য ডিকশনারি
ip_requests = defaultdict(list)

# Rate limiting এর সেটিংস
MAX_REQUESTS = 100  # Max requests allowed
TIME_FRAME = 60  # Time frame in seconds (1 মিনিট)
BLOCK_TIME = 600  # ব্লক সময় (10 মিনিট)

@app.route('/')
def home():
    ip = request.remote_addr  # ক্লায়েন্টের IP অ্যাড্রেস নিয়ে আসা
    current_time = time.time()

    # পুরনো request গুলো ক্লিন করা (TIME_FRAME এর বাইরে)
    ip_requests[ip] = [timestamp for timestamp in ip_requests[ip] if current_time - timestamp < TIME_FRAME]

    # IP থেকে আসা রিকোয়েস্টের সংখ্যা চেক করা (TIME_FRAME এর মধ্যে)
    if len(ip_requests[ip]) >= MAX_REQUESTS:
        return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

    # নতুন request রেকর্ড করা
    ip_requests[ip].append(current_time)
    
    return jsonify({"message": "Welcome to the website!"})

@app.route('/admin/blocked')
def blocked_ips():
    # যে IP গুলো BLOCK_TIME এর বেশি ব্লক হয়ে আছে সেগুলি দেখানো
    current_time = time.time()
    blocked_ips = {ip: timestamps for ip, timestamps in ip_requests.items() if current_time - timestamps[0] > BLOCK_TIME}
    return jsonify(blocked_ips)

if __name__ == '__main__':
    app.run(debug=True)
