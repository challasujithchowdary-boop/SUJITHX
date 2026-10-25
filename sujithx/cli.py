"""SUJITHX - Unified Python Toolkit Command Center."""

from . import (
    hello,
    analyze_folder,
    search_files,
    find_duplicates,
    largest_files,
    format_bytes,
    generate_token,
    generate_password,
    check_password_strength,
    ensure_directory,
    get_file_info,
    banner,
    success,
    error,
    info,
    display_system_info,
    get_network_info,
    create_logger,
)


def show_menu():
    print("\n1. Welcome")
    print("2. Analyze folder")
    print("3. Search files")
    print("4. Find duplicate files")
    print("5. Show largest files")
    print("6. Generate secure token")
    print("7. Generate password")
    print("8. Check password strength")
    print("9. Create folder")
    print("10. Get file information")
    print("11. System information")
    print("12. Network information")
    print("13. Logging demonstration")
    print("0. Exit")


def main():
    print(banner("SUJITHX COMMAND CENTER"))
    logger = create_logger("SUJITHX_CLI", "sujithx_cli.log")

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                name = input("Your name: ").strip() or "Developer"
                print(success(hello(name)))

            elif choice == "2":
                folder = input("Folder path: ").strip().strip('"')
                result = analyze_folder(folder)
                print("Folder:", result["folder"])
                print("Files:", result["file_count"])
                print("Size:", format_bytes(result["total_bytes"]))
                print("Extensions:", result["extensions"])

            elif choice == "3":
                folder = input("Folder path: ").strip().strip('"')
                pattern = input("Pattern (default ): ").strip() or ""
                results = search_files(folder, pattern)
                for path in results:
                    print(path)
                print(f"Found {len(results)} file(s).")

            elif choice == "4":
                folder = input("Folder path: ").strip().strip('"')
                groups = find_duplicates(folder)
                if not groups:
                    print(success("No duplicates found."))
                else:
                    for group in groups:
                        print("\nDuplicate group:")
                        for path in group:
                            print(" ", path)

            elif choice == "5":
                folder = input("Folder path: ").strip().strip('"')
                for path, size in largest_files(folder, 10):
                    print(f"{format_bytes(size):>12}  {path}")

            elif choice == "6":
                print("Generated token:", generate_token())

            elif choice == "7":
                print("Generated password:", generate_password())

            elif choice == "8":
                password = input("Password to evaluate: ")
                result = check_password_strength(password)
                print("Rating:", result["rating"])
                print("Checks:", result["checks"])

            elif choice == "9":
                folder = input("Folder path to create: ").strip().strip('"')
                print(success(ensure_directory(folder)))

            elif choice == "10":
                path = input("File path: ").strip().strip('"')
                for key, value in get_file_info(path).items():
                    print(f"{key}: {value}")

            elif choice == "11":
                display_system_info()

            elif choice == "12":
                for key, value in get_network_info().items():
                    print(f"{key.replace('_', ' ').title()}: {value}")

            elif choice == "13":
                logger.info("SUJITHX logging demonstration.")
                logger.warning("This is a sample warning.")
                print(success("Log messages written to sujithx_cli.log"))

            elif choice == "0":
                print(success("SUJITHX closed. Goodbye!"))
                break

            else:
                print(error("Choose a number from 0 to 13."))

        except (OSError, ValueError, TypeError) as exc:
            print(error(str(exc)))


if __name__ == "__main__":
    main()