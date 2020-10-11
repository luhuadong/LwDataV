#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/11 16:04
# @Author : Rudy
# @Site :
# @Describe:

from flask import Flask, render_template
from data import SourceData
from data_com import ComData
from data_air import AirData

app = Flask(__name__)


@app.route('/')
def index():
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/com')
def com():
    data = ComData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/air')
def air():
    data = AirData()
    return render_template('index.html', form=data, title=data.title)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
