from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from myapp.models import db, Todo

todo = Blueprint('todo', __name__, template_folder='templates/todo')

@todo.route('/todo', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            new_todo = Todo(task=task, user=current_user)
            db.session.add(new_todo)
            db.session.commit()
            flash("Task added!", "success")
        return redirect(url_for('todo.index'))

    todos = Todo.query.filter_by(user=current_user).all()
    return render_template('index.html', todos=todos)

@todo.route('/todo/toggle/<int:id>')
@login_required
def toggle(id):
    todo = Todo.query.get_or_404(id)
    if todo.user != current_user:
        flash("You can't edit another user's task.", "error")
        return redirect(url_for('todo.index'))
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('todo.index'))

@todo.route('/todo/delete/<int:id>')
@login_required
def delete(id):
    todo = Todo.query.get_or_404(id)
    if todo.user != current_user:
        flash("You can't delete another user's task.", "error")
        return redirect(url_for('todo.index'))
    db.session.delete(todo)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for('todo.index'))