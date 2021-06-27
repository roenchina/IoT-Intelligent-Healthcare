'''
功能：设置项目常量，如DB连接参数
使用：在app.py中使用 app.config.from_object('config') 注册配置
'''
# 配置 sqlalchemy  "数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码"
SQLALCHEMY_DATABASE_URI = "mysql://root:1@localhost:3306/bsdb"
SQLALCHEMY_TRACK_MODIFICATIONS = True