import pytest

from project0 import project0

myurl='http://normanpd.normanok.gov/filebrowser_download/657/2019-02-14%20Daily%20Arrest%20Summary.pdf'
def test_download_incidents():
    assert project0.fetchincidents(myurl) is not None
