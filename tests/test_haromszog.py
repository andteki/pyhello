from triangle import Triangle

class TestTriangle:

    @classmethod
    def setup_class(cls):
        cls.triangle = Triangle()

    def test_calcArea_30_35(self):
        actual = self.triangle.calcArea(30, 35)
        expected = 525
        assert actual == expected

    def test_calcArea_65_75(self):
        actual = self.triangle.calcArea(60, 75)
        expected = 2250
        assert actual == expected


