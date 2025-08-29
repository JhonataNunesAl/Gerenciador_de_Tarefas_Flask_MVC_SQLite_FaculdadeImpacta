import os
from flask import Flask
from config import Config # importa as 
from controllers.user_controller import UserController
from models.user import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)

# cria tabelas

with app.app_context():
    db.create_all()

# forma alternativa de criar rotas, parâmetros: rota em si, endpoint interno do flask e função a ser executada quando a URL for acessada
app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])
app.add_url_rule('/task', 'task', TaskController.task)
app.add_url_rule('/task', 'create_task', TaskController.task, methods=['GET', 'POST'])
app.add_url_rule('/tasks', 'listar_tasks', TaskController.listar_tasks)
app.add_url_rule('/tasks/new', 'criar_task', TaskController.criar_task, methods=['GET', 'POST'])
app.add_url_rule('/tasks/atualizar/<int:task_id>', 'atualizar_task_status', TaskController.atualizar_task_status, methods=['POST'])
app.add_url_rule('/tasks/deletar/<int:task_id>', 'deletar_task', TaskController.deletar_task, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True, port=5002)