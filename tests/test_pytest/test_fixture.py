# file relates to fixtures - request, factories, parameterization, scope

def test_fixture_request(data_verify):
    assert 1 == 1


# using fixture - data_type_collection
def test_data_type_collection_fixture(data_type_collection):
    # calling the same fixture with different argument
    assert data_type_collection("list") == [1, 2, 3]
    assert data_type_collection("tuple") == (2,4,5)
    assert type(data_type_collection("string")) == list


# parameterization using fixtures
def test_param(data_for_fixture, access_data):
    if access_data == "access":
        assert type(data_for_fixture) in [tuple, list]
    elif access_data == "split":
        assert len(data_for_fixture) == 2 or 3
    elif access_data == "assign":
        data_for_fixture[1] = 9
        assert True

