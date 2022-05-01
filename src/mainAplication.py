# Atualizar código para interface gráfica: pyuic6 -o output.py -x input.ui
# Criar executável: auto-py-to-exe

import math
#########
import os

import control.matlab as control
import matplotlib.pyplot as plt  # library to plot graphics
import numpy as np  # important package for scientific computing
import pandas as pd
import vrft  # vrft package
from PyQt6 import QtWidgets
#########
from PyQt6.QtWidgets import QFileDialog
from scipy import signal  # signal processing library

from guiPrincipal import Ui_MainWindow


class MyWindow(Ui_MainWindow):

    def mySetupUi(self, MainWindow):
        self.flag = False
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

    ## Faz a leitura de cada campo de entrada de texto presente na interface
    def textCapture(self, chave):
        valor = ""
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

        if valor != "":
            valor = valor.replace(" ", "")
            valor = valor.replace("[", "")
            valor = valor.replace("]", "")
            lista = valor.split(",")
            floats = [float(y) for y in lista]

            return floats

    ## Faz a leitura especificamente dos campos de texto do controlador
    def customControllerSetter(self, chave):
        if chave == 0:
            valor = self.customCNum.text()
        else:
            valor = self.customCDen.text()

        i, j = 0, 0
        for x in valor:
            if x == '[':
                i += 1
            elif x == ']':
                j += 1
        if i != j:
            # TODO: Error flag
            texto = "Modelo de controlador invalido"
            self.controllerOutput.appendPlainText(texto)
        else:
            valores = []
            aux = []
            contador = 0
            abre = 0
            fecha = 0
            while contador < len(valor):
                if valor[contador] == '[':
                    abre = 1

                if abre == 1:
                    aux.append(valor[contador])

                if valor[contador] == ']' and abre == 1:
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

    ## Botao para gerar o ponto ideal para coleta de dados    
    def pontoIdealPressed(self):
        duty = self.textCapture(8)
        v0 = self.textCapture(9)

        controllerType = self.gPre.checkedId()

        # Não faz nada enquanto todas as opções não forem selecionadas
        if controllerType == -1 or duty is None or v0 is None:
            pass
        elif controllerType == 15:
            ideal = v0[0] / duty[0]
        elif controllerType == 16:
            ideal = v0[0] / (1 - duty[0])
        elif controllerType == 17:
            ideal = v0[0] / (duty[0] * (1 - duty[0]))
        elif controllerType == 18:
            ideal = v0[0] / (duty[0] * (1 - duty[0]))

        if controllerType != -1 and duty is not None and v0 is not None:
            ideal = 1 / ideal

            texto = "Ganho estático máximo: " + str(ideal) + " [V<sup>-1</sup>]"

            self.preOutput.append(texto)

    def getRef(self):
        if self.ensaioText.text() != '':

            modelFunc = self.gTd.checkedId()

            if modelFunc == 5:
                tso = self.textCapture(1)
                speed = self.textCapture(2)
                freq = self.textCapture(3)

                p1 = math.exp(-(4 / freq[0]) / (tso[0] * 10 ** -3 * (1 - 0.01 * speed[0])))

                self.modelNum = [1 - p1]
                self.modelDen = [1, -p1]

            elif modelFunc == 6:
                self.modelNum = self.textCapture(4)
                self.modelDen = self.textCapture(5)

            elif modelFunc == -1:
                # TODO: Error flag
                texto = "Modelo de referência invalido"
                self.controllerOutput.appendPlainText(texto)

            objectiveFunction = signal.TransferFunction(self.modelNum, self.modelDen, dt=1)

            return objectiveFunction

    def getCont(self):
        # Conforme selecao do usuario, seta o tipo de controlador
        controlClass = self.gControlador.checkedId()

        pNum = [1]
        pDen = [1]

        iNum = [1, 0]
        iDen = [1, -1]

        dNum = [1, -1]
        dDen = [1, 0]

        if controlClass == 7:  # Proporcional
            controllerModel = [[signal.TransferFunction(pNum, pDen, dt=1)]]  # Kp
            k = "p"

        elif controlClass == 8:  # Proporcional Integral
            controllerModel = [[signal.TransferFunction(pNum, pDen, dt=1)],  # Kp
                               [signal.TransferFunction(iNum, iDen, dt=1)], ]  # Ki
            k = "pi"

        elif controlClass == 9:  # Proporcional Derivativo
            controllerModel = [[signal.TransferFunction(pNum, pDen, dt=1)],  # Kp
                               [signal.TransferFunction(dNum, dDen, dt=1)], ]  # Kd
            k = "pd"

        elif controlClass == 10:  # Proporcional Integral Derivativo
            controllerModel = [[signal.TransferFunction(pNum, pDen, dt=1)],  # Kp
                               [signal.TransferFunction(iNum, iDen, dt=1)],  # Ki
                               [signal.TransferFunction(dNum, dDen, dt=1)], ]  # Kd
            k = "pid"

        elif controlClass == 11:  # Custom
            controllerNumTemp, self.numNum = self.customControllerSetter(0)
            controllerDenTemp, numDen = self.customControllerSetter(1)
            # TODO: flag que impede sequencia se o len de cada for diferente

            contNum = len(controllerNumTemp)
            contDen = len(controllerDenTemp)
            temp = contNum + contDen

            contador, i, j = 0, 0, 0
            controllerTemp = []

            # TODO:
            while contador < temp:
                if (contador % 2) == 0:
                    controllerTemp.append(controllerDenTemp[i])
                    i += 1
                else:
                    controllerTemp.append(controllerNumTemp[j])
                    j += 1
                contador += 1

            controllerModel = []
            contador = 1

            while contador < len(controllerTemp):
                controllerModel.append([signal.TransferFunction(controllerTemp[contador], controllerTemp[contador - 1], dt=1)])
                contador += 2

            k = "custom"

        elif controlClass == -1:
            # TODO: Error flag
            texto = "Modelo do controlador invalido"
            self.controllerOutput.appendPlainText(texto)
            controllerModel = 0
            k = 0

        return controllerModel, k

    def getFilter(self):
        # Conforme selecao do usuario, seta o tipo de filtro
        filterType = self.gFiltro.checkedId()

        if filterType == 12:  # Sem Filtro
            filterNum = [1]
            filterDen = [1]

        elif filterType == 13:  # Filtro Padrão
            # L = Td * (1 - Td)
            um = control.tf([1], [1], dt=1)
            tTemp = control.tf(self.modelNum, self.modelDen, dt=1)
            tDesejada = (um - tTemp)
            tDesejada = tDesejada * tTemp

            numL = tDesejada.num
            filterNum = numL[0][0]
            denL = tDesejada.den
            filterDen = denL[0][0]

        elif filterType == 14:  # Filtro Custom
            filterNum = self.textCapture(6)
            filterDen = self.textCapture(7)

        elif filterType == -1:
            # TODO: Error flag
            texto = "Modelo de filtro invalido"
            self.controllerOutput.appendPlainText(texto)

        filterL = signal.TransferFunction(filterNum, filterDen, dt=1)

        return filterL

    # TODO: Adicionar trava para quando não for informado todos os dados necessários
    ## Botao para aplicar o metodo VRFT
    def VRFTPressed(self):
        self.flag = False

        if self.ensaioText.text() != '':

            # Gera o modelo de referência da planta
            objectiveFunction = self.getRef()

            pNum = [1]
            pDen = [1]

            iNum = [1, 0]
            iDen = [1, -1]

            dNum = [1, -1]
            dDen = [1, 0]

            # Gera a função do controlador
            controllerModel, k = self.getCont()

            # Gera a função do filtro
            filterL = self.getFilter()

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
            if iv == "":  # Nao tem ensaio com variavel instrumentavel
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

            textoaux = "Parâmetros gerados para o tipo de controlador escolhido: \n\tKp = "

            # Exibe resultados de um controlador P
            if k == "p":
                ganhos = [resultado[0].item()]
                texto = textoaux + str(ganhos[0])
                cNum = [i * ganhos[0] for i in pNum]
                self.contNum = cNum
                self.contDen = pDen
                self.flag = True

            # Exibe resultados de um controlador PI
            elif k == "pi":
                ganhos = [resultado[0].item(), resultado[1].item()]
                texto = textoaux + str(ganhos[0]) + "\n\tKi = " + str(ganhos[1])
                cNum1 = [i * ganhos[0] for i in pNum]
                cNum2 = [j * ganhos[1] for j in iNum]
                cFinal = control.tf(cNum1, pDen, dt=1) + control.tf(cNum2, iDen, dt=1)
                cAux = cFinal.num
                self.contNum = cAux
                cAux = cFinal.den
                self.contDen = cAux
                self.flag = True

            # Exibe resultados de um controlador PD
            elif k == "pd":
                ganhos = [resultado[0].item(), resultado[1].item()]
                texto = textoaux + str(ganhos[0]) + "\n\tKd = " + str(ganhos[1])
                cNum1 = [i * ganhos[0] for i in pNum]
                cNum2 = [i * ganhos[1] for i in dNum]
                cFinal = control.tf(cNum1, pDen, dt=1) + control.tf(cNum2, dDen, dt=1)
                cAux = cFinal.num
                self.contNum = cAux
                cAux = cFinal.den
                self.contDen = cAux
                self.flag = True

            # Exibe resultados de um controlador PID
            elif k == "pid":
                ganhos = [resultado[0].item(), resultado[1].item(), resultado[2].item()]
                texto = textoaux + str(ganhos[0]) + "\n\tKi = " + str(ganhos[1]) + "\n\tKd = " + str(ganhos[2])
                cNum1 = [i * ganhos[0] for i in pNum]
                cNum2 = [i * ganhos[1] for i in iNum]
                cNum3 = [i * ganhos[2] for i in dNum]
                cFinal = control.tf(cNum1, pDen, dt=1) + control.tf(cNum2, iDen, dt=1) + control.tf(cNum3, dDen, dt=1)
                cAux = cFinal.num
                self.contNum = cAux
                cAux = cFinal.den
                self.contDen = cAux
                self.flag = True

            # Exibe resultados de um controlador customizado
            elif k == "custom":
                ganhos = [resultado[x].item() for x in range(self.numNum)]
                texto = "Parâmetros gerados para o tipo de controlador escolhido: \n\t"
                textoaux = ""
                for y in range(self.numNum):
                    textoaux = textoaux + "K" + str(y + 1) + " = " + str(ganhos[y]) + "\n\t"
                texto = texto + textoaux
                self.flag = True

            self.controllerOutput.appendPlainText(texto)

        else:
            texto = "Adicione um conjunto de dados."
            self.controllerOutput.setPlainText(texto)

    ## Botao para gerar o grafico de T(z)
    def graphTzPressed(self):
        lw = 1  # linewidth
        case = 0
        count1 = False
        count2 = False

        if self.flag:
            count1 = True
        if self.ensaioMFText.text() != '':
            count2 = True

        if count1 or count2:
            if not count2:
                case = 1
            elif not count1:
                case = 2
            else:
                case = 3

        num = self.dfEnsaioMF.shape[0]

        dfEnsaioMFCopia = self.dfEnsaioMF.copy()

        entradaMFTemp = dfEnsaioMFCopia.pop(dfEnsaioMFCopia.columns[0]).to_numpy()
        saidaMFTemp = dfEnsaioMFCopia.pop(dfEnsaioMFCopia.columns[0]).to_numpy()

        entradaMF = np.ones((num, 1))
        saidaMF = np.ones((num, 1))

        for x in range(0, num):
            entradaMF[x] = entradaMFTemp[x]
            saidaMF[x] = saidaMFTemp[x]

        # Gráfico dados da malha fechada
        if case == 2:

            plt.plot(entradaMF, "r", drawstyle="steps", linewidth=lw, label="Entrada")
            plt.plot(saidaMF, "b", drawstyle="steps", linewidth=lw, label="Saida")
            plt.grid(True)
            plt.xlabel("tempo (amostras)")
            plt.ylabel("Tensao [V]")
            plt.legend()
            plt.tight_layout()

        # Gráfico Td e malha fechada juntas
        elif case == 3:

            Td = signal.TransferFunction(self.modelNum, self.modelDen, dt=1)

            yTd = vrft.filter(Td, entradaMF)

            # Remove os dados que influenciam na escala dos sianis
            minimo = np.amin(entradaMF) if np.amin(entradaMF) <= np.amin(saidaMF) else np.amin(saidaMF)

            where = np.where(yTd >= minimo)
            index = where[0][0]

            yTd = yTd[index: num]
            saidaMF = saidaMF[index: num]
            entradaMF = entradaMF[index: num]

            # plot 1:
            plt.subplot(2, 1, 1)
            plt.plot(entradaMF, "b", drawstyle="steps", linewidth=lw, label="Entrada Malha Fechada")
            plt.plot(yTd, "r", drawstyle="steps", linewidth=lw, label="Saida Td desejada")
            plt.grid(True)
            plt.ylabel("Tensao [V]")
            plt.legend()

            # plot 2:
            plt.subplot(2, 1, 2)
            plt.plot(entradaMF, "g", drawstyle="steps", linewidth=lw, label="Entrada Malha Fechada")
            plt.plot(saidaMF, "y", drawstyle="steps", linewidth=lw, label="Saida Malha Fechada")
            plt.grid(True)
            plt.legend()
            plt.xlabel("tempo (amostras)")
            plt.ylabel("Tensao [V]")
            plt.tight_layout()

        elif case <= 1:
            texto = "Adicione um ensaio de malha fechada e aplique o método VRFT primeiro."
            self.MFOutput.setPlainText(texto)

        if case > 0:
            plt.show()

    # TODO:
    ## Botao para gerar o custo JVR
    def JVRPressed(self):

        count1 = False
        count2 = False

        if self.flag:
            count1 = True
        if self.ensaioMFText.text() != '':
            count2 = True

        if count1 is True and count2 is True:

            num = self.dfEnsaioMF.shape[0]

            dfEnsaioMFCopia = self.dfEnsaioMF.copy()

            entradaMFTemp = dfEnsaioMFCopia.pop(dfEnsaioMFCopia.columns[0]).to_numpy()
            saidaMFTemp = dfEnsaioMFCopia.pop(dfEnsaioMFCopia.columns[0]).to_numpy()

            entradaMF = np.ones((num, 1))
            saidaMF = np.ones((num, 1))

            for x in range(0, num):
                entradaMF[x] = entradaMFTemp[x]
                saidaMF[x] = saidaMFTemp[x]

            Td = signal.TransferFunction(self.modelNum, self.modelDen, dt=1)

            yTd = vrft.filter(Td, entradaMF)

            maxEnsaio = np.amax(yTd)
            minEnsaio = np.amin(yTd)

            for y in range(0, num):
                yTd[y] = (yTd[y] - minEnsaio) / (maxEnsaio - minEnsaio)

            maxMF = np.amax(saidaMF)
            minMF = np.amin(saidaMF)

            for y in range(0, num):
                saidaMF[y] = (saidaMF[y] - minMF) / (maxMF - minMF)

            soma = 0

            for i in range(num):
                diff = saidaMF[i][0] - yTd[i][0]
                squareDiff = diff ** 2
                soma += squareDiff

            MSE = soma / num
            texto = "Estimativa do custo minimizado: " + str(MSE)
            self.MFOutput.appendPlainText(texto)

        else:
            texto = "Aplicar o método VRFT primeiro e adicionar os dados da malha fechada."
            self.MFOutput.setPlainText(texto)

    # TODO:
    ## Botao para calcular a sensibilidade
    def sensiPressed(self):

        if self.flag:
            '''
            T = C * G / (1 + C * G)
            G = T / (C - T * C)
            '''

            tdEsperado = control.tf(self.modelNum, self.modelDen, dt=1)

            cProj = control.tf(self.contNum, self.contDen, dt=1)

            G = tdEsperado / (cProj - (tdEsperado * cProj))

            sensi = 1 / (1 + G * cProj)

            x = sensi.num
            x = list(x[0][0])
            y = sensi.den
            y = list(y[0][0])

            z, p, k = control.tf2zpk(x, y)

            tam1 = z.shape[0]

            texto = "Sensibilidade estimada da planta: "
            self.MFOutput.setPlainText(texto)

            texto = [str(k)]
            auxtext = "(z + ("

            for i in range(tam1):
                redondo = np.round(z[i], 7)
                if z[i] == 0:
                    aux = "(z)"
                elif "j" in str(redondo):
                    aux = auxtext + str(redondo)[1:-1] + "))"
                else:
                    aux = auxtext + str(redondo) + "))"
                texto.append(aux)

            texto = ''.join(texto)

            length = len(texto)

            self.MFOutput.appendPlainText(texto)

            linha = []
            for i in range(length):
                if i < 100:
                    if i < len(str(k)):
                        linha.append(" ")
                    else:
                        linha.append("-")

            linha = ''.join(linha)

            self.MFOutput.appendPlainText(linha)

            tam2 = p.shape[0]

            texto = ["  "]

            for j in range(tam2):
                redondo = np.round(p[j], 7)
                if p[j] == 0:
                    aux = "(z)"
                elif "j" in str(redondo):
                    aux = auxtext + str(redondo)[1:-1] + "))"
                else:
                    aux = auxtext + str(redondo) + "))"
                texto.append(aux)

            texto = ''.join(texto)

            self.MFOutput.appendPlainText(texto)

        else:
            texto = "Aplicar o método VRFT primeiro."
            self.MFOutput.setPlainText(texto)

    ######
    ## Trabalho com a caixa de texto output:
    # setPlainText - apaga todo o texto presente e escreve o texto passado como argumento
    # insertPlainText - insere o texto passado como argumento no inicio da caixa de texto sem apagar o texto antigo, nao adiciona nova linha
    # appendPlainText - insere o texto passado como argumento apos o texto presente sem apagar o texto antigo, adiciona uma nova linha automatica

    ## Botao para buscar planilha com os dados do ensaio da planta
    def getFile(self):
        file_filter = 'Data File (*.xlsx *.csv);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileName(parent=self,
                                                caption='Select a data file',
                                                directory=os.getcwd(),
                                                filter=file_filter,
                                                initialFilter='Data File (*.xlsx *.csv)')
        if response[0] == '':
            return False
        elif response[0][-1] == 'v':
            df = pd.read_csv(response[0])
        else:
            df = pd.read_excel(response[0])
        return df, response[0]

    def ensaioPressed(self):
        self.dfEnsaio, address = self.getFile()
        if address:
            self.ensaioText.setText(address)
            texto = "Dados de ensaio carregados. Numero de amostras dos sinais carregados: " + str(
                self.dfEnsaio.shape[0])
            self.controllerOutput.setPlainText(texto)
        # TODO: if address == False

    ## Botao para buscar planilha com os dadosdo ensaio da variavel instrumentavel da planta
    def ivPressed(self):
        self.dfIV, address = self.getFile()
        if address:
            self.ivText.setText(address)
            texto = "Dados da variavel instrumentavel carregados. Numero de amostras dos sinais carregados: " + str(
                self.dfIV.shape[0])
            self.controllerOutput.appendPlainText(texto)

    ## Botao para buscar planilha com os dados do ensaio em malha fechada da planta
    def ensaioMFPressed(self):
        self.dfEnsaioMF, address = self.getFile()
        if address:
            self.ensaioMFText.setText(address)
            texto = "Dados de ensaio em malha fechada carregados. Numero de amostras dos sinais carregados: " + str(
                self.dfEnsaioMF.shape[0])
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
