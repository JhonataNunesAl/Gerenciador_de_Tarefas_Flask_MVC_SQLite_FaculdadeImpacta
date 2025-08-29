from flask import render_template, request, redirect
from models.task import Task
from models.user import User  # Supondo que você tenha um model User
from database import db_session

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = db_session.query(Task).join(User).all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'GET':
            users = db_session.query(User).all()
            return render_template("create_task.html", users=users)
        elif request.method == 'POST':
            title = request.form['title']
            description = request.form.get('description')
            user_id = request.form['user_id']
            new_task = Task(title=title, description=description, user_id=user_id)
            db_session.add(new_task)
            db_session.commit()
            return redirect('/tasks')

    @staticmethod
    def update_task_status(task_id):
        task = db_session.query(Task).get(task_id)
        if task:
            task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
            db_session.commit()
        return redirect('/tasks')

    @staticmethod
    def delete_task(task_id):
        task = db_session.query(Task).get(task_id)
        if task:
            db_session.delete(task)
            db_session.commit()
        return redirect('/tasks')
