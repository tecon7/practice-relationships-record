# practice-relationships-record

# Deliverables:
## Initializers, Readers, Writers
Artist
- `Artist __init__(self, name)`
    - `Artist` is initialized with a name (string)
    - name *can* be changed after the artist is initialized
- `Artist get_name()`
    - returns the artist's name

Record
- `Record __init__(self, title, artist, year)`
    - `Record` is initialized with a title (string), artist (`Artist`), and a year (int)
    - title, artist, and year can be changed after the record is initialized
- `Record get_title()`
    - returns the record's title in title-case (hint: use the string method .title())
- `Record get_year()`
    - return the record's year
- `Record get_artist()`
    - returns the `Artist` object associated with the `Record` instance

Song
- `Song __init__(title, runtime, genre)`
    - `Song` is initialized with a title (string), runtime in seconds (int), and a genre (string)
    - title, runtime, and genre can be changed after the object is created
- `Song get_title()`
    - returns the song's title in title-case (hint: use the string method .title())
- `Song get_runtime()`
    - returns the song's 
- `Song get_genre()`
    - returns the song's genre

## Object Relationship Methods
Artist
- `Artist get_records()`
    - returns the list of `Record` objects associated with the `Artist` instance

Record
- `Record get_songs()`
    - returns the list of `Song` objects associated with the `Record` instance
- `Record get_artist()`
    - returns the `Artist` object associated with the `Record` instance

Song
- `Song get_record()`
    - returns the `Record` object associated with the `Song` instance
- `Song get_artist()`
    - returns the `Artist` object associated with the `Song` instance

## Aggregate and Association Methods
Artist
- `Artist get_first_record()`
    - returns the first record this artist released, by year

Record
- `Record total_runtime()`
    - returns the total runtime in seconds of all songs on the record
- `Record has_song(song)`
    - returns True if the `song` exists on the record

- `Record get_longest_song()`
    - returns the `Song` object with the longest runtime on the `Record` instance
