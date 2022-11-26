from modules.cfg_to_cnf import get_set_of_production


def test_convertion():
    cnf = {
        "S": ["a", "AS", "AX", "SA", "YB"],
        "A": ["a", "b", "SA", "AS", "AX", "YB"],
        "B": ["b"],
        "T": ["a", "AS", "AX", "SA", "YB"],
        "X": ["SA"],
        "Y": ["a"]
    }
    result = get_set_of_production()
    for key, value in result.items():
        for i in value:
            assert i in cnf[key]
