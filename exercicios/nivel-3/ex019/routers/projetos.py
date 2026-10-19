from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Usuario, Projeto
from depends import verificar_token, get_db
from schemas import ProjetoCreate, ProjetoResponse, ProjetoUpdate

projetos_router = APIRouter(prefix="/projetos", tags=["projetos"])

@projetos_router.post("/", response_model=ProjetoResponse)
async def criar_projeto(dados: ProjetoCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):

    projeto_novo = Projeto(
        nome=dados.nome,
        descricao=dados.descricao,
        usuario_id=usuario.id,
    )

    db.add(projeto_novo)
    db.commit()
    db.refresh(projeto_novo)

    return projeto_novo


@projetos_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_projeto(id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projeto = db.query(Projeto).filter(Projeto.id == id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    db.delete(projeto)
    db.commit()

    return None


@projetos_router.put("/{id}", response_model=ProjetoResponse)
async def atualizar_projeto(id: int, dados: ProjetoUpdate, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projeto = db.query(Projeto).filter(Projeto.id == id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    if dados.nome is not None:
        projeto.nome = dados.nome

    if dados.descricao is not None:
        projeto.descricao = dados.descricao

    db.commit()
    db.refresh(projeto)

    return projeto


@projetos_router.get("/", response_model=list[ProjetoResponse])
async def listar_projetos(db:Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projetos = db.query(Projeto).filter(Projeto.usuario_id == usuario.id).all()

    return projetos


@projetos_router.get("/{id}", response_model=ProjetoResponse)
async def pegar_projeto(id:int, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projeto = db.query(Projeto).filter(Projeto.id == id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    return projeto
