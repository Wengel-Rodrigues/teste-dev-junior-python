from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from xml.etree import ElementTree as ET
from database.models import NFE  
from database.db import SessionLocal

router = APIRouter()

# Dependência para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para upload do arquivo XML
@router.post("/upload/")
async def upload_nfe(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.filename.endswith('.xml'):
        content = await file.read()
        

        namespaces = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
        tree = ET.ElementTree(ET.fromstring(content))

        # Extração de dados da NFE
        cUF = tree.find(".//ns:cUF", namespaces=namespaces).text
        cNF = tree.find(".//ns:cNF", namespaces=namespaces).text
        natOp = tree.find(".//ns:natOp", namespaces=namespaces).text
        mod = tree.find(".//ns:mod", namespaces=namespaces).text
        serie = tree.find(".//ns:serie", namespaces=namespaces).text
        nNF = tree.find(".//ns:nNF", namespaces=namespaces).text
        emitente_CNPJ = tree.find(".//ns:emit/ns:CNPJ", namespaces=namespaces).text
        emitente_xNome = tree.find(".//ns:emit/ns:xNome", namespaces=namespaces).text
        emitente_xFant = tree.find(".//ns:emit/ns:xFant", namespaces=namespaces).text
        destinatario_CPF = tree.find(".//ns:dest/ns:CPF", namespaces=namespaces).text
        destinatario_xNome = tree.find(".//ns:dest/ns:xNome", namespaces=namespaces).text
        cProd = tree.find(".//ns:prod/ns:cProd", namespaces=namespaces).text
        xProd = tree.find(".//ns:prod/ns:xProd", namespaces=namespaces).text
        vProd = tree.find(".//ns:prod/ns:vProd", namespaces=namespaces).text
        vNF = tree.find(".//ns:ICMSTot/ns:vNF", namespaces=namespaces).text
        vICMS = tree.find(".//ns:ICMSTot/ns:vICMS", namespaces=namespaces).text

        
        new_nfe = NFE(
        cUF=cUF,
        cNF=cNF,
        natOp=natOp,
        mod=mod,
        serie=serie,
        nNF=nNF,
        emitente_CNPJ=emitente_CNPJ,
        emitente_xNome=emitente_xNome,
        emitente_xFant=emitente_xFant,
        destinatario_CPF=destinatario_CPF,
        destinatario_xNome=destinatario_xNome,
        cProd=cProd,
        xProd=xProd,
        vProd=vProd,
        vNF=vNF,
        vICMS=vICMS
    )

        db.add(new_nfe)
        db.commit()
        
        return {"message": "Arquivo processado com sucesso"}
    else:
        return HTTPException(status_code=400, detail="Tipo de arquivo inválido")

# Endpoint para listar todas as NFes
@router.get("/nfe/")
def read_nfes( db: Session = Depends(get_db)):
    nfes = db.query(NFE).all()
    if nfes is None:
        raise HTTPException(status_code=404, detail="NFEs not found")
    return nfes

# Endpoint para detalhes de uma NFE específica
@router.get("/nfe/{nfe_id}")
def read_nfe(nfe_id: int, db: Session = Depends(get_db)):
    nfe = db.query(NFE).filter(NFE.id == nfe_id).first()
    if nfe is None:
        raise HTTPException(status_code=404, detail="NFE não encontrada")
    return nfe
