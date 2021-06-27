from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager, Server

from app import app
from app import db

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand) # 创建数据库映射命令
# manager.add_command('start', Server(port=8000, use_debugger=True)) # 创建启动命令

if __name__ == '__main__':
    manager.run()