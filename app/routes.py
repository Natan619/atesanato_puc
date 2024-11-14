from flask import render_template, request, redirect, url_for
from . import db
from .models import Aluno, Artesanato, Gasto
from flask import current_app as app
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            faturamento = float(request.form['faturamento'])
            forma_pagamento = request.form['forma_pagamento']
            data = datetime.strptime(request.form['data'], '%Y-%m-%d')
            novo_aluno = Aluno(nome=nome, faturamento=faturamento, forma_pagamento=forma_pagamento, data=data)
            db.session.add(novo_aluno)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Erro ao adicionar aluno: {e}")
            return str(e), 500
        return redirect(url_for('index'))
    return render_template('form.html', tipo='Aluno')

@app.route('/artesanato', methods=['GET', 'POST'])
def artesanato():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            faturamento = float(request.form['faturamento'])
            forma_pagamento = request.form['forma_pagamento']
            data = datetime.strptime(request.form['data'], '%Y-%m-%d')
            novo_artesanato = Artesanato(nome=nome, faturamento=faturamento, forma_pagamento=forma_pagamento, data=data)
            db.session.add(novo_artesanato)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Erro ao adicionar artesanato: {e}")
            return str(e), 500
        return redirect(url_for('index'))
    return render_template('form.html', tipo='Artesanato')

@app.route('/gasto', methods=['GET', 'POST'])
def gasto():
    if request.method == 'POST':
        try:
            nome_do_gasto = request.form['nome_do_gasto']
            valor = float(request.form['valor'])
            forma_pagamento = request.form['forma_pagamento']
            data = datetime.strptime(request.form['data'], '%Y-%m-%d')
            novo_gasto = Gasto(nome_do_gasto=nome_do_gasto, valor=valor, forma_pagamento=forma_pagamento, data=data)
            db.session.add(novo_gasto)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Erro ao adicionar gasto: {e}")
            return str(e), 500
        return redirect(url_for('index'))
    return render_template('form.html', tipo='Gasto')