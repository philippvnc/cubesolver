class TableSaver:
    __FILE_EXTENSION = ".py"
    __GENERATED_DIR = "generated/"

    @staticmethod
    def save_table(table, name: str) -> None:
        file_name = TableSaver.__GENERATED_DIR + name.lower() + TableSaver.__FILE_EXTENSION
        table_name = name.upper()

        # Replace unreachable -1 states with 255 so it fits in the byte range
        sanitized = [(v if v >= 0 else 255) for v in table]

        byte_values = bytes(sanitized)

        with open(file_name, "w") as f:
            f.write(table_name + " = ")
            f.write(repr(byte_values))
            f.write("\n")

        print(f"generated {file_name}")
