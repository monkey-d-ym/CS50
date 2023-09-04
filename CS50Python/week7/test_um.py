from um import count

def test_um():
    assert count("um?") == 1
def test_um_in_word():
    assert count("Um, thanks for the album.") == 1
def test_ums():
    assert count("Um, thanks, um...") == 2
