def test_save_image(tmp_path):
    from postersession.japanmap import save_image

    actual = save_image(["北海道", "東京"], tmp_path / "test.png")

    expected = tmp_path / "test.png"
    assert actual == expected
    assert actual.exists()
