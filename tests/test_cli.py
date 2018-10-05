from pytest import mark

from functools import partial
from os import listdir, environ
from os.path import abspath, dirname, join
from subprocess import check_output

GAME_OF_LIFE = environ.get('GAME_OF_LIFE') or 'game-of-life'

HERE = abspath(dirname(__file__))
here_path = partial(join, HERE)

LIVES = here_path('lives')
life_path = partial(join, LIVES)


def worlds(life):
    return sorted(listdir(life_path(life)))


def lives():
    return sorted(listdir(LIVES))


def data():
    for life in lives():
        ws = worlds(life)
        for world, next_one in zip(ws, ws[1:]):
            yield join(life, world), join(life, next_one)


@mark.parametrize('world, next_one', data())
def test(world, next_one):
    args = [GAME_OF_LIFE]
    with open(life_path(world), 'rb') as stdin:
        stdout = check_output(args, stdin=stdin)
    with open(life_path(next_one), 'rb') as next_one:
        assert stdout == next_one.read()
