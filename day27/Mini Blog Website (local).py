# Day 27 — Flask Mini Blog
# pip install flask

from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
POSTS = []  # in-memory (resets on restart)

TEMPLATE = """
<!doctype html>
<title>Mini Blog</title>
<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
<header><h1>Mini Blog</h1></header>
<main>
  <section>
    <h2>Create a Post</h2>
    <form method="POST" action="/new">
      <input name="title" placeholder="Title" required>
      <textarea name="content" placeholder="Write something..." required></textarea>
      <button type="submit">Publish</button>
    </form>
  </section>
  <section>
    <h2>Recent Posts</h2>
    {% if posts %}
      {% for p in posts %}
        <article>
          <h3>{{p.title}}</h3>
          <p>{{p.content}}</p>
        </article>
      {% endfor %}
    {% else %}
      <p>No posts yet. Write one!</p>
    {% endif %}
  </section>
</main>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, posts=POSTS)

@app.route("/new", methods=["POST"])
def new_post():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()
    if title and content:
        POSTS.insert(0, {"title": title, "content": content})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
