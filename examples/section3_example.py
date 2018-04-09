# The following is a replica of the example mentioned in Section3


def build_sample_record(records, schema, byteorder):
    """Build a byte record that is similar to that presented in Figure 2

    The record data is just a sequence of null bytes

    :param list records: A list of (record type, record size) tuples
    :param dict schema: A dict of file schema byte sizes
    :param str byteorder: The way that the
    :return:
    """
    sample_input = bytearray()

    # Read the schema information for building the file
    header_byte_size = schema['header_byte_size']
    record_type_byte_size = schema['record_type_byte_size']
    record_size_byte_size = schema['record_size_byte_size']

    # Build the header, as a 4 byte representation
    num_records = len(records)
    file_header = num_records.to_bytes(header_byte_size, byteorder=byteorder)
    sample_input.extend(file_header)

    # Build out the two records
    for record in records:
        rt, rs = record

        # Record type, 2 byte representation
        rt_bytes = rt.to_bytes(record_type_byte_size, byteorder=byteorder)
        sample_input.extend(rt_bytes)

        # Record size, 2 byte representation
        rs_bytes = rs.to_bytes(record_size_byte_size, byteorder=byteorder)
        sample_input.extend(rs_bytes)

        # Now add in records data as an empty byte representation
        # Note: -4 is to remove the bytes for rt and rl
        sample_input.extend(bytes(rs - 4))

    return sample_input


def parse_sample_record(input, schema, byteorder):
    """Parse a bytearray using a fileschema

    :param bytearray input:
    :param dict schema: A dict of file schema byte sizes
    :return:
    """

    input_len = len(input)
    result_list = []

    # Read the schema information for parsing the file
    header_byte_size = schema['header_byte_size']
    record_type_byte_size = schema['record_type_byte_size']
    record_size_byte_size = schema['record_size_byte_size']

    # Get the number of records in the input
    i = header_byte_size
    num_records = int.from_bytes(input[0:i], byteorder=byteorder)

    while i < input_len:
        # Read the record type
        record_type_bytes = input[i:i + record_type_byte_size]
        record_type = int.from_bytes(record_type_bytes, byteorder=byteorder)
        i += record_type_byte_size

        # Read the record size
        record_size_bytes = input[i: i + record_size_byte_size]
        record_size = int.from_bytes(record_size_bytes, byteorder=byteorder)
        i += (record_size - record_type_byte_size)

        result_list.append((record_type, record_size))

    assert (len(result_list) == num_records, "Records found, did not equal records specified in header")

    return result_list


def main():
    # Schema for the file input
    schema = {
        "header_byte_size": 4,
        "record_type_byte_size": 2,
        "record_size_byte_size": 2
    }
    byteorder = 'big'

    # Section 3.2: Build a sample

    # records consists of tuples represented as:
    # 1.  Record type
    # 2.  Record length
    records = [(1, 13), (5, 10)]
    sample_input = build_sample_record(records, schema, byteorder)

    # Parse the sample file
    parsed_results = parse_sample_record(sample_input, schema, byteorder)
    print(parsed_results)


if __name__ == "__main__":
    main()
