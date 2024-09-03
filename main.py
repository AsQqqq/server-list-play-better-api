from flask import Flask, request
from flask_restful import Resource, Api
from ServerGet import servergetinfo
import json
from config import host, port
from ServerGet.database import add_record_global, add_record_local



app = Flask(__name__)
api = Api(app)


class GetInfoServers(Resource):
    def get_info_server(self) -> json:
        info = {}
        result = servergetinfo().getting_corrected_information_about_server()
        for server_info in result:
            server_info_json_format_r = json.dumps(server_info)
            server_info_json_format = json.loads(server_info_json_format_r)
            info[server_info_json_format['port']] = server_info_json_format
        return info

    def get(self):
        info = self.get_info_server()
        return info
api.add_resource(GetInfoServers, '/api/v0.1/getinfoserversglobal')


class AddRecordGlobal(Resource):
    def post(self):
        # Получаем данные из запроса
        server_ip = request.json.get('server_ip')
        server_port = request.json.get('server_port')

        # Получаем IP и порт клиента
        client_ip = request.remote_addr
        client_port = request.environ.get('REMOTE_PORT')

        # Добавляем запись в глобальную таблицу
        add_record_global(
            client_ip=client_ip,
            client_port=client_port,
            server_ip=server_ip,
            server_port=server_port
        )

        return {'message': 'Запись успешно добавлена'}, 201
api.add_resource(AddRecordGlobal, '/api/v0.1/addrecordglobal')



class GetInfoServersLocal(Resource):
    def get_info_server(self) -> json:
        info = {}
        result = servergetinfo().getting_corrected_information_about_server_local()
        for server_info in result:
            server_info_json_format_r = json.dumps(server_info)
            server_info_json_format = json.loads(server_info_json_format_r)
            info[server_info_json_format['port']] = server_info_json_format
        return info

    def get(self):
        info = self.get_info_server()
        return info
api.add_resource(GetInfoServersLocal, '/api/v0.1/getinfoserverslocal')

if __name__ == '__main__':
    app.run(host, port, debug=True)