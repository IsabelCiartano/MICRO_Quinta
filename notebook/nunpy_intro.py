import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #introduzione a numpy
    la libreria numpy serve per creare e manipolare **array**
    """)
    return


@app.cell
def _(np):
    array=np.array([1,2,3],dtype=np.int8)#un esempio di costruttore di array a cui passo una lista 
    array
    return (array,)


@app.cell
def _(array):
    array.dtype
    return


@app.cell
def _(array):
    array.size 
    return


if __name__ == "__main__":
    app.run()
