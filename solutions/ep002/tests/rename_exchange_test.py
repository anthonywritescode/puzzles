import rename_exchange

import pytest


def test_rename_exchange_successful(tmp_path):
    f1 = tmp_path.joinpath('f1')
    f1.write_text('file 1')
    f2 = tmp_path.joinpath('f2')
    f2.write_text('file 2')

    rename_exchange.rename_exchange(str(f1), str(f2))

    assert f1.read_text() == 'file 2'
    assert f2.read_text() == 'file 1'


def test_rename_exchange_file_does_not_exist(tmp_path):
    dne = tmp_path.joinpath('dne')
    dne2 = tmp_path.joinpath('dne2')

    with pytest.raises(OSError):
        rename_exchange.rename_exchange(str(dne), str(dne2))
