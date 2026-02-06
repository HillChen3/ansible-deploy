from flask import Blueprint
from flask import request
from flask import send_from_directory
import time,os,json
ansible_test = Blueprint("ansible_test", __name__)

@ansible_test.route('/index')
def index():
    return "Ansible Deploy Blueprint!"

@ansible_test.route('/ajaxtest')
def ajaxtest():
    return "Ansible Ajax Test Content!"

@ansible_test.route('/ajaxget')
def ajaxget():
    server_name = request.args.get('server_name')
    server_ip = request.args.get('server_ip')
    return "Server Name is: {0}, Server IP is {1}".format( server_name, server_ip )

@ansible_test.route('/ajaxpost', methods=['get', 'post'])
def ajaxpost():
    info = request.get_data()
    info = json.loads(info)
    return info['username']

@ansible_test.route('/download')
def download():
    curent_dir = os.path.dirname( os.path.realpath(__file__) )
    return send_from_directory( curent_dir+"/static", "serverexample.xlsx", as_attachment=True )

@ansible_test.route('/upload', methods=['get', 'post'])
def upload():
    servers = request.files.get('servers')
    ramname = int(time.time() * 1000)
    print( ramname )
    servers.save('/tmp/{0}'.format( ramname ))
    return "Upload Success!"

@ansible_test.route('/get')
def get():
    print( request.args )
    server_name = request.args.get("server_name")
    server_ip = request.args.get("server_ip")
    return "Server name is: {0}, Server IP is: {1}".format(server_name, server_ip)

@ansible_test.route('/post', methods=['get', 'post'])
def post():
    print( request.form )
    username = request.form.get("username")
    password = request.form.get("password")
    return "username is: {0}, password is: {1}".format(username, password)