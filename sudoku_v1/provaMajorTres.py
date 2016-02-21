import unittest

class  ProvaMajorTresTestCase(unittest.TestCase):

    def major_de_tres(self, A, B, C):
        if A > B:
            if A > C:
                return A
            else:
                return C
        elif B > C:
            return B
        else: 
            return C
            
    def test_prova_major_de_tres(self):
        
        self.assertEqual(self.major_de_tres(0, 2, 1), 2)
        self.assertEqual(self.major_de_tres(-1, 1, 0), 1)
        self.assertEqual(self.major_de_tres(1, 2, 3), 3)
        self.assertEqual(self.major_de_tres(0, 1, 1), 1)
        self.assertEqual(self.major_de_tres(-1, 1, 1), 1)
        self.assertEqual(self.major_de_tres(-1, 0, 0), 0)
        self.assertEqual(self.major_de_tres(2, 2, 0), 2)
        self.assertEqual(self.major_de_tres(0, 0, 0), 0)
        self.assertEqual(self.major_de_tres(2, 2, 3), 3)
        self.assertEqual(self.major_de_tres(3, 2, 3), 3)
        self.assertEqual(self.major_de_tres(3, 2, 4), 4)
        self.assertEqual(self.major_de_tres(3, 2, 2), 3)
        
    def test_prova_major_de_tres_B(self):
        
        self.assertEqual(self.major_de_tres(100, -100, 1), 100)
        self.assertEqual(self.major_de_tres(-100, 0, -100), 0)
        

if __name__ == '__main__':
    unittest.main()

