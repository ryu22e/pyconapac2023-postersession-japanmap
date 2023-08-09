def test_get_prefs(html, responses):
    from postersession.pyconjp import get_prefs

    responses.add(
        responses.GET,
        "https://www.pycon.jp/support/bootcamp.html",
        body=html.read("pyconjp.html"),
    )

    actual = sorted(list(get_prefs()))

    expected = sorted(
        [
            "北海道",
            "岩手",
            "宮城",
            "山形",
            "福島",
            "茨城",
            "栃木",
            "群馬",
            "埼玉",
            "千葉",
            "神奈川",
            "山梨",
            "長野",
            "新潟",
            "富山",
            "石川",
            "福井",
            "静岡",
            "愛知",
            "岐阜",
            "京都",
            "大阪",
            "兵庫",
            "和歌山",
            "岡山",
            "広島",
            "山口",
            "香川",
            "愛媛",
            "徳島",
            "高知",
            "福岡",
            "佐賀",
            "長崎",
            "熊本",
            "鹿児島",
            "沖縄",
        ]
    )
    assert actual == expected
