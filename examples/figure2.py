# The following is a replica of "Figure 2: Running example input"

def build_sample_record(byteorder):
    sample_input = bytearray()

    # Build the header, as a 4 byte representation
    num_records = 2
    file_header = num_records.to_bytes(4, byteorder=byteorder)
    sample_input.extend(file_header)

    # records consists of tuples represented as:
    # 1.  Record type
    # 2.  Record length
    records = [(1, 13), (5, 10)]

    # Build out the two records
    for record in records:
        rt, rl = record

        # Record type, 2 byte representation
        rt_bytes = rt.to_bytes(2, byteorder=byteorder)
        sample_input.extend(rt_bytes)

        # Record size, 2 byte representation
        rl_bytes = rl.to_bytes(2, byteorder=byteorder)
        sample_input.extend(rl_bytes)

        # Now add in records data as an empty byte representation
        # Note: -4 is to remove the bytes for rt and rl
        sample_input.extend(bytes(rl - 4))

    return sample_input


def main():
    sample_input = build_sample_record('big')
    print(sample_input)


if __name__ == "__main__":
    main()
