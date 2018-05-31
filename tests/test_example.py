def test_pathlib(fs): #fs is the fake filesystem fixture
    """Attempt to use a pathlib path"""

    import pathlib
    base_dir = pathlib.Path('/tmp/corpus_data')
    fs.create_dir(base_dir)
