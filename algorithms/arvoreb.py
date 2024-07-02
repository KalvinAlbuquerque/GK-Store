import unidecode

class Registro:
  def __init__(self):
    self.Chave = None
    self.Elemento = None
    self.posicaoNoArquivo = -1

class Pagina:
  def __init__(self, ordem):
    self.n = 0
    self.r = [None for _ in range(ordem)]
    self.p = [None for _ in range(ordem+1)]

class BTree():
    
    def __init__(self, order: int) -> None:
        self.order = order
        self.root = None

    def converter_para_numerico(self, texto):
        texto = unidecode.unidecode(texto)
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        texto_numerico = ''
        for letra in texto.lower():  
            if letra.isalpha():  
                indice = alfabeto.index(letra) + 1  
                texto_numerico += str(indice)  
        return int(texto_numerico.strip()) 
    
    def contem_apenas_letras(self, texto):
        tem_letras = any(letra.isalpha() for letra in texto)

        return tem_letras

    def getListaOrdenada(self) -> list:
        """ 
            Retorna uma lista em ordem crescente das chaves presentes na árvore
        """
        result = []
        
        self.__getOrdenado__(self.root, result)

        return result

    def __getOrdenado__(self, Ap, lista):

        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getOrdenado__(Ap.p[i], lista)
                lista.append(Ap.r[i].Elemento)
                i += 1
            self.__getOrdenado__(Ap.p[i], lista)

    def getListaLimiteMaxMinElemento(self, registroMax, registroMin) -> list:
        
        result = []

        self.__getValorMaiorXMenorYElemento__(registroMin, registroMax, self.root, result)

        return result
    
    def __getValorMaiorXMenorYElemento__(self, x, x2, Ap, lista):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMaiorXMenorYElemento__(x, x2, Ap.p[i], lista)
                if (Ap.r[i].Elemento >= x.Elemento and Ap.r[i].Elemento <= x2.Elemento):
                    lista.append(Ap.r[i].Chave)
                i += 1
            self.__getValorMaiorXMenorYElemento__(x, x2, Ap.p[i], lista)

    def getListaValoresMaioresElemento(self, registro: Registro) -> list:
        """ 
            Retorna uma lista de valores maiores que uma chave
        """

        result = []

        self.__getValorMaiorElemento__(registro, self.root, result)

        return result
    
    def __getValorMaiorElemento__(self, x, Ap, lista):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMaiorElemento__(x, Ap.p[i], lista)
                if (Ap.r[i].Elemento > x.Elemento):
                    lista.append(Ap.r[i].Chave)
                i += 1
            self.__getValorMaiorElemento__(x, Ap.p[i], lista)

    def getListaValoresMenoresElemento(self, registro: Registro) -> list:
        """ 
            Retorna uma lista de valores menores que uma chave
        """

        result = []

        self.__getValorMenorElemento__(registro, self.root, result)

        return result

    def __getValorMenorElemento__(self, x, Ap, lista):

        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMenorElemento__(x, Ap.p[i], lista)
                if (Ap.r[i].Elemento < x.Elemento):
                    lista.append(Ap.r[i].Chave)
                i += 1
            self.__getValorMenorElemento__(x, Ap.p[i], lista)
    
    def getListaLimiteMaxMinChave(self, registroMax, registroMin) -> list:
        
        result = []

        self.__getValorMaiorXMenorYElemento__(registroMin, registroMax, self.root, result)

        return result
    
    def __getValorMaiorXMenorYChave__(self, x, x2, Ap, lista):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMaiorXMenorYChave__(x, x2, Ap.p[i], lista)
                if (Ap.r[i].Chave >= x.Chave and Ap.r[i].Chave <= x2.Chave):
                    lista.append(Ap.r[i].Elemento)
                i += 1
            self.__getValorMaiorXMenorYChave__(x, x2, Ap.p[i], lista)

    def getListaValoresMaioresChave(self, registro: Registro) -> list:
        """ 
            Retorna uma lista de valores maiores que uma chave
        """

        result = []

        self.__getValorMaiorChave__(registro, self.root, result)

        return result
    
    def __getValorMaiorChave__(self, x, Ap, lista):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMaiorChave__(x, Ap.p[i], lista)
                if (Ap.r[i].Chave > x.Chave):
                    lista.append(Ap.r[i].Elemento)
                i += 1
            self.__getValorMaiorChave__(x, Ap.p[i], lista)

    def getListaValoresMenoresChave(self, registro: Registro) -> list:
        """ 
            Retorna uma lista de valores menores que uma chave
        """

        result = []

        self.__getValorMenorChave__(registro, self.root, result)

        return result

    def __getValorMenorChave__(self, x, Ap, lista):

        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.__getValorMenorChave__(x, Ap.p[i], lista)
                if (Ap.r[i].Chave < x.Chave):
                    lista.append(Ap.r[i].Elemento)
                i += 1
            self.__getValorMenorChave__(x, Ap.p[i], lista)

    def search(self, x, Ap):
        i = 1
        if (Ap == None):
            print("Registro não está presente na árvore\n")
            return None

        while (i < Ap.n and x.Chave > Ap.r[i - 1].Chave):
            i += 1
        if (x.Chave == Ap.r[i - 1].Chave):
            x = Ap.r[i - 1]
            return x

        if (x.Chave < Ap.r[i - 1].Chave):
            x = self.search(x, Ap.p[i - 1])
        else:
            x = self.search(x, Ap.p[i])
        
        return x
    
    def insert_from_list(self, listOfKeys, listOfElements):
        
        posicaoCounter = 0
        for key, element in zip(listOfKeys, listOfElements):
           novoRegistro = Registro()
           novoRegistro.Chave = int(key) if not self.contem_apenas_letras(key) else self.converter_para_numerico(key) # pra garantir que a chave vai ser um numero
           novoRegistro.Elemento = element
           novoRegistro.posicaoNoArquivo = posicaoCounter
           self.__insert_element__(novoRegistro)
           posicaoCounter += 1
    
    def __insert_element__(self, reg: Registro):
        
        cresceu = False
        regRetorno = Registro()
        pagRetorno = Pagina(self.order)

        cresceu, regRetorno, pagRetorno = self.__insert_helper__(reg, self.root, cresceu, regRetorno, pagRetorno, self.order)

        if (cresceu):
            ApTemp = Pagina(self.order)
            ApTemp.n = 1
            ApTemp.r[0] = regRetorno
            ApTemp.p[1] = pagRetorno
            ApTemp.p[0] = self.root
            self.root = ApTemp
        
    def __insert_helper__(self, Reg, Ap, Cresceu, RegRetorno, ApRetorno, Ordem):
        
        i = 1
        J = None
        if (Ap == None):
            Cresceu = True
            RegRetorno = Reg
            ApRetorno = None
            return Cresceu, RegRetorno, ApRetorno

        while ( i < Ap.n and Reg.Chave > Ap.r[i - 1].Chave ):
            i+= 1

        # if(Reg.Chave == Ap.r[i - 1].Chave):
        #     print(" Erro: Registro já está presente\n")
        #     Cresceu = False
        #     return Cresceu, RegRetorno, ApRetorno

        if(Reg.Chave < Ap.r[i - 1].Chave ):
            i-= 1

        Cresceu, RegRetorno, ApRetorno = self.__insert_helper__(Reg, Ap.p[i], Cresceu, RegRetorno, ApRetorno, Ordem)

        if(not Cresceu):
            return Cresceu, RegRetorno, ApRetorno
        if (Ap.n < Ordem): # Página tem espaco
            self.__insert_on_page__(Ap, RegRetorno, ApRetorno)
            Cresceu = False
            return Cresceu, RegRetorno, ApRetorno

        # Overflow: Página tem que ser dividida /
        ApTemp = Pagina(Ordem)
        ApTemp.n = 0
        ApTemp.p[0] = None
        if (i < (Ordem//2) + 1):
            self.__insert_on_page__(ApTemp, Ap.r[Ordem - 1], Ap.p[Ordem])
            Ap.n-= 1
            self.__insert_on_page__(Ap, RegRetorno, ApRetorno)
        else:
            self.__insert_on_page__(ApTemp, RegRetorno, ApRetorno)
        for J in range((Ordem//2) + 2, Ordem + 1):
            self.__insert_on_page__(ApTemp, Ap.r[J - 1], Ap.p[J])
        Ap.n = (Ordem//2)
        ApTemp.p[0] = Ap.p[(Ordem//2) + 1]
        RegRetorno = Ap.r[(Ordem//2)]
        ApRetorno = ApTemp
        return Cresceu, RegRetorno, ApRetorno
    
    def __insert_on_page__(self, Ap, Reg, ApDir):
        k = Ap.n
        NaoAchouPosicao = (k > 0)
        while (NaoAchouPosicao):
            if ( Reg.Chave >= Ap.r[k - 1].Chave ):
                NaoAchouPosicao = False
                break
            Ap.r[k] = Ap.r[k - 1]
            Ap.p[k + 1] = Ap.p[k]
            k-= 1
            if (k < 1):
                NaoAchouPosicao = False

        Ap.r[k] = Reg
        Ap.p[k + 1] = ApDir
        Ap.n += 1
    
    def Imprime(self, Ap):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.Imprime(Ap.p[i])
                print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
                i += 1
            self.Imprime(Ap.p[i])

    def ImprimeMenor(self, x, Ap):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.ImprimeMenor(x, Ap.p[i])
                if (Ap.r[i].Chave < x.Chave):
                    print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
                i += 1
            self.ImprimeMenor(x, Ap.p[i])
    
    def ImprimeMaior(self, x, Ap):
        if (Ap != None):
            i = 0
            while i < Ap.n:
                self.ImprimeMaior(x, Ap.p[i])
                if (Ap.r[i].Chave > x.Chave):
                    print(Ap.r[i].Chave, "-", Ap.r[i].Elemento)
                i += 1
            self.ImprimeMaior(x, Ap.p[i])