from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        filtered_posts = [post for post in posts if search.lower() in post['title'].lower() or search.lower() in post['content'].lower()]
    else:
        filtered_posts = posts
    return render_template('index.html', posts=filtered_posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts[post_id] = {'title': title, 'content': content}
        return redirect(url_for('index'))
    return render_template('update.html', post=posts[post_id])

@app.route('/delete/<int:post_id>')
def delete(post_id):
    del posts[post_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
