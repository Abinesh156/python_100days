# def primechecker(num):
#     if num <= 1:
#         print("Not a prime number")
#         return
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             return
#     print("Prime number")

# num = int(input("Enter a number: "))
# primechecker(num)


from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Prime Number Checker</title>
</head>
<body>
    <h1>Prime Number Checker</h1>
    <form method="post">
        <label>Enter a number:</label>
        <input type="number" name="num" required>
        <input type="submit" value="Check">
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

def primechecker(num):
    if num <= 1:
        return "Not a prime number"
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime number"
    return "Prime number"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num = int(request.form["num"])
            result = primechecker(num)
        except:
            result = "Invalid input"
    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
