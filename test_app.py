from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_nfe():
    # Arquivo XML falso para o teste
    fake_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
    <NFe xmlns="http://www.portalfiscal.inf.br/nfe">
        <infNFe Id="NFe35110212345678901234550010000000011000000011">
            <ide>
                <cUF>35</cUF>
                <cNF>00000001</cNF>
                <natOp>VENDA DE PRODUTO</natOp>
                <mod>55</mod>
                <serie>1</serie>
                <nNF>1</nNF>
                <dhEmi>2023-08-28T14:30:00-03:00</dhEmi>
                <tpNF>1</tpNF>
                <idDest>1</idDest>
                <cMunFG>3550308</cMunFG>
                <tpImp>1</tpImp>
                <tpEmis>1</tpEmis>
                <cDV>1</cDV>
                <tpAmb>1</tpAmb>
                <finNFe>1</finNFe>
                <indFinal>1</indFinal>
                <indPres>1</indPres>
                <procEmi>0</procEmi>
                <verProc>4.00</verProc>
            </ide>
            <emit>
                <CNPJ>12345678901234</CNPJ>
                <xNome>EMPRESA FICTICIA LTDA</xNome>
                <xFant>EMPRESA FICTICIA</xFant>
                <enderEmit>
                    <xLgr>RUA FICTICIA</xLgr>
                    <nro>123</nro>
                    <xBairro>BAIRRO FICTICIO</xBairro>
                    <cMun>3550308</cMun>
                    <xMun>SAO PAULO</xMun>
                    <UF>SP</UF>
                    <CEP>01001000</CEP>
                </enderEmit>
            </emit>
            <dest>
                <CPF>11122233344</CPF>
                <xNome>JOAO FICTICIO</xNome>
                <enderDest>
                    <xLgr>RUA FICTICIA DO CLIENTE</xLgr>
                    <nro>456</nro>
                    <xBairro>BAIRRO CLIENTE</xBairro>
                    <cMun>3550308</cMun>
                    <xMun>SAO PAULO</xMun>
                    <UF>SP</UF>
                    <CEP>02002000</CEP>
                </enderDest>
            </dest>
            <det nItem="1">
                <prod>
                    <cProd>001</cProd>
                    <xProd>PRODUTO FICTICIO</xProd>
                    <NCM>99999999</NCM>
                    <CFOP>5102</CFOP>
                    <uCom>UN</uCom>
                    <qCom>1.0000</qCom>
                    <vUnCom>100.00</vUnCom>
                    <vProd>1000.00</vProd>
                    <indTot>1</indTot>
                </prod>
            </det>
            <total>
                <ICMSTot>
                    <vBC>100.00</vBC>
                    <vICMS>38.00</vICMS>
                    <vICMSDeson>0.00</vICMSDeson>
                    <vBCST>0.00</vBCST>
                    <vST>0.00</vST>
                    <vProd>100.00</vProd>
                    <vFrete>0.00</vFrete>
                    <vSeg>0.00</vSeg>
                    <vDesc>0.00</vDesc>
                    <vII>0.00</vII>
                    <vIPI>0.00</vIPI>
                    <vPIS>0.65</vPIS>
                    <vCOFINS>3.00</vCOFINS>
                    <vOutro>0.00</vOutro>
                    <vNF>1000.00</vNF>
                </ICMSTot>
            </total>
        </infNFe>
    </NFe>
</nfeProc>
'''
    
    files = {"file": ("test.xml", fake_xml, "application/xml")}
    
    response = client.post("/upload/", files=files)
    
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Arquivo processado com sucesso"


def test_upload_nfe2():
    with open("sample.xml", "r") as f:
        file_content = f.read()
    
    files = {"file": ("sample.xml", file_content, "application/xml")}
    
    response = client.post("/upload/", files=files)
    
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Arquivo processado com sucesso"

def test_read_all_nfes():
    response = client.get("/nfe/")
    assert response.status_code == 200