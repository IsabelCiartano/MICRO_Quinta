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
    #questo è il primo notebook

    in questo file scriveremo i primi codici python dentro un notebook
    """)
    return


@app.cell
def _():
    a,b = 1,2
    print (f"ciao mondo, a+b fa {a+b}")
    return


@app.function
def neurone(x1,x2,soglia=1):
    somma=x1+x2
    if somma>=soglia:
        return 1
    else:
        return 0


@app.cell
def _(mo):
    x1_slider=mo.ui.slider(start=0.,stop=2.,step=0.1,value=1.,label="x1") #ui user interface 
    x2_slider=mo.ui.slider(start=0.,stop=2.,step=0.1,value=1.,label="x2") 

    lista_slider=[x1_slider,x2_slider]
    mo.hstack(lista_slider)
    return x1_slider, x2_slider


@app.cell
def _(x1_slider, x2_slider):
    f"l'output del neurone di McCulloch e Pitts e: {neurone(x1_slider.value,x2_slider.value)}"
    return


if __name__ == "__main__":
    app.run()
