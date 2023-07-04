from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criaDocumento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Quantidade de dígitos do documento incorreta')


class DocCPF:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!!!')

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self) -> str:
        return self.format()


class DocCNPJ:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!!!')

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self) -> str:
        return self.format()