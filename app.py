from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)

# -----------------------------
# URL SAFETY CHECK FUNCTION
# -----------------------------
def check_url(url):
    score = 0

    # Long URL
    if len(url) > 75:
        score += 1

    # @ symbol
    if "@" in url:
        score += 1

    # Domain extraction
    domain = urlparse(url).netloc

    # Hyphen in domain
    if "-" in domain:
        score += 1

    # IP address check
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        score += 2

    # HTTPS check
    if not url.startswith("https"):
        score += 1

    # Suspicious keywords
    suspicious_words = ["login", "verify", "bank", "secure", "account"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Final result
  def check_website(url):
    # Example logic
    score = 0  # Replace with your real logic

    if score <= 1:
        result_type = "safe"
        result = "THIS WEBSITE IS 100% SAFE."
    elif score <= 3:
        result_type = "warning"
        result = "THIS WEBSITE SEEMS SUSPICIOUS."
    else:
        result_type = "danger"
        result = "THIS WEBSITE IS DANGEROUS. DO NOT ENTER PERSONAL INFO."

    return result, result_type


# -----------------------------
# HOME PAGE ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        url = request.form["url"]
        result = check_url(url)

    return render_template("index.html", result=result)


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




