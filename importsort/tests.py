import pytest

import importsort


@pytest.fixture(autouse=True)
def configure():
    importsort.configure(first_party_modules=['first_party', 'mymodule'])


@pytest.fixture
def run(tmp_path):
    def _runner(code_snippet):
        filename = tmp_path / 'tmp.py'
        with open(filename, 'w') as f:
            f.write('\n'.join(code_snippet) + '\n')
        importsort.run_query([filename], write=True, silent=False)
        with open(filename, 'r') as f:
            return f.read().splitlines()

    yield _runner


def test_group_order(run):
    assert run(['from a_thirdparty import d', 'from os import c']) == [
        'from os import c',
        '',
        'from a_thirdparty import d',
    ]


def test_alphabet_imports_with_from(run):
    assert run(['from b import z', 'from a import z']) == [
        'from a import z',
        'from b import z',
    ]


def test_alphabet_imports_without_from(run):
    assert run(['import z', 'import a']) == [
        'import a',
        'import z',
    ]


def test_modules_in_one_statement(run):
    assert run(['import b, a, c']) == ['import a, b, c']


def test_modules_in_one_statement_with_line_breaks(run):
    assert run(['import b,\\', '  a, \\', '  c']) == ['import a, \\', '  b, \\', '  c']


def test_from_order(run):
    assert run(['from a import z', 'import a']) == [
        'import a',
        'from a import z',
    ]


def test_symbol_order(run):
    assert run(['from a import b, a, c']) == ['from a import a, b, c']


def test_symbol_order_with_parentheses(run):
    assert run(['from a import (b, a, c)']) == ['from a import (a, b, c)']


def test_symbol_order_with_line_breaks(run):
    assert run(['from a import\\', '  c,\\', '  b']) == [
        'from a import \\',
        '  b, \\',
        '  c',
    ]


def test_sort_identical_imports(run):
    assert run(['import a', 'import a']) == ['import a', 'import a']


def test_preserve_leading_comments(run):
    assert run(['import b', '#comment a', 'import a']) == [
        '#comment a',
        'import a',
        'import b',
    ]


def test_preserve_same_line_comments(run):
    assert run(['import b  # comment b', 'import a', 'import c']) == [
        'import a',
        'import b  # comment b',
        'import c',
    ]


def test_preserve_block_comments_including_whitespace(run):
    assert run(
        [
            '#commentb 1',
            '#commentb 2',
            '',
            '#commentb 4',
            'import b',
            'import a',
            'import c',
        ]
    ) == [
        'import a',
        '#commentb 1',
        '#commentb 2',
        '',
        '#commentb 4',
        'import b',
        'import c',
    ]


def test_preserve_same_line_comments_during_block_statement(run):
    assert run(
        ['from a import (', '  c,  # commentC', '  a,', '  b  # commentB', ')',]
    ) == ['from a import (', '  a,', '  b,  # commentB', '  c  # commentC', ')',]
