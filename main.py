from flask import Flask, request
from flask_restful import Resource, Api
from ServerGet import servergetinfo
import json
from config import host, port, api_version
from ServerGet.database import add_record_global, add_record_local, add_record_program


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
api.add_resource(GetInfoServers, f'/api/{api_version}/getinfoserversglobal')


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

        return {'message': 'The entry was successfully added'}, 201
api.add_resource(AddRecordGlobal, f'/api/{api_version}/addrecordglobal')


class AddRecordProgramList(Resource):
    def post(self):
        # Получаем данные из запроса
        program_version = request.json.get('program_version')

        # Получаем IP и порт клиента
        client_ip = request.remote_addr
        client_port = request.environ.get('REMOTE_PORT')

        # Добавляем запись в программный список
        add_record_program(
            client_ip=client_ip,
            client_port=client_port,
            program_version=program_version
        )

        return {'message': 'The entry was successfully added'}, 201
api.add_resource(AddRecordProgramList, f'/api/{api_version}/addrecordprogram')


class AddRecordLocal(Resource):
    def post(self):
        # Получаем данные из запроса
        server_ip = request.json.get('server_ip')
        server_port = request.json.get('server_port')

        # Получаем IP и порт клиента
        client_ip = request.remote_addr
        client_port = request.environ.get('REMOTE_PORT')

        # Добавляем запись в локальную таблицу
        add_record_local(
            client_ip=client_ip,
            client_port=client_port,
            server_ip=server_ip,
            server_port=server_port
        )

        return {'message': 'The entry was successfully added'}, 201
api.add_resource(AddRecordLocal, f'/api/{api_version}/addrecordlocal')



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
api.add_resource(GetInfoServersLocal, f'/api/{api_version}/getinfoserverslocal')

if __name__ == '__main__':
    app.run(host, port, debug=True)