from io import StringIO

def test_factorial(monkeypatch, capsys):
    from factorial import factorial

    monkeypatch.setattr('sys.stdin', StringIO("5\n"))
    factorial()
    captured = capsys.readouterr()
    assert '120' in captured.out, "Expected '120' for input '5' but got something else..."

    monkeypatch.setattr('sys.stdin', StringIO("10\n"))
    factorial()
    captured = capsys.readouterr()
    assert '3628800' in captured.out, "Expected '3628800' for input '10' but got something else..."

def test_foobar(capsys):
    from foobar import foobar
    foobar_str = '1\n2\nfoo\n4\nbar\nfoo\n7\n8\nfoo\nbar\n11\nfoo\n13\n14\nfoobar\n16\n17\nfoo\n19\nbar\nfoo\n22\n23\nfoo\nbar\n26\nfoo\n28\n29\nfoobar\n'
    foobar()
    captured = capsys.readouterr()
    assert foobar_str in captured.out, f"Expected output\n{foobar_str} but got something different..."

def test_grade_calculator(monkeypatch, capsys):
    from grade_calculator import grade_calculator

    pairs = {
        '59': 'F',
        '60': 'D',
        '69': 'D',
        '70': 'C',
        '79': 'C',
        '80': 'B',
        '89': 'B',
        '90': 'A',
        '100': 'A'
    }

    for number, letter in pairs.items():
        monkeypatch.setattr('sys.stdin', StringIO(f"{number}\n"))
        grade_calculator()
        captured = capsys.readouterr()
        assert letter.lower() in captured.out.lower(), f"Expected output '{letter}' for input '{number}' but got something different..."

def test_leap_year(monkeypatch, capsys):
    from leap_year import leap_year

    pairs = {
        '1900': 'regular year',
        '1992': 'leap year',
        '2000': 'leap year'
    }

    for year, status in pairs.items():
        monkeypatch.setattr('sys.stdin', StringIO(f"{year}\n"))
        leap_year()
        captured = capsys.readouterr()
        assert status.lower() in captured.out.lower(), f"Expected output '{status}' for input '{year}' but got something different..."

def test_vowel_counter(monkeypatch, capsys):
    from vowel_counter import vowel_counter

    pairs = {
        'aardvark': '3',
        'city': '1',
        'onomatopoeia': '8',
        'crwth': '0',
        'Adobado': '4' 
    }

    for word, vowel_count in pairs.items():
        monkeypatch.setattr('sys.stdin', StringIO(f"{word}\n"))
        vowel_counter()
        captured = capsys.readouterr()
        assert vowel_count in captured.out, f"Expected output '{vowel_count}' for input '{word}' but got something different..."