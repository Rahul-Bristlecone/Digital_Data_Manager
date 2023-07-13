from dtm import order_check


def test_assert():
    assert True


def test_order_no():
    test_order_data = [('536634455', False), ('88778799823321', True), ('7849777900280047834', False),
                       ('jkjsaisd', False), ('TRYuhwubbjeurd', True), ('HYTUIhjkdiejjkrkied', False),
                       ('TREE564', False), ('Hulk8938892', True), ('099040jknsmmkask8989as9', False),
                       ('HJU@67869', False), ('Yutr_892738', True), ('YYUY_oewioewo877676', False),
                       ]
    for data in test_order_data:
        assert order_check(data[0]) == data[1]
