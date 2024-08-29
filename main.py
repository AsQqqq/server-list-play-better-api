from flask import Flask
from flask_restful import Resource, Api
from ServerGet import servergetinfo
import json
from config import host, port




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
api.add_resource(GetInfoServers, '/api/v0.1/getinfoservers')


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