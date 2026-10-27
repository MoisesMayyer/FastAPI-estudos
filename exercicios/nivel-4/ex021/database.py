import json

def salvar_json(dados):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_json():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []