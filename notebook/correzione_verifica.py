import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #correzione verfica
    """)
    return


@app.class_definition
class Terminale:
    def __init__(self):
        self.comandi={}
        self.storico=[]
    def registra(self,nome,funzione):
        self.comandi[nome.lower()]=funzione
    def esegui(self,riga):
        parole=riga.strip().split(" ")
        comando=parole[0].lower()
        print(comando)
        argomento= " ".join(parole[1:])
        

        if comando not in self.comandi:
            result="ERRORE comando sconosciuto"
        else:
             result=self.comandi[comando](argomento)
        self.storico.append((comando,result))
        return result
    def conta_errori(self):
        nErrori=0
        for _,result in self.storico:
            if "ERRORE" in result:
                nErrori+=1
        return nErrori


@app.cell
def _():
    def inverti(testo):
        parole=testo.strip().split(" ")
        return " ".join(parole[::-1])
    def conta(testo):
        return str(len(testo.strip().split(" ")))


    return conta, inverti


@app.cell
def _(conta, inverti):
    t=Terminale()
    t.registra("inverti",inverti)
    t.registra("conta",conta)
    print(t.comandi)
    print(t.esegui("inverti il gatto nero"))
    print(t.esegui("salta "))
    print(t.conta_errori())
    return


if __name__ == "__main__":
    app.run()
