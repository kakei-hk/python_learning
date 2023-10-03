import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test arguments parser")
    parser.add_argument("must_arg", help="Required argument")
    parser.add_argument("-m", required=True, help="Hyphenated required argument")
    parser.add_argument("--opt_arg", help="Optional argument")
    parser.add_argument("-t", "--test_arg", help="Abbreviation of --test_arg")
    parser.add_argument(
        "--int_arg", type=int, default=0, help="int-type argument (default is 0)"
    )
    parser.add_argument(
        "--flag", action="store_true", help="Flag argument (store_true)"
    )
    parser.add_argument("--choice", choices=["choice1", "choice2"], default="choice1")
    parser.add_argument("--list0", nargs="*", help="List of 0 or more")
    parser.add_argument("--list1", nargs="+", default="1", help="List of 1 or more")
    parser.add_argument(
        "--list2", nargs=2, default=["1", "2"], help="List of 2 or more"
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    print(f"must_arg; {args.must_arg}")
    print(f"m; {args.m}")
    print(f"opt_arg; {args.opt_arg}")
    print(f"test_arg; {args.test_arg}")
    print(f"int_arg; {args.int_arg}")
    print(f"flag; {args.flag}")
    print(f"choice; {args.choice}")
    print(f"list0; {args.list0}")
    print(f"list1; {args.list1}")
    print(f"list2; {args.list2}")


if __name__ == "__main__":
    main()
