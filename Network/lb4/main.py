from pysnmp.hlapi import *


def snmp_get(ip, oid):
    # Выполнение SNMP GET-запроса
    error_indication, error_status, error_index, var_binds = next(
        getCmd(
            SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
    )

    # Обработка ошибок
    if error_indication:
        print(f"Ошибка: {error_indication}")
        return None
    elif error_status:
        print(f"Ошибка SNMP: {error_status.prettyPrint()} (индекс: {error_index})")
        return None

    # Обработка успешного результата
    for var_bind in var_binds:
        print(f"{var_bind[0]} = {var_bind[1]}")
    return var_bind[1]  # Возвращаем последнее значение


# Пример использования с интерпретацией статуса
status = snmp_get('192.168.1.1', '1.3.6.1.2.1.2.2.1.8.1')  # ifOperStatus OID
if status is not None:
    print(f"Статус интерфейса: {'Up' if int(status) == 1 else 'Down'}")
