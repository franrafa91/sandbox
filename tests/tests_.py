from sandbox_fc import functions, to_string

def test_haversine():
    # Amsterdam to Berlin
    assert functions.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291

def test_to_string():
    a = 5000.14
    fmt = to_string.Format()

    for i in range(1,4):
        print(f"Number format #{i}")
        print(fmt(a))
        fmt.update(i)
        assert(type(fmt(a)) == str)