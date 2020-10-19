from config import *
from models import Paciente

@app.route("/")
def mostrar_home():
    return "Olá"


@app.route("/listar_pacientes")

def listar_pacientes():
    pacientes = db.session.query(Paciente).all()
    lista_pac = []
    for p in pacientes:
        lista_pac.append(p.json())
    print(lista_pac)
    return jsonify(lista_pac)

@app.route("/incluir_paciente", methods=['post'])
def adicionar_paciente():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        novo_paci = Paciente(**dados)
        db.session.add(novo_paci)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/remover_paciente/<int:paciente_id>", methods=['DELETE'])
def remover_paciente(paciente_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Paciente.query.filter(Paciente.id == paciente_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

if __name__ == "__main__":
    app.run(debug=True)