import argparse
from gendiff.gendiff_work import generate_diff


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(prog='gendiff', description=description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-v', '--version', action='version',
                        version='Current version is 1.0')
    parser.add_argument(
        '-f', '--format', choices=['stylish', 'plain', 'json'],
        help='output format(default: stylish)', default='stylish'
    )
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
