class TableSaver:
    _FILE_EXTENSION = ".py"
    _GENERATED_DIR = "generated/"

    @staticmethod
    def save_table(table, name: str) -> None:
        file_name = TableSaver._GENERATED_DIR + name.lower() + TableSaver._FILE_EXTENSION
        table_name = name.upper()

        byte_values = bytes(table)

        with open(file_name, "w") as f:
            f.write(table_name + " = ")
            f.write(repr(byte_values))
            f.write("\n")

        print(f"generated {file_name}")
