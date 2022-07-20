from src.command.debian.apt_cache import AptCache

from tests.mocks.command_run_mock import CommandRunMock


def test_interface_get_package_dependencies(mocker):
    ''' Check argument construction for `apt-cache depends` '''
    with CommandRunMock(mocker, AptCache(1).get_package_dependencies, {'package': 'vim'}) as call_args:
        assert call_args == ['apt-cache',
                             'depends',
                             '--no-recommends',
                             '--no-suggests',
                             '--no-conflicts',
                             '--no-breaks',
                             '--no-replaces',
                             '--no-enhances',
                             '--no-pre-depends',
                             'vim']
