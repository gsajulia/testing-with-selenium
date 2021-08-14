import unittest
from exploreDegrees import ExploreDegrees
from searchAboutCourse import SearchAboutCourse

def main():
    # Criando as classes de testes
    # tc1=unittest.TestLoader().loadTestsFromTestCase(ExploreDegrees)
    tc2=unittest.TestLoader().loadTestsFromTestCase(SearchAboutCourse)

    #Adicionando as classes no suite
    # testingBasePage = unittest.TestSuite([tc1, tc2])

    #Executando todos os testes definidos
    # unittest.TextTestRunner().run(tc1)
    unittest.TextTestRunner().run(tc2)


if __name__ == "__main__":
    main()