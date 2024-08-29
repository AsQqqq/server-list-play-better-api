import configparser, glob


def read_all_port() -> configparser.ConfigParser:
    """Функция чтения всех портов из конфигурационного файла

    Returns:
        configparser.ConfigParser: Обьект возращает конфигурационный парсер с портами
    """

    if glob.glob("ServerGet/config/port.ini"):
        config = configparser.ConfigParser()
        config.read("ServerGet/config/port.ini")
        return config['PORT']['ports'].replace(' ', '').split(',')
    return None


def read_ip() -> configparser.ConfigParser:
    """Функция чтения айпи из конфигурационного файла

    Returns:
        configparser.ConfigParser: Обьект возращает конфигурационный парсер с портами
    """

    if glob.glob("ServerGet/config/ip.ini"):
        config = configparser.ConfigParser()
        config.read("ServerGet/config/ip.ini")
        return config['IP']['ip']
    return None


def read_local_ip() -> configparser.ConfigParser:
    """Функция чтения локального айпи из конфигурационного файла

    Returns:
        configparser.ConfigParser: Обьект возращает конфигурационный парсер с портами
    """

    if glob.glob("ServerGet/config/ip.ini"):
        config = configparser.ConfigParser()
        config.read("ServerGet/config/server_data.ini")
        return config['SERVER_DATA']['local_ip']
    return None