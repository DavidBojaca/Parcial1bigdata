import boto3
from datetime import datetime
from lectura import get_url, get_boto, get_date


def test_get_url():
    assert get_url() == "https://casas.mitula.com.co/searchRE" + \
                        "/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/" + \
                        "orden-0/op-1/m2_min-1/m2_max-200/hab_min-1/" + \
                        "ban_min-1/q-bogot%C3%A1?req_sgmt=" + \
                        "REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=="


def test_get_date():
    dt = get_date()
    assert dt == datetime.today().strftime('%Y-%m-%d')


def test_get_boto(mocker):
    mocker.patch("boto3.client")
    s3_mock = mocker.MagicMock()
    boto3.client.return_value = s3_mock
    s3 = get_boto()
    assert s3 == s3_mock
