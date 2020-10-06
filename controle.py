from PyQt5 import uic, QtWidgets
import mysql.connector as mysql

bd = mysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='form_clientes'
)


def funcaoPrincipal():
    nome = cadastrar.lineEdit.text()
    cpf = cadastrar.lineEdit_2.text()
    cep = cadastrar.lineEdit_3.text()
    endereco = cadastrar.lineEdit_4.text()
    numero = cadastrar.lineEdit_5.text()
    complemento = cadastrar.lineEdit_6.text()
    bairro = cadastrar.lineEdit_7.text()
    cidade = cadastrar.lineEdit_13.text()
    estado = cadastrar.lineEdit_14.text()
    email = cadastrar.lineEdit_8.text()
    dataNasc = cadastrar.lineEdit_9.text()
    idade = cadastrar.lineEdit_10.text()
    genero = ''
    if cadastrar.radioButton.isChecked():
        print('Genero: Masculino')
        genero = 'Masculino'
    elif cadastrar.radioButton_2.isChecked():
        print('Genero: Feminino')
        genero = 'Feminino'
    telefone = cadastrar.lineEdit_11.text()
    celular = cadastrar.lineEdit_12.text()
    convenio = cadastrar.lineEdit_15.text()


    print(f'nome-> {nome} \ncpf-> {cpf}\ncep-> {cep}\nendereço-> {endereco}\nnumero-> {numero}')
    print(f'complemento-> {complemento}\nbairro-> {bairro}\ncidade-> {cidade}\nestado-> {estado}\nemail-> {email}')
    print(f'Data de Nascimento-> {dataNasc}\nidade-> {idade}\ntelefone-> {telefone}\ncelular-> {celular}')
    print(f'convenio-> {convenio}')


    cursor = bd.cursor()
    comandoSQL = '''
    INSERT INTO pacientes (nome, cpf, cep, endereco, numero, complemento, bairro, cidade, estado, email, 
    dataNasc, idade, genero, telefone, celular, convenio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    dados = (str(nome), str(cpf), str(cep), str(endereco), str(numero), str(complemento), str(bairro), str(cidade), str(estado),
             str(email), str(dataNasc), str(idade), genero, str(telefone), str(celular), str(convenio))
    cursor.execute(comandoSQL, dados)
    bd.commit()

    cadastrar.lineEdit.setText('')
    cadastrar.lineEdit_2.setText('')
    cadastrar.lineEdit_3.setText('')
    cadastrar.lineEdit_4.setText('')
    cadastrar.lineEdit_5.setText('')
    cadastrar.lineEdit_6.setText('')
    cadastrar.lineEdit_7.setText('')
    cadastrar.lineEdit_13.setText('')
    cadastrar.lineEdit_14.setText('')
    cadastrar.lineEdit_8.setText('')
    cadastrar.lineEdit_9.setText('')
    cadastrar.lineEdit_10.setText('')
    cadastrar.lineEdit_11.setText('')
    cadastrar.lineEdit_12.setText('')
    cadastrar.lineEdit_15.setText('')

def listar_clientes():
    clientes.show()

    cursor = bd.cursor()
    comandoSQL = 'SELECT *FROM PACIENTES'
    cursor.execute(comandoSQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos[0][0])

    clientes.tableWidget.setRowCount(len(dados_lidos))
    clientes.tableWidget.setColumnCount(17)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 17):
            clientes.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



app=QtWidgets.QApplication([])
cadastrar=uic.loadUi('cadastro.ui')
clientes=uic.loadUi('clientes.ui')
cadastrar.pushButton.clicked.connect(funcaoPrincipal)
cadastrar.pushButton_2.clicked.connect(listar_clientes)
cadastrar.show()
app.exec()