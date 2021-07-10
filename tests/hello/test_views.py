
def test_hello_page(test_client):
    response = test_client.get("/hello/world/")
    assert response.status_code == 200
    assert b"Hello world!" == response.data


def test_privet_page(test_client):
    response = test_client.get("/hello/privet/")
    assert response.status_code == 200
    assert b"Privet!" == response.data
