from flask import Flask, render_template, request, redirect, url_for

books = [
    {"id": 1, "title": "დონ კიხოტი", "author": "მიგელ დე სერვანტესი", "description": "სათავგადასავლო რომანი"},
    {"id": 2, "title": "ომი და მშვიდობა", "author": "ლევ ტოლსტოი", "description": "ისტორიულ-ფილოსოფიური ნაწარმოები"},
    {"id": 3, "title": "უცნაური შემთხვევა დოქტორ ჯეკილისა და მისტერ ჰაიდის", "author": "რობერტ ლუის სტივენსონი", "description": "თრილერი"},
    {"id": 4, "title": "ბრმა საათი", "author": "თომას ჰარისი", "description": "დეტექტიური რომანი"},
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", books=books)
@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break
    if not book:
        return "წიგნი ვერ მოიძებნა", 404
    return render_template("book_detail.html", book=book)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)