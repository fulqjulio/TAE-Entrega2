from ast import Try
from re import S
from django.shortcuts import redirect, render
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


def rredirect(request):
    return redirect('/index/inicio/-/')


def index(request, current, predict):
    output = '-'
    if predict != '-':
        try:
            # REMOTO
            direccion='proyect/bd/modelo.csv'
            # LOCAL
            # direccion = 'proyect/proyect/bd/modelo.csv'
            salida = pd.read_csv(direccion, index_col=0)
            drop_columns_list = salida.columns.values[22:-2]
            salida.drop(columns=drop_columns_list, inplace=True)
            output = dict(salida.loc[int(predict)])
        except:
            output = '-'

    context = {
        "current": current,
        "predict": predict,
        "output": output,
    }

    return render(request, 'Index.html', context)

# Vista para la predicción


def prediction(request):
    prediction = "-"
    if request.GET:
        prediction = request.GET.get('id', '-')

    return redirect('../index/prediccion/'+str(prediction)+'/')
