# -*- coding: utf-8 -*-

"""
Protocol Buffer

编译命令：protoc --python_out=$DST_DIR $SRC_DIR/address_book.proto
文档：https://developers.google.com/protocol-buffers/docs/pythontutorial
"""

import address_book_pb2 as pb

if __name__ == '__main__':
    person = pb.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = pb.PhoneType.HOME
    # 序列化
    seri_out = person.SerializeToString()
    print(seri_out)

    # 反序列化
    dese_person = pb.Person()
    dese_person.ParseFromString(seri_out)
    print(dese_person.id, dese_person.name)
