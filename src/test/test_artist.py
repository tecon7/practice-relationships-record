from artist import Artist
from record import Record
from song import Song

def test_artist_init_with_name():
    """
    Should be able to initialize an Artist object
    with a name
    """
    artist = Artist('Avril Lavigne')
    assert artist.name == 'Avril Lavigne'

def test_artist_name_can_be_changed():
    """
    Should be able to change an artist's name after
    it is created
    """
    artist = Artist('Avril Lavigne')
    artist.name = 'Cardi B'
    assert artist.name == 'Cardi B'

def test_artist_get_name():
    """
    get_name() should return the artist's name
    """
    artist = Artist('Avril Lavigne')
    assert artist.get_name() == 'Avril Lavigne'

def test_artist_get_records():
    """
    get_records() should return the list of the
    artist's records
    """
    artist = Artist('Avril Lavigne')
    record = Record('Let Go', artist, 2001)
    artist.records = [record]
    assert artist.get_records() == [record]

def test_artist_get_first_record():
    """
    get_first_record() should return the first
    record (by year) released by the artist
    """
    artist = Artist('Avril Lavigne')
    record1 = Record('Let Go', artist, 2001)
    record2 = Record('Love Sux', artist, 2022)
    artist.records = [record1, record2]
    assert artist.get_first_record() == record1

    