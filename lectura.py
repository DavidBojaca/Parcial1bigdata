import boto3
from datetime import datetime
from urllib.request import urlopen


def get_url():
    return "https://casas.mitula.com.co/searchRE" + \
           "/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/" + \
           "orden-0/op-1/m2_min-1/m2_max-200/hab_min-1/" + \
           "ban_min-1/q-bogot%C3%A1?req_sgmt=" + \
           "REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=="


def get_boto():
    return boto3.client('s3')


def get_date():
    return datetime.today().strftime('%Y-%m-%d')


def f():
    fecha_actual = get_date()
    url = get_url()
    with urlopen(url) as response:
        html = response.read()
    s3 = get_boto()
    s3.put_object(Body=html,
                  Bucket='lecturadatoscasas',
                  Key=str(fecha_actual)+".html")
    
    
    
