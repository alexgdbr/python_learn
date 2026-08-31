from datetime import datetime

def validar_data(data_srt) -> bool:
    try:
        data = datetime.strptime(data_srt, "%d/%m/%y")
        return True
    except ValueError:
        return False