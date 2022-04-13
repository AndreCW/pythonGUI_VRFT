# Atualizar código para interface gráfica: pyuic6 -o output.py -x input.ui
# Criar executável: auto-py-to-exe

#########
import os
from PyQt6 import QtCore, QtGui, QtWidgets
#########
from PyQt6.QtWidgets import QFileDialog, QMainWindow
import pandas as pd
import numpy as np  # important package for scientific computing
from scipy import signal  # signal processing library
import matplotlib.pyplot as plt  # library to plot graphics
import vrft  # vrft package
from  controlsystems import types
import math

import guiPrincipal

class MyWindow(guiPrincipal.Ui_MainWindow):
    def mySetupUi(self, MainWindow):
        ########################################################################
        ## Cria grupo de botões 1 - classe do conversor
        self.gConversor = QtWidgets.QButtonGroup(MainWindow)
        self.gConversor.addButton(self.bBuck)
        self.gConversor.addButton(self.bBoost)
        self.gConversor.addButton(self.bSepic)
        self.gConversor.addButton(self.bFlyback)
        self.gConversor.setId(self.bBuck, 1)
        self.gConversor.setId(self.bBoost, 2)
        self.gConversor.setId(self.bSepic, 3)
        self.gConversor.setId(self.bFlyback, 4)
        
        ## Cria grupo de botões 2 - Modelo de referencia Td
        self.gTd = QtWidgets.QButtonGroup(MainWindow)
        self.gTd.addButton(self.bTdPadrao)
        self.gTd.addButton(self.bTdCustom)
        self.gTd.setId(self.bTdPadrao, 5)
        self.gTd.setId(self.bTdCustom, 6)
        
        ## Cria grupo de botões 3 - classe do controlador
        self.gControlador = QtWidgets.QButtonGroup(MainWindow)
        self.gControlador.addButton(self.CPropor)
        self.gControlador.addButton(self.CPi)
        self.gControlador.addButton(self.CPd)
        self.gControlador.addButton(self.CPid)
        self.gControlador.addButton(self.customC)
        self.gControlador.setId(self.CPropor, 7)
        self.gControlador.setId(self.CPi, 8)
        self.gControlador.setId(self.CPd, 9)
        self.gControlador.setId(self.CPid, 10)
        self.gControlador.setId(self.customC, 11)
    
        ## Cria grupo de botões 4 - Filtro L(z)
        self.gFiltro = QtWidgets.QButtonGroup(MainWindow)
        self.gFiltro.addButton(self.semFiltro)
        self.gFiltro.addButton(self.filtroPadrao)
        self.gFiltro.addButton(self.filtroCustom)
        self.gFiltro.setId(self.semFiltro, 12)
        self.gFiltro.setId(self.filtroPadrao, 13)
        self.gFiltro.setId(self.filtroCustom, 14)
        
        ## Cria grupo de botões 5 - Classe controlador pré projeto
        self.gPre = QtWidgets.QButtonGroup(MainWindow)
        self.gPre.addButton(self.bBuck)
        self.gPre.addButton(self.bBoost)
        self.gPre.addButton(self.bFlyback)
        self.gPre.addButton(self.bSepic)
        self.gPre.setId(self.bBuck, 15)
        self.gPre.setId(self.bBoost, 16)
        self.gPre.setId(self.bFlyback, 17)
        self.gPre.setId(self.bSepic, 18)
        
        ## Chamada das funções para quando algum botao for pressionado
        self.gTd.buttonClicked.connect(self.TdPressed)
        self.gControlador.buttonClicked.connect(self.CPressed)
        self.gFiltro.buttonClicked.connect(self.filterPressed)
        
        self.bPontoOp.clicked.connect(self.pontoIdealPressed)
        self.bVRFT.clicked.connect(self.VRFTPressed)
        self.grafTd.clicked.connect(self.graphTzPressed)
        self.bJVR.clicked.connect(self.JVRPressed)
        self.bSensi.clicked.connect(self.sensiPressed)
        
        self.bEnsaio.clicked.connect(self.ensaioPressed)
        self.bIV.clicked.connect(self.ivPressed)
        self.bEnsaioMF.clicked.connect(self.ensaioMFPressed)
        
    ################################################################
    ## Funções de botoes que foram pressionados
    ## Deixa os campos de escrita do modelo de referencia como read only conforme o botao que foi selecionado
    def TdPressed(self):
        pressed = self.gTd.checkedId()
        if pressed == 5:
            self.textAcom.setReadOnly(False)
            self.textSpeed.setReadOnly(False)
            self.TdNum.setReadOnly(True)
            self.TdDen.setReadOnly(True)
        elif pressed == 6:
            self.textAcom.setReadOnly(True)
            self.textSpeed.setReadOnly(True)
            self.TdNum.setReadOnly(False)
            self.TdDen.setReadOnly(False)
    
    ## Deixa o campo de escrita do controlador como read only conforme o botao que foi selecionado
    def CPressed(self):
        pressed = self.gControlador.checkedId()
        if pressed == 11:
            self.customCNum.setReadOnly(False)
            self.customCDen.setReadOnly(False)
        else:
            self.customCNum.setReadOnly(True)
            self.customCDen.setReadOnly(True)
    
    ## Deixa o campo de escrita do filtro como read only conforme o botao que foi selecionado
    def filterPressed(self):
        pressed = self.gFiltro.checkedId()
        if pressed == 14:
            self.fTdNum.setReadOnly(False)
            self.fTdDen.setReadOnly(False)
        else:
            self.fTdNum.setReadOnly(True)
            self.fTdDen.setReadOnly(True)
    
    ## 
    def textCapture(self, chave):
        if chave == 1:
            valor = self.textAcom.text()
        elif chave == 2: 
            valor = self.textSpeed.text()
        elif chave == 3:
            valor = self.textFreq.text()
        elif chave == 4: 
            valor = self.TdNum.text()
        elif chave == 5: 
            valor = self.TdDen.text()
        elif chave == 6: 
            valor = self.fTdNum.text()
        elif chave == 7: 
            valor = self.fTdDen.text()
        elif chave == 8:
            valor = self.input_duty.text()
        elif chave == 9:
            valor = self.input_Vo.text()
            
        valor = valor.replace(" ", "")
        valor = valor.replace("[", "")
        valor = valor.replace("]", "")
        lista = valor.split(",")
        floats = [float(y) for y in lista]
        
        return floats
    
    ## 
    def customControllerSetter(self, chave):
        if chave == 0:
            valor = self.customCNum.text()
        else:
            valor = self.customCDen.text()
            
        i, j = 0, 0
        for x in valor:
            if (x == '['):
                i += 1
            elif (x == ']'):
                j += 1
        if (i != j):
            # TODO: Error flag
            texto = "Modelo de controaldor invalido"
            self.controllerOutput.appendPlainText(texto)
        else:
            valores = []
            aux = []
            contador = 0
            abre = 0
            fecha = 0
            while(contador < len(valor)):
                if (valor[contador] == '['):
                    abre = 1
                
                if (abre == 1):
                    aux.append(valor[contador])
                    
                if (valor[contador] == ']' and abre == 1):
                    abre = 0
                    fecha += 1
                    str1 = "".join(aux)
                    valores.append(str1)
                    aux = []
                
                contador += 1
            
            for x in range(0, len(valores)):
                valores[x] = valores[x].replace(" ", "")
                valores[x] = valores[x].replace("[", "")
                valores[x] = valores[x].replace("]", "")
                valores[x] = valores[x].split(",")
                
            for m in range(len(valores)):
                for n in range(len(valores[m])):
                    valores[m][n] = float(valores[m][n])
                    
            return valores, fecha
        
    # TODO:    
    ## Botao para gerar o ponto ideal para coleta de dados    
    def pontoIdealPressed(self):
        duty = self.textCapture(8)
        v0 = self.textCapture(9)
    
    ## Botao para aplicar o metodo VRFT
    def VRFTPressed(self):
        modelFunc = self.gTd.checkedId()
        
        # TODO: Zero de fase nao minima    
        # zeroFNM = check ZFNM button
        
        if modelFunc == 5:
            tso = self.textCapture(1)
            speed = self.textCapture(2)
            freq = self.textCapture(3)
            
            p1 = math.exp(-(4 / freq[0]) / (tso[0] * math.pow(10, -3) * (1 - 0.01 * speed[0])))
            p2 = 10 * p1
            
            k0 = 1 * (1 - p1) * (1 - p2)
            
            tdNum = [k0]
            tdDen = [1, -2*p1*p2, p1*p2]
            
        elif modelFunc == 6:
            tdNum = self.textCapture(4)
            tdDen = self.textCapture(5)
            
        elif modelFunc == -1:
            # TODO: Error flag
            texto = "Modelo de referência invalido"
            self.controllerOutput.appendPlainText(texto)
        
        objectiveFunction = signal.TransferFunction(tdNum, tdDen, dt=1)
        
        # Conforme selecao do usuario, seta o tipo de controlador
        controlClass = self.gControlador.checkedId()
        
        if controlClass == 7:                                                               # Proporcional
            controllerModel = [[signal.TransferFunction([1], [1], dt=1)]]                       # Kp
            k = "p"
            
        elif controlClass == 8:                                                             # Proporcional Integral
            controllerModel = [[signal.TransferFunction([1], [1], dt=1)],                       # Kp
                               [signal.TransferFunction([1, 0], [1, -1], dt=1)],]               # Ki
            k = "pi"
            
        elif controlClass == 9:                                                             # Proporcional Derivativo
            controllerModel = [[signal.TransferFunction([1], [1], dt=1)],                       # Kp
                               [signal.TransferFunction([1, -1], [1, 0], dt=1)],]               # Kd
            k = "pd"
            
        elif controlClass == 10:                                                            # Proporcional Integral Derivativo
            controllerModel = [[signal.TransferFunction([1], [1], dt=1)],                       # Kp
                               [signal.TransferFunction([1, 0], [1, -1], dt=1)],                # Ki
                               [signal.TransferFunction([1, -1], [1, 0], dt=1)],]               # Kd
            k = "pid"
            
        elif controlClass == 11:                                                            # Custom
            controllerNumTemp, numNum = self.customControllerSetter(0)
            controllerDenTemp, numDen = self.customControllerSetter(1)
            # TODO: flag que impede sequencia se o len de cada for diferente
            
            tempNum = len(controllerNumTemp)
            tempDen = len(controllerDenTemp)
            temp = tempNum + tempDen
            
            contador, i, j = 0, 0, 0
            controllerTemp = []
            
            while (contador < temp):
                if (contador % 2) == 0:
                    controllerTemp.append(controllerDenTemp[i])
                    i += 1
                else:
                    controllerTemp.append(controllerNumTemp[j])
                    j += 1
                contador += 1

            controllerModel = []
            contador = 0
            
            while (contador < len(controllerTemp)):
                controllerModel.append([signal.TransferFunction(controllerTemp[contador], controllerTemp[contador + 1], dt=1)])
                contador += 2
                
            k = "custom"
            
        elif controlClass == -1:
            # TODO: Error flag
            texto = "Modelo do controlador invalido"
            self.controllerOutput.appendPlainText(texto)
        
        # Conforme selecao do usuario, seta o tipo de filtro
        filterType = self.gFiltro.checkedId()
        
        if filterType == 12:    # Sem Filtro
            filterNum, filterDen = [1]
            
        elif filterType == 13:  # Filtro Padrão
            um = types.TransferFunction([1], [1])
            tTemp = types.TransferFunction(tdNum, tdDen)
            tDesejada = tTemp * (um - tTemp)
            
            filterNum, filterDen = tDesejada.getNumDen()
            filterNum = list(filterNum)
            filterDen = list(filterDen)
            
        elif filterType == 14:  # Filtro Custom
            filterNum = self.textCapture(6)
            filterDen = self.textCapture(7)
            
        elif filterType == -1:
            # TODO: Error flag
            texto = "Modelo de filtro invalido"
            self.controllerOutput.appendPlainText(texto)
            
        filterL = signal.TransferFunction(filterNum, filterDen, dt=1)
        
        num = self.dfEnsaio.shape[0]
        
        dfEnsaioCopia = self.dfEnsaio.copy()
        
        entradaTemp = dfEnsaioCopia.pop(dfEnsaioCopia.columns[0]).to_numpy()
        saidaTemp = dfEnsaioCopia.pop(dfEnsaioCopia.columns[0]).to_numpy()
        
        entradaEnsaio = np.ones((num, 1))
        saidaEnsaio = np.ones((num, 1))
        
        for x in range(0, num):
            entradaEnsaio[x] = entradaTemp[x]
            saidaEnsaio[x] = saidaTemp[x]
        
        iv = self.ivText.text()
        if iv == "": # Nao tem ensaio com variavel instrumentavel
            saidaIV = saidaEnsaio
        else:
            numIV = self.dfIV.shape[0]
            dfIVCopia = self.dfIV.copy()
            saidaIVTemp = dfIVCopia.pop(dfIVCopia.columns[1]).to_numpy()
            saidaIV = np.ones((numIV, 1))
            for x in range(0, numIV):
                saidaIV[x] = saidaIVTemp[x]
        
        '''
        resultado = vrft.design(dfEnsaio.dados de entrada, dfEnsaio.dados de saida, dfIV.dados de saida com variavel instrumentavel, funcao de transferencia objetivo, modelo de controle, filtro)
        '''
        
        resultado = vrft.design(entradaEnsaio, saidaEnsaio, saidaIV, objectiveFunction, controllerModel, filterL)
        
        if (k == "p"):
            cont = [resultado[0].item()]
            texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\tKp = " + str(cont[0])
        elif (k == "pi"):
            cont = [resultado[0].item(), resultado[1].item()]
            texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\tKp = " + str(cont[0]) + "\n\tKi = " + str(cont[1])
        elif (k == "pd"):
            cont = [resultado[0].item(), resultado[1].item()]
            texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\tKp = " + str(cont[0]) + "\n\tKd = " + str(cont[1])
        elif (k =="pid"):
            cont = [resultado[0].item(), resultado[1].item(), resultado[2].item()]
            texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\tKp = " + str(cont[0]) + "\n\tKi = " + str(cont[1]) + "\n\tKd = " + str(cont[1])
        elif (k == "custom"):
            cont = [resultado[x].item() for x in range(numNum)]
            texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\t"
            textoaux = ""
            for y in range(numNum):
                textoaux = textoaux + "K" + str(y + 1) + " = " + str(cont[y]) + "\n\t"
            texto = texto + textoaux
            
        self.controllerOutput.appendPlainText(texto)
        
        objectiveFunction = 0
        controllerModel = 0
        filterL = 0
        resultado = 0

    # TODO:
    ## Botao para gerar o grafico de T(z)
    def graphTzPressed(self):
        pass
    
    # TODO:
    ## Botao para gerar o custo JVR
    def JVRPressed(self):
        pass

    # TODO:
    ## Botao para calcular a sensibilidade
    def sensiPressed(self):
        pass
    
    ######
    ## Trabalho com a caixa de texto output:
    # setPlainText - apaga todo o texto presente e escreve o texto passado como argumento
    # insertPlainText - insere o texto passado como argumento no inicio da caixa de texto sem apagar o texto antigo, nao adiciona nova linha
    # appendPlainText - insere o texto passado como argumento apos o texto presente sem apagar o texto antigo, adiciona uma nova linha automatica
    
    ## Botao para buscar planilha com os dados do ensaio da planta
    def getFile(self):
        file_filter = 'Data File (*.xlsx *.csv);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.xlsx *.csv)')
        if response[0] == '':
            return False
        elif  response[0][-1] == 'v':
            df = pd.read_csv(response[0])
        else:
            df = pd.read_excel(response[0])
        return df, response[0]
            
    def ensaioPressed(self):
        self.dfEnsaio, address = self.getFile()
        if address != False:
            self.ensaioText.setText(address)
            texto = "Dados de ensaio carregados. Numero de pares entrada-saida amostrados: " + str(self.dfEnsaio.shape[0])
            self.controllerOutput.setPlainText(texto)
        # TODO: if address == False
    
    ## Botao para buscar planilha com os dadosdo ensaio da variavel instrumentavel da planta
    def ivPressed(self):
        self.dfIV, address = self.getFile()
        if address != False:
            self.ivText.setText(address)
            texto = "Dados da variavel instrumentavel carregados. Numero de pares entrada-saida amostrados: " + str(self.dfIV.shape[0])
            self.controllerOutput.appendPlainText(texto)
    
    ## Botao para buscar planilha com os dados do ensaio em malha fechada da planta
    def ensaioMFPressed(self):
        self.dfEnsaioMF, address = self.getFile()
        if address != False:
            self.ensaioMFText.setText(address)
            texto = "Dados de ensaio em malha fechada carregados. Numero de pares entrada-saida amostrados: " + str(self.dfEnsaioMF.shape[0])
            self.MFOutput.appendPlainText(texto)
    
    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow()
    ui.setupUi(MainWindow)
    ui.mySetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())