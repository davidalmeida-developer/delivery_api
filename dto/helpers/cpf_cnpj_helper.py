from abc import ABC, abstractmethod
from pydantic import BaseModel
from validate_docbr import CPF, CNPJ
from email_validator import EmailNotValidError, validate_email
from phonenumbers import is_valid_number, parse, NumberParseException


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


class Validator:

    @staticmethod
    def validateDocument(document: str):
        document = Documento.criaDocumento(document)
        return str(document)

    @staticmethod
    def validateEmail(email: str):
        try:
            validate_email(email=email)
        except EmailNotValidError:
            raise ValueError('Email inválido')
        return email

    @staticmethod
    def validatePhoneNumber(phone_number: str):
        try:
            if len(phone_number) in [11, 10] and phone_number[0:2] != "+55":
                phone_number = f"+55{phone_number}"
            parsed_number = parse(phone_number, None)
            if not is_valid_number(parsed_number):
                raise ValueError('Número de telefone inválido')
        except NumberParseException:
            raise ValueError('Número de telefone inválido')
        return phone_number
