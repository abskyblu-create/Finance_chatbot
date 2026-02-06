print(">>> flask_app.py started running")


from flask import Flask, request, render_template_string
from chatbot_logic import chatbot_web, df

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Finance Chatbot</title>
</head>
<body>
    <h2>Finance Chatbot</h2>

    <form method="post">
        <input type="text" name="query" placeholder="Ask question..." size="50">
        <input type="submit" value="Ask">
    </form>

    {% if response %}
        <h3>Response:</h3>
        <pre>{{ response }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_query = request.form.get("query", "")
        response = chatbot_web(user_query, df)
    return render_template_string(HTML_PAGE, response=response)

if __name__ == "__main__":
    app.run(debug=True)

