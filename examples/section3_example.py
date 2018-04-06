# The following is a replica of the example mentioned in Section3


def build_sample_record(records, byteorder):
    """Build a byte record that is similar to that presented in Figure 2

    The record data is just a sequence of null bytes

    :param list records: A list of (record type, record size) tuples
    :param str byteorder: The way that the
    :return:
    """
    sample_input = bytearray()

    # Build the header, as a 4 byte representation
    num_records = len(records)
    file_header = num_records.to_bytes(4, byteorder=byteorder)
    sample_input.extend(file_header)

    # Build out the two records
    for record in records:
        rt, rs = record

        # Record type, 2 byte representation
        rt_bytes = rt.to_bytes(2, byteorder=byteorder)
        sample_input.extend(rt_bytes)

        # Record size, 2 byte representation
        rs_bytes = rs.to_bytes(2, byteorder=byteorder)
        sample_input.extend(rs_bytes)

        # Now add in records data as an empty byte representation
        # Note: -4 is to remove the bytes for rt and rl
        sample_input.extend(bytes(rs - 4))

    return sample_input


def parse_sample_record(input):
    pass


def main():
    # Get the sample input

    # records consists of tuples represented as:
    # 1.  Record type
    # 2.  Record length
    records = [(1, 13), (5, 10)]
    sample_input = build_sample_record(records, 'big')
    print(sample_input)


if __name__ == "__main__":
    main()
