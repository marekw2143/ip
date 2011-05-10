
    def test_avg(self):
        ret = avg(range(3))
        self.assertEqual(ret, 1)
    def test_dev(self):
        ret = dev(range(3))
        print ret
