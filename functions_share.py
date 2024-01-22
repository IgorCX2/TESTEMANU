from datetime import datetime
import json
import os

def obter_turno_atual(): #Para pegar o turno Atual
    hora_atual = datetime.now().time()
    turno_m_inicio = datetime.strptime("07:00", "%H:%M").time()
    turno_m_fim = datetime.strptime("16:48", "%H:%M").time()
    turno1_inicio = datetime.strptime("06:00", "%H:%M").time()
    turno2_inicio = datetime.strptime("14:36", "%H:%M").time()
    turno3_inicio = datetime.strptime("23:04", "%H:%M").time()

    if turno_m_inicio <= hora_atual < turno_m_fim:
        if turno1_inicio <= hora_atual < turno2_inicio:
            return "M1"
        else:
            return "M2"
    elif turno1_inicio <= hora_atual < turno2_inicio:
        return 1
    elif turno2_inicio <= hora_atual < turno3_inicio:
        return 2
    else:
        return 3
    
def carregar_usuarios():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'equipe', 'equipeDados.json')
    
    with open(caminho_arquivo, 'r') as arquivo:
        usuarios = json.load(arquivo)
    
    return usuarios

def carregar_maquina():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'maquina.json')
    with open(caminho_arquivo, 'r') as arquivo:
        maquina = json.load(arquivo)
    
    return maquina
    
def buscar_maquina_nome(maquina, dados):
    for maquinaListagem in dados:
        if maquinaListagem["maquina"] == maquina:
            return maquinaListagem
        
def buscar_pessoa_registro(registro):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["Registro"] == registro:
            return usuario

def mostrar_usuarios(cod): #Mostra Usuario x Cargo x Turno
    if cod is None:
       return 0
    turno_selecionado = obter_turno_atual()
    list_permit={
        "0405": "Mecanico",
        "0406": "Eletricista",
        "0407": "Eletricista",
        "0408": "Eletricista",
        "0403": "TODOS",
        "0706": "TODOS",
        "0502": "Mecanico",
        "0504": "Eletricista",
        "0505": "Eletricista",
        "0506": "Eletricista",
        "0404": "Mecanico",
        "0418": "Mecanico",
    }
    usuarios = carregar_usuarios()
    usuarios_turno = []
    for usuario in usuarios:
        if isinstance(turno_selecionado, int) and usuario["Cargo"] != list_permit[cod] and usuario["Cargo"] != "Adm":
            if str(usuario["Turno"]) == str(turno_selecionado):
                usuarios_turno.append(usuario)
        elif isinstance(turno_selecionado, str):
            if turno_selecionado[0] == 'M' and (usuario["Turno"] == "M" or str(usuario["Turno"]) == turno_selecionado[1:]) and usuario["Cargo"] != list_permit[cod] and usuario["Cargo"] != "Adm":
                usuarios_turno.append(usuario)
    return usuarios_turno
