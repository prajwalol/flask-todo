from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize the list to store tasks
kaam = []


@app.route('/')
def hello():
    return '<h1>Write /todo to add your todo</h1>'


@app.route('/todo', methods=["GET", "POST"])
def todo():
    if request.method == 'GET':
        return render_template('todo.html', kaam=kaam)
    else:
        try:
            task = request.form['todo']
            kaam.append(task)
        except KeyError:
            # This is not a POST request, do nothing
            pass
        return redirect('/todo')


@app.route('/remove_todo', methods=["POST"])
def remove_todo():
    if request.method == 'POST':
        try:
            task_index_to_remove = int(request.form['id'])
            if 0 <= task_index_to_remove < len(kaam):
                kaam.pop(task_index_to_remove)
        except (ValueError, IndexError):
            # Invalid index or task not found, do nothing
            pass
        return redirect('/todo')


if __name__ == '__main__':
    app.run(debug=True)
