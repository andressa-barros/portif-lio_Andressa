from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, create_engine, Identity

# Conexão com o banco de dados
engine = create_engine('sqlite:///banc_dados.db', echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()

# Tabelas
class Aluno(Base):
    __tablename__ = "aluno"
    id_aluno: Mapped[int] = mapped_column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome_aluno: Mapped[str] = mapped_column(String(30))
    idade: Mapped[int] = mapped_column(Integer)
    cpf: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"aluno={self.id_aluno!r},nome={self.nome_aluno!r},idade={self.idade!r}, cpf={self.cpf!r}"

class Instrutor(Base):
    __tablename__ = 'instrutor'
    id_instrutor: Mapped[int] = mapped_column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome_instrutor: Mapped[str] = mapped_column(String(50))
    cpf: Mapped[int] = mapped_column(Integer)
    cep: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"instrutor={self.id_instrutor!r}, nome_instrutor={self.nome_instrutor!r}, cpf={self.cpf!r}, cep={self.cep!r}"

class Treino(Base):
    __tablename__ = 'treino'
    id_treino: Mapped[int] = mapped_column(Integer, Identity(start=1, cycle=False), primary_key=True)
    situacao_saude: Mapped[str] = mapped_column(String(100))
    objetivo_aluno: Mapped[str] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"aluno={self.id_treino!r}, situacao_saude={self.situacao_saude!r}, objetivo_aluno={self.objetivo_aluno!r}"

class Pagamento(Base):
    __tablename__ = 'pagamento'
    id_pagamento: Mapped[int] = mapped_column(Integer, Identity(start=1, cycle=False), primary_key=True)
    tipo_pagamento: Mapped[str] = mapped_column(String(20))
    nome_aluno: Mapped[str] = mapped_column(String, ForeignKey("aluno.nome_aluno"))

    def __repr__(self) -> str:
        return f"nome_aluno={self.nome_aluno!r}, id_pagamento={self.id_pagamento!r}, tipo_pagamento={self.tipo_pagamento!r}"

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Aluno CRUD
def create_aluno(nome_aluno, idade, cpf):
    try:
        with Session(engine) as sessao:
            novo_aluno = Aluno(nome_aluno=nome_aluno, idade=idade, cpf=cpf)
            sessao.add(novo_aluno)
            sessao.commit()
            print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {str(e)}")

def read_aluno():
    try:
        with Session(engine) as sessao:
            alunos = sessao.query(Aluno).all()
            if alunos:
                for aluno in alunos:
                    print(f"ID: {aluno.id_aluno} | Nome: {aluno.nome_aluno} | Idade: {aluno.idade} | CPF: {aluno.cpf}")
            else:
                print("Nenhum aluno encontrado.")
    except Exception as e:
        print(f"Erro ao ler alunos: {str(e)}")

def update_aluno(id_aluno, nome_aluno, idade, cpf):
    try:
        with Session(engine) as sessao:
            aluno = sessao.query(Aluno).filter_by(id_aluno=id_aluno).first()
            if aluno:
                aluno.nome_aluno = nome_aluno
                aluno.idade = idade
                aluno.cpf = cpf
                sessao.commit()
                print(f"Aluno com ID {id_aluno} atualizado com sucesso.")
            else:
                print(f"Aluno com ID {id_aluno} não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar aluno: {str(e)}")

def delete_aluno(id_aluno):
    try:
        with Session(engine) as sessao:
            aluno = sessao.query(Aluno).filter_by(id_aluno=id_aluno).first()
            if aluno:
                sessao.delete(aluno)
                sessao.commit()
                print(f"Aluno com ID {id_aluno} deletado.")
            else:
                print(f"Aluno com ID {id_aluno} não encontrado.")
    except IntegrityError as e:
        print(f"Erro ao deletar aluno com ID {id_aluno}: {str(e)}")

# Treino CRUD
def create_treino(situacao_saude, objetivo_aluno):
    try:
        with Session(engine) as sessao:
            novo_treino = Treino(situacao_saude=situacao_saude, objetivo_aluno=objetivo_aluno)
            sessao.add(novo_treino)
            sessao.commit()
            print("Treino cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar treino: {str(e)}")

def read_treinos() -> List[Treino]:
    try:
        with Session(engine) as sessao:
            treinos = sessao.query(Treino).all()

            if treinos:
                for treino in treinos:
                    print(f"ID Treino: {treino.id_treino}")
                    print(f"Saúde: {treino.situacao_saude}")
                    print(f"Objetivo: {treino.objetivo_aluno}")
                    print("-" * 20)  # Separador visual entre os treinos
            else:
                print("Não foram encontrados treinos.")
    except Exception as e:
        print(f"Erro ao ler os treinos: {str(e)}")
        return None

def update_treino(situacao_saude, objetivo_aluno, id_treino):
    try:

        with Session(engine) as sessao:

            treino = sessao.query(Treino).filter_by(id_treino=id_treino).first()
            if treino:
                treino.situacao_saude = situacao_saude
                treino.objetivo_aluno = objetivo_aluno
                sessao.commit()
                print(f"Treino com ID {id_treino} atualizado.")
            else:
                print(f"Treino com ID {id_treino} não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar treino: {str(e)}")

def delete_treino(id_treino):
    try:
        with Session(engine) as sessao:
            treino = sessao.query(Treino).filter_by(id_treino=id_treino).first()
            if treino:
                sessao.delete(treino)
                sessao.commit()
                print(f"Treino com ID {id_treino} deletado.")
            else:
                print(f"Treino com ID {id_treino} não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar treino: {str(e)}")

# Instrutor CRUD
def create_instrutor(nome_instrutor, cpf, cep):
    try:
        with Session(engine) as sessao:
            novo_instrutor = Instrutor(nome_instrutor=nome_instrutor, cpf=cpf, cep=cep)
            sessao.add(novo_instrutor)
            sessao.commit()
            print("Instrutor cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar instrutor: {str(e)}")

def read_instrutor() -> List[Instrutor]:
    try:
        with Session(engine) as sessao:
            instrutores = sessao.query(Instrutor).all()

            if instrutores:
                for instrutor in instrutores:
                    print(f"ID: {instrutor.id_instrutor}")
                    print(f"Nome: {instrutor.nome_instrutor}")
                    print(f"CPF: {instrutor.cpf}")
                    print(f"CEP: {instrutor.cep}")
                    print("-" * 20)  # Separador visual entre os instrutores
            else:
                print("Não foram encontrados instrutores.")
    except Exception as e:
        print(f"Erro ao ler os instrutores: {str(e)}")
        return None

def update_instrutor(id_instrutor, nome_instrutor, cpf, cep):
    try:
        with Session(engine) as sessao:
            instrutor = sessao.query(Instrutor).filter_by(id_instrutor=id_instrutor).first()
            if instrutor:
                instrutor.nome_instrutor = nome_instrutor
                instrutor.cpf = cpf
                instrutor.cep = cep
                sessao.commit()
                print(f"Instrutor com ID {id_instrutor} atualizado.")
            else:
                print(f"Instrutor com ID {id_instrutor} não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar instrutor: {str(e)}")

def delete_instrutor(id_instrutor):
    try:
        with Session(engine) as sessao:
            instrutor = sessao.query(Instrutor).filter_by(id_instrutor=id_instrutor).first()
            if instrutor:
                sessao.delete(instrutor)
                sessao.commit()
                print(f"Instrutor com ID {id_instrutor} deletado.")
            else:
                print(f"Instrutor com ID {id_instrutor} não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar instrutor: {str(e)}")

# Pagamento CRUD
def create_pagamento(tipo_pagamento, nome_aluno):
    try:
        with Session(engine) as sessao:
            pagamento = Pagamento(tipo_pagamento=tipo_pagamento, nome_aluno=nome_aluno)
            sessao.add(pagamento)
            sessao.commit()
            print("Pagamento registrado com sucesso!")
    except Exception as e:
        print(f"Erro ao registrar pagamento: {str(e)}")

def update_pagamento(id_pagamento, tipo_pagamento, nome_aluno):
    try:
        with Session(engine) as sessao:
            pagamento = sessao.query(Pagamento).filter_by(id_pagamento=id_pagamento).first()
            if pagamento:
                pagamento.tipo_pagamento = tipo_pagamento
                pagamento.nome_aluno = nome_aluno
                sessao.commit()
                print(f"Pagamento com ID {id_pagamento} atualizado.")
            else:
                print(f"Pagamento com ID {id_pagamento} não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar pagamento: {str(e)}")

def read_pagamento() -> List[Pagamento]:
    try:
        with Session(engine) as sessao:
            pagamentos = sessao.query(Pagamento).all()

            if pagamentos:
                for pagamento in pagamentos:
                    print(f"ID Pagamento: {pagamento.id_pagamento}")
                    print(f"Tipo: {pagamento.tipo_pagamento}")
                    print(f"Nome do aluno: {pagamento.nome_aluno}")
                    print("-" * 20)  # Separador visual entre os pagamentos
            else:
                print("Não foram encontrados pagamentos.")
    except Exception as e:
        print(f"Erro ao ler os pagamentos: {str(e)}")
        return None

def delete_pagamento(id_pagamento):
    try:
        with Session(engine) as sessao:
            pagamento = sessao.query(Pagamento).filter_by(id_pagamento=id_pagamento).first()
            if pagamento:
                sessao.delete(pagamento)
                sessao.commit()
                print(f"Pagamento com ID {id_pagamento} deletado.")
            else:
                print(f"Pagamento com ID {id_pagamento} não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar pagamento: {str(e)}")
