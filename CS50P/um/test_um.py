import um

def test_1():
    assert um.count("Um excuse me?") == 1
def test_2():
    assert um.count("um um um um ,um um, um!") == 7
def test_3():
    assert um.count("yummy") == 0
