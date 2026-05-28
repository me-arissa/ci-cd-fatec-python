# main.py
import sqlite3


def saudacao(nome: str) -> str:
    """Retorna uma saudação segura."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    """Calcula a média de uma lista de notas."""
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)


def buscar_usuario_seguro(user_id):
    """Busca um usuário de forma segura usando queries parametrizadas."""
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # Usando a variável cursor de forma correta e segura para o flake8 não reclamar
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado


if __name__ == "__main__":
    print(saudacao("Aluno FATEC"))
    print(f'Média: {calcular_media([8.5, 9.0, 7.5])}')
    # Exemplo de uso da função para garantir que o código rode perfeitamente
    print(f'Usuário: {buscar_usuario_seguro(1)}')
    