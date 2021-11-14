from memory import paging
from memory import units_converter
from os import system


def wait(msg):
    print(msg)
    input("Press Enter to continue...")


def main():
    while True:
        system("cls")
        print(
            """\t\tPaging Menu:\n
    [1] Get logical/virtual address length (in bits)
    [2] Get physical/real address length (in bits)
    [3] Get physical/real address (given a virtual address and the page size)
    """
        )
        opt = input("Enter an option: ")
        system("cls")
        if opt == "1":
            pages = int(input("Number of pages: "))
            page_size = int(input("Page space in bytes (e.g. 1024): "))
            wait(paging.get_logical_address_length(pages, page_size))

        if opt == "2":
            frames = int(input("Number of frames: "))
            frame_size = int(input("Frame space in bytes (e.g. 1024): "))
            wait(paging.get_physical_address_length(frames, frame_size))

        if opt == "3":
            print("Valid units: GB, MB, KB, B, b (e.g. 1MB, 6KB, 2B, ...)\n\n")
            virtual_address = input("Enter virtual address: ").strip()
            page_size = units_converter.convert_size_unit_to_bytes(
                *units_converter.decompose_number(
                    input("Enter page size (see valid units above): ").strip()
                )
            )
            wait(
                f"Real direction is: {paging.get_real_address(virtual_address, page_size)}"
            )


if __name__ == "__main__":
    main()