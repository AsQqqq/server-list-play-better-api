from ServerGet.ConfigRead import read_all_port, read_ip, read_local_ip
import concurrent.futures, socket, a2s
QUERY_TIMEOUT = 4
import socket


class servergetinfo:
    def __init__(self):
        self.ip = read_ip()
        self.ports = read_all_port()
        self.local_ip = read_local_ip()
        self.debug = False


    def get_server_info(self):
        """Функция для получения информации о серверах из конфигурационного файла

        Raises:
            info_except: Информация о серверах

        Returns:
            _type_: Список словарей с информацией о серверах
        """


        info = []
        for port in self.ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    sock.settimeout(5)  # Устанавливаем таймаут на 5 секунд
                    ip, port = self.ip, int(port)
                    info_error = False

                    # Запрос подключения к серверу
                    try:
                        socket.getaddrinfo(ip, port)
                    except socket.gaierror:
                        if self.debug:
                            print("Неверный адрес сервера")
                        info_error = True
                    
                    try:
                        # Получение информации о сервере
                        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                            info_future = pool.submit(
                                a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
                    except:
                        info_error = True
                    
                    if info_error != True:
                        # Инфомария сервера
                        info_res = info_future.result()
                        print(info_res)
                        info.append([info_res, [ip, port]])
            except Exception as e:
                if self.debug:
                    print(f"Сервер не ответил: {ip}:{port} -- {e}")
            
        return info
    

    def getting_corrected_information_about_server(self) -> list:
        info_servers = []
        for info in self.get_server_info():
            info_server = info[0]
            ip_port = info[1]
            ip, port = ip_port[0], ip_port[1]

            """
            карта - название карты (зависит от названия сервера)
            игроков сейчас
            игроков максимум
            название - название сервера
            пинг - время ответа сервера в миллисекундах
            ссылка на подключение
            """

            if "Arena" in str(info_server.server_name):
                map_ = "am_mirage_custom"
            else:
                map_ = info_server.map_name
            
            now_players = info_server.player_count
            max_players = info_server.max_players
            server_name = info_server.server_name
            ping = round(float(info_server.ping), 3)
            connect_server = f"steam://connect/{ip}:{port}"
            
            if self.debug:
                print("\nУспех!")
                print('-------')

                print(f"Карта: {map_}")
                print(f"Сейчас игроков {now_players} из {max_players}")
                print(f"Сервер: {server_name}")
                print(f"Пинг: {ping}")
                print(f"Ссылка на подключение: {connect_server}")
                print(f"Порт сервера: {port}")
                
                print('-------')

            info_servers.append(
                {
                    "map": map_,
                    "now_players": now_players,
                    "max_players": max_players,
                    "server_name": server_name,
                    "ping": ping,
                    "connect_server": connect_server,
                    "port": port
                }
                )
        return info_servers
    
    
    def getting_corrected_information_about_server_local(self) -> list:
        info_servers = []
        for info in self.get_server_info():
            info_server = info[0]
            ip_port = info[1]
            ip, port = ip_port[0], ip_port[1]

            """
            карта - название карты (зависит от названия сервера)
            игроков сейчас
            игроков максимум
            название - название сервера
            пинг - время ответа сервера в миллисекундах
            ссылка на подключение
            """

            if "Arena" in str(info_server.server_name):
                map_ = "am_mirage_custom"
            else:
                map_ = info_server.map_name
            
            now_players = info_server.player_count
            max_players = info_server.max_players
            server_name = info_server.server_name
            ping = round(float(info_server.ping), 3)
            connect_server = f"steam://connect/{self.local_ip}:{port}"
            
            if self.debug:
                print("\nУспех!")
                print('-------')

                print(f"Карта: {map_}")
                print(f"Сейчас игроков {now_players} из {max_players}")
                print(f"Сервер: {server_name}")
                print(f"Пинг: {ping}")
                print(f"Ссылка на подключение: {connect_server}")
                print(f"Порт сервера: {port}")
                
                print('-------')

            info_servers.append(
                {
                    "map": map_,
                    "now_players": now_players,
                    "max_players": max_players,
                    "server_name": server_name,
                    "ping": ping,
                    "connect_server": connect_server,
                    "port": port
                }
                )
        return info_servers

