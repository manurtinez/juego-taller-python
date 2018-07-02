class Boton(object):
    """
    Esta clase boton contiene su inicializador, funciones de control, como si se pasa el cursor por el boton. Y tambien para colocar
    en pantall el boton"""
    
    def __init__(self, color, colorSuave, display, texto, posIzquierda, posMedio, ancho, alto, colorTexto, posTexto, anchoDisplay,
                 altoDisplay, fuente):
        self.color=color
        self.colorSuave=colorSuave
        self.display=display
        self.texto=texto
        self.posIzquierda=posIzquierda
        self.posMedio=posMedio
        self.ancho=ancho
        self.alto=alto
        self.colorTexto=colorTexto
        self.posTexto=posTexto
        self.anchoDisplay=anchoDisplay
        self.altoDisplay=altoDisplay
        self.fuente=fuente

    def textoDisplay(self):
        textoDisplay = self.fuente.render(self.texto, True, self.colorTexto)
        self.display.blit(textoDisplay, [self.anchoDisplay - (textoDisplay.get_rect().width / 2),
                                        self.altoDisplay + (self.ancho / 2) - (textoDisplay.get_rect().height / 2)
                                        + self.posTexto])

    def mostarBoton(self):
        self.display.fill(self.color, (self.posIzquierda, self.posMedio, self.ancho, self.alto))
        self.textoDisplay()

    def toca(self, cursor):
        if self.posIzquierda < cursor[0] < self.posIzquierda + self.ancho and self.posMedio < cursor[1] < self.posMedio + self.alto:
            self.display.fill(self.colorSuave, (self.posIzquierda, self.posMedio, self.ancho, self.alto))
            self.textoDisplay()
            return True