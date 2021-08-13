import unittest
from basePage import BasePage

def main():
    # Criando as classes de testes
    tc1=unittest.TestLoader().loadTestsFromTestCase(BasePage)

    #Adicionando as classes no suite
    testingBasePage = unittest.TestSuite([tc1])

    #Executando todos os testes definidos
    unittest.TextTestRunner().run(testingBasePage)


if __name__ == "__main__":
    main()